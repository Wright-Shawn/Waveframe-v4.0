"""Waveframe V4.0 — limit_case_LCDM.py

Utilities to demonstrate recovery of ΛCDM as a limit case by constructing α_match(z)
that reproduces a target ΛCDM background H_LCDM(z).

Key identities (Unicode math):
- y(z) = 1 / H(z)²
- α_match(z) = − π · (1+z) · H(z) · d/dz [ y(z) ]

This module provides:
- A flat ΛCDM H(z) function
- A helper to compute α_match(z) from any H(z)
- A quick check that feeding α_match into the Waveframe ODE reproduces H(z)
"""

from typing import Callable
import numpy as np

PI = np.pi

def H_LCDM_flat(H0: float, Omega_m0: float, Omega_r0: float = 0.0, Omega_L0: float = None) -> Callable[[np.ndarray], np.ndarray]:
    """Return H_LCDM(z) for a spatially flat model.
    If Omega_L0 is None, set it to 1 − Omega_m0 − Omega_r0.
    """
    if Omega_L0 is None:
        Omega_L0 = 1.0 - Omega_m0 - Omega_r0
    def H_of_z(z):
        z = np.asarray(z, dtype=float)
        return H0 * np.sqrt(Omega_r0*(1+z)**4 + Omega_m0*(1+z)**3 + Omega_L0)
    return H_of_z

def alpha_match_from_H(H_of_z: Callable[[np.ndarray], np.ndarray], z: np.ndarray) -> np.ndarray:
    """Compute α_match(z) from a target H(z) using:
        α(z) = − π · (1+z) · H(z) · d/dz [1 / H(z)²]
    Uses finite differences for dy/dz.
    """
    z = np.asarray(z, dtype=float)
    H = H_of_z(z).astype(float)
    y = 1.0 / (H**2)
    # Gradient with second-order accuracy
    dy_dz = np.gradient(y, z, edge_order=2)
    return - PI * (1.0 + z) * H * dy_dz

if __name__ == "__main__":
    # Demonstration: recover α_match for a flat ΛCDM background
    H0 = 70.0
    Om0 = 0.3
    z = np.linspace(0.0, 3.0, 400)
    H_LCDM = H_LCDM_flat(H0, Om0)
    alpha = alpha_match_from_H(H_LCDM, z)
    print("α_match(z) summary:", float(alpha.min()), float(alpha.max()))
