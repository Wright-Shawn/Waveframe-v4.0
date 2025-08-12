"""Waveframe V4.0 — structure_growth.py

Compute the linear growth factor D(a) and fσ₈(z) on a background defined by H(z).

We adopt the standard (general-relativistic) linear growth equation with a modified
background H(a); this is the minimal comparison model for RSD constraints:

In terms of scale factor a:

    d²D/da² + [ (3/a) + d ln H / d ln a ] dD/da − (3/2) Ω_m(a) D / a² = 0

where
    Ω_m(a) = Ω_m0 · a^(−3) · (H0/H(a))²

Outputs:
- D(a) normalized to D(a=1) = 1
- f(z) = d ln D / d ln a
- fσ₈(z) = f(z) · σ₈(a), where σ₈(a) = σ₈0 · D(a)

All math uses Unicode in docstrings. Code uses Python, NumPy, SciPy.
"""

from typing import Callable, Tuple
import numpy as np
from scipy.integrate import solve_ivp

def compute_growth_from_H(
    z_grid: np.ndarray,
    H_of_z: Callable[[np.ndarray], np.ndarray],
    H0: float,
    Omega_m0: float,
    sigma8_0: float = 0.8,
    rtol: float = 1e-7,
    atol: float = 1e-9,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute D(a), f(z), and fσ₈(z) given H(z).

    Parameters
    ----------
    z_grid : array
        Monotonic non-negative redshift grid, includes z=0.
    H_of_z : callable
        Function returning H(z) on the provided grid values.
    H0 : float
        Hubble constant today, same units as H_of_z output.
    Omega_m0 : float
        Present-day matter density parameter.
    sigma8_0 : float
        σ₈ today (normalization). Default 0.8.
    rtol, atol : float
        ODE tolerances.

    Returns
    -------
    D_of_z : array
        Linear growth factor normalized to 1 at z=0.
    f_of_z : array
        Growth rate f = d ln D / d ln a.
    fsigma8_of_z : array
        fσ₈(z) = f(z) · σ₈0 · D(z).
    """
    z_grid = np.asarray(z_grid, dtype=float)
    if z_grid[0] != 0.0:
        raise ValueError("z_grid must start at 0 for normalization D(0)=1.")
    if not np.all(np.diff(z_grid) >= 0):
        raise ValueError("z_grid must be non-decreasing.")

    # Prepare a-grid (integration runs from a=1 back to a at max z)
    a_grid = 1.0 / (1.0 + z_grid)
    H_grid = H_of_z(z_grid).astype(float)

    # Interpolants for H(a) and ln H derivative
    # Use simple linear interpolation in log-space for stability
    import numpy as np

    def H_of_a(a: np.ndarray) -> np.ndarray:
        # map a to z
        z = 1.0 / a - 1.0
        return H_of_z(z)

    # derivative d ln H / d ln a via finite differences on the provided grid
    lnH = np.log(H_grid)
    lna = np.log(a_grid)
    dlnH_dlnA = np.gradient(lnH, lna, edge_order=2)

    def dlnH_dlnA_of_a(a: float) -> float:
        # interpolate over the precomputed grid
        return np.interp(np.log(a), lna, dlnH_dlnA)

    def Omega_m_of_a(a: float) -> float:
        # Ω_m(a) = Ω_m0 a^(−3) (H0/H(a))²
        Ha = H_of_a(np.array([a]))[0]
        return Omega_m0 * a**(-3) * (H0/Ha)**2

    # ODE for D as function of a
    def rhs(a, y):
        D, dD_da = y
        term = (3.0/a) + dlnH_dlnA_of_a(a)
        grav = 1.5 * Omega_m_of_a(a) / (a**2)
        d2D_da2 = - term * dD_da + grav * D
        return [dD_da, d2D_da2]

    # Integrate from a=1 to smallest a (highest z), then interpolate back
    a_span = (1.0, a_grid[-1])
    if a_grid[-1] < 1.0:
        # integrate backward
        a_span = (1.0, a_grid[-1])
    else:
        raise ValueError("z_grid must extend to z >= 0; a must be ≤ 1.")

    # Initial conditions at a=1: D=1, dD/da ≈ f0 / a where f0 ~ Ω_m0^0.55 as a guess
    f0_guess = Omega_m0**0.55
    y0 = [1.0, f0_guess]  # approximate derivative at a=1

    sol = solve_ivp(rhs, a_span, y0, t_eval=a_grid[::-1], rtol=rtol, atol=atol, method="RK45")
    if not sol.success:
        raise RuntimeError(f"Growth ODE failed: {sol.message}")

    D_rev = sol.y[0]
    D = D_rev[::-1]  # reorder to match ascending z_grid

    # Compute f = d ln D / d ln a from D(a)
    dlnD_dlnA = np.gradient(np.log(np.maximum(D, 1e-300)), lna, edge_order=2)
    f = dlnD_dlnA

    # σ₈(a) = σ₈0 · D(a)
    fs8 = f * (sigma8_0 * D)

    return D, f, fs8

if __name__ == "__main__":
    # Simple smoke test with a made-up H(z) flat model
    z = np.linspace(0, 2.0, 300)
    # Example H(z): H = H0 * sqrt(Ωm(1+z)^3 + ΩΛ)
    H0 = 70.0
    Om0 = 0.3
    Ol0 = 0.7
    def H_flat_LCDM(z_arr):
        z_arr = np.asarray(z_arr, dtype=float)
        return H0 * np.sqrt(Om0*(1+z_arr)**3 + Ol0)
    D, f, fs8 = compute_growth_from_H(z, H_flat_LCDM, H0, Omega_m0=Om0, sigma8_0=0.8)
    print("D(0)=", D[0], "  f(0)=", f[0], "  fσ8(0)=", fs8[0])
