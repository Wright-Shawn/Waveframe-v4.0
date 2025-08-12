"""Waveframe V4.0 — entropy_variational_solver.py

General solver for the entropy–action background in *time* t.

Core equations (Unicode math):
- dH/dt = − α(t) / (2π) · H³
- dS/dt = α(t)
- da/dt = a · H

Given α(t) (constant or callable), this integrates H(t), S(t), and a(t)
from t0 to tf with initial conditions H(t0)=H0, S(t0)=S0, a(t0)=1.
"""

from typing import Callable, Dict
import numpy as np
from scipy.integrate import solve_ivp

PI = np.pi

def integrate_background_time(
    t_span: tuple,
    H0: float,
    S0: float,
    alpha_of_t: Callable[[float], float],
    rtol: float = 1e-8,
    atol: float = 1e-10,
) -> Dict[str, np.ndarray]:
    """Integrate the background equations in time.

    Parameters
    ----------
    t_span : (t0, tf)
        Time interval to integrate over.
    H0 : float
        H(t0) initial value.
    S0 : float
        S(t0) initial value.
    alpha_of_t : callable
        Function α(t).
    rtol, atol : float
        ODE tolerances.

    Returns
    -------
    dict with keys: t, H, S, a
    """
    def rhs(t, y):
        H, S, a = y
        alpha = alpha_of_t(t)
        dH = - alpha * (H**3) / (2.0 * PI)
        dS = alpha
        da = a * H
        return [dH, dS, da]

    y0 = [H0, S0, 1.0]
    sol = solve_ivp(rhs, t_span, y0, rtol=rtol, atol=atol, dense_output=False)
    if not sol.success:
        raise RuntimeError(f"Time integration failed: {sol.message}")
    t = sol.t
    H, S, a = sol.y
    return {"t": t, "H": H, "S": S, "a": a}

def alpha_constant(value: float) -> Callable[[float], float]:
    """Return α(t) = value."""
    return lambda t: float(value)

def alpha_tanh(t0: float, width: float, low: float, high: float) -> Callable[[float], float]:
    """Smooth step: α(t) = low + (high − low)/(1 + exp(−(t − t0)/width))."""
    def fn(t):
        return low + (high - low) / (1.0 + np.exp(-(t - t0)/width))
    return fn

if __name__ == "__main__":
    # Example: integrate with constant α
    out = integrate_background_time(t_span=(0.0, 10.0), H0=70.0, S0=0.0, alpha_of_t=alpha_constant(0.02))
    print("Integrated points:", len(out["t"]))
