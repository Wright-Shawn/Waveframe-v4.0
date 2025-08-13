# ΛCDM Comparison — Waveframe v4.0 (γ = 0.05)

## Overview
This document compares the Waveframe v4.0 entropy‑action, observer‑driven model (γ = 0.05) directly to a ΛCDM baseline.  
All results are from local theory–theory calculations without external datasets, performed using Python scripts in `/notebooks` and `/equations`.

---

## 1. Model Definitions
- **ΛCDM:** Ωₘ = 0.315, ΩΛ = 0.685, H₀ = 67.4 km/s/Mpc  
- **Waveframe v4.0:** H(t) ∝ 1 / √(t − t₀), implemented as E_WF(a) = 1 / (1 + γ ln a), γ = 0.05, normalized to H(z=0) = H₀.

---

## 2. Results Table (γ = 0.05)

| Observable | Waveframe / ΛCDM | Derived shift / Interpretation |
|------------|------------------|--------------------------------|
| CMB distance ratio D_A(z*) | 245.7160 | Δℓ ≈ 53837.5200 (distance‑only proxy) |
| BAO proxy D_V(0.35) | 1.1191 | Larger mid‑z volume‑avg distance |
| BAO proxy D_V(0.57) | 1.2113 | Larger mid‑z volume‑avg distance |
| Linear growth at z=1 | 0.8481 | Suppressed vs ΛCDM |

---

## 3. Figures

**E(z) — Expansion Rate Ratio**  
![E(z) = H(z)/H0](Figures/E(z) = H(z):H0.png)

**Angular Diameter Distance D_A(z)**  
![Angular Diameter Distance D_A(z)](Figures/Angular Diameter Distance D_A(z).png)

**Linear Growth Factor D(z)**  
*(This figure should be saved from local runs as Growth_D(z).png and placed in Figures/)*

---

## 4. Interpretation
- Waveframe v4.0 predicts larger high‑z distances than ΛCDM, leading to a positive Δℓ if rₛ is unchanged.  
- BAO D_V values are similarly larger, implying measurable differences in rₛ/D_V in principle.  
- Structure growth is modestly suppressed at z ≥ 0.5 compared to ΛCDM.

These differences are direct consequences of replacing the metric‑based expansion law with an entropy‑action formulation tied to observer‑driven information dynamics.

---

## 5. Method & Constraints
- Computations done **locally** without CAMB/CLASS; no observational datasets used.  
- CMB shift values are **distance‑only** proxies; a full treatment requires evolving rₛ in a Boltzmann solver.  
- Results serve as **proof‑of‑concept** for AI‑orchestrated multi‑thread research workflows, not as a complete cosmological model.

---

**References:**  
- `/theory/falsifiability_criteria.md` — defines testable predictions.  
- `/Analysis/01_results_summary_unicode.md` — narrative results summary.  
