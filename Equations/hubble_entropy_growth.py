"""Waveframe V4.0 — hubble_entropy_growth.py

Compute H(z) on a redshift grid from the entropy–action framework:

Core equations (Unicode math):
- Master ODE in redshift for y(z) = 1 / H(z)²:
    dy/dz = − α(z) · √y / [π · (1+z)]

- Initial condition at z = 0:
    y(0) = 1 / H0²

This module provides:
- Built-in α(z) parameterizations (constant, power-law in a, logistic transition)
- Support for custom α(z) callables
- Utility to infer α_match(z) from a target H_target(z) using the identity:
    α(z) = − π · (1+z) · H(z) · d/dz [ 1 / H(z)² ]

All math is in Unicode; the code uses standard Python, NumPy, and SciPy.
"""

from typing import Callable, Sequence, Tuple
import numpy as np
from scipy.integrate import solve_ivp

PI = np.pi

def alpha_constant(value: float) -> Callable[[np.ndarray], np.ndarray]:
    """Return α(z) = value (constant)."""
    def alpha(z):
        return np.full_like(np.asarray(z, dtype=float), float(value))
    return alpha

def alpha_powerlaw_a(alpha0: float, n: float) -> Callable[[np.ndarray], np.ndarray]:
    """Return α(a) = α0 · a^(−n), expressed as α(z).
    Uses a = 1 / (1+z).
    """
    def alpha(z):
        z = np.asarray(z, dtype=float)
        a = 1.0 / (1.0 + z)
        return alpha0 * a**(-n)
    return alpha

def alpha_logistic(zc: float, width: float, low: float, high: float) -> Callable[[np.ndarray], np.ndarray]:
    """Smooth transition: α(z) = low + (high − low) / (1 + exp((z − zc)/width))."""
    def alpha(z):
        z = np.asarray(z, dtype=float)
        return low + (high - low) / (1.0 + np.exp((z - zc)/width))
    return alpha

def infer_alpha_match_from_H(H_of_z: Callable[[np.ndarray], np.ndarray], z: np.ndarray) -> np.ndarray:
    """Infer α_match(z) that *exactly* reproduces the given H(z).

    Uses the identity:
        α(z) = − π · (1+z) · H(z) · d/dz [1 / H(z)²]

    Derivative is computed with a 5-point stencil in z for stability.
    """
    z = np.asarray(z, dtype=float)
    H = H_of_z(z).astype(float)
    y = 1.0 / (H**2)

    # Finite difference derivative dy/dz with interior 5-point stencil, endpoint 3-point
    dy_dz = np.empty_like(z, dtype=float)
    if len(z) < 5:
        # fallback to simple gradient
        dy_dz[:] = np.gradient(y, z, edge_order=2)
    else:
        dz = z[1] - z[0]
        dy_dz[2:-2] = (y[:-4] - 8*y[1:-3] + 8*y[3:-1] - y[4:]) / (12*dz)
        # endpoints: 3-point
        dy_dz[0] = (y[1] - y[0]) / (z[1] - z[0])
        dy_dz[1] = (y[2] - y[0]) / (z[2] - z[0])
        dy_dz[-2] = (y[-1] - y[-3]) / (z[-1] - z[-3])
        dy_dz[-1] = (y[-1] - y[-2]) / (z[-1] - z[-2])

    alpha = - PI * (1.0 + z) * H * dy_dz
    return alpha

def solve_H_of_z(
    z_grid: Sequence[float],
    H0: float,
    alpha_of_z: Callable[[np.ndarray], np.ndarray],
    rtol: float = 1e-8,
    atol: float = 1e-10,
) -> np.ndarray:
    """Solve for H(z) over z_grid given α(z).

    Parameters
    ----------
    z_grid : sequence of float
        Monotonic grid in redshift (e.g., np.linspace(0, 3, 600)). Must start at 0 for IC.
    H0 : float
        Hubble parameter today (same units returned for H(z)).
    alpha_of_z : callable
        Function α(z) returning array of same shape as input.
    rtol, atol : float
        ODE tolerances.

    Returns
    -------
    H : ndarray
        H(z) evaluated on z_grid.
    """
    z_grid = np.asarray(z_grid, dtype=float)
    if z_grid[0] != 0.0:
        raise ValueError("z_grid must start at 0 for the initial condition.")
    if not np.all(np.diff(z_grid) >= 0):
        raise ValueError("z_grid must be non-decreasing.")

    # ODE for y = 1 / H^2
    def rhs(z, y):
        # y is scalar; ensure positivity
        y_val = max(y[0], 1e-300)
        sqrt_y = np.sqrt(y_val)
        alpha = alpha_of_z(z)
        return [- alpha * sqrt_y / (PI * (1.0 + z))]

    y0 = [1.0 / (H0**2)]
    sol = solve_ivp(rhs, (z_grid[0], z_grid[-1]), y0, t_eval=z_grid, rtol=rtol, atol=atol, method="RK45")
    if not sol.success:
        raise RuntimeError(f"ODE solve failed: {sol.message}")
    y = sol.y[0]
    H = 1.0 / np.sqrt(np.maximum(y, 1e-300))
    return H

# Convenience: build α(z) from a simple spec dictionary
def make_alpha(spec: dict) -> Callable[[np.ndarray], np.ndarray]:
    """Create α(z) from a specification dict.

    Examples:
        make_alpha({"type": "constant", "value": 0.01})
        make_alpha({"type": "powerlaw_a", "alpha0": 0.01, "n": 2.0})
        make_alpha({"type": "logistic", "zc": 0.5, "width": 0.2, "low": 0.0, "high": 0.02})
    """
    t = spec.get("type", "constant")
    if t == "constant":
        return alpha_constant(spec["value"])
    if t == "powerlaw_a":
        return alpha_powerlaw_a(spec["alpha0"], spec["n'])
    if t == "logistic":
        return alpha_logistic(spec["zc"], spec["width"], spec["low"], spec["high"])
    raise ValueError(f"Unknown alpha spec type: {t}")

if __name__ == "__main__":
    # Example usage
    z = np.linspace(0.0, 3.0, 400)
    H0 = 70.0  # units arbitrary (e.g., km/s/Mpc)
    alpha = make_alpha({"type": "logistic", "zc": 0.8, "width": 0.3, "low": 0.0, "high": 0.02})
    H = solve_H_of_z(z, H0, alpha)
    # Print a small table
    for zi, Hi in zip(z[::80], H[::80]):
        print(f"z={zi:4.2f}  H(z)={Hi:8.3f}")
