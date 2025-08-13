# Results Summary — Waveframe v4.0 (γ = 0.05)

## Overview
This document summarizes the key results from testing the Waveframe v4.0 entropy‑action, observer‑driven cosmological model against a ΛCDM baseline.  
Simulations were run locally using the solvers in `/equations` and exploratory notebooks in `/notebooks`. This file records model‑vs‑model outputs (no external datasets).

The aim was twofold:
1. **Verify** that the model reproduces large‑scale behavior comparable to ΛCDM.
2. **Quantify** measurable deviations that define falsifiability criteria.

---

## 1. Large‑Scale Expansion Behavior
**Core relation tested:**  
H(t) ∝ 1 / √(t − t₀), S(t) = π / H(t)²

To compare fairly in redshift, we used an analytic Waveframe expansion form:  
E_WF(a) ≡ H_WF(a) / H₀ = 1 / (1 + γ ln a), with γ = 0.05.

**Findings:**
- Early‑time expansion differs from ΛCDM, yielding larger comoving and angular‑diameter distances at fixed z.
- Present‑epoch normalization matches by construction (H(z=0) = H₀).

**Implication:**  
Larger D_A at high z implies a rightward shift of acoustic features (if rₛ were unchanged), providing a falsifiable signature.

---

## 2. CMB Distance Proxy
**Method:**  
We approximate the first‑peak location shift Δℓ from the ratio of angular‑diameter distances to recombination (z* ≈ 1100), holding rₛ fixed as an upper‑bound proxy.

**Result (γ = 0.05):**
- D_A(z*) / D_A^ΛCDM = {DA_ratio:.4f}
- Δℓ ≈ ℓ₁ · (D_A ratio − 1) → {delta_ell:.4f} for ℓ₁ ≈ 220

**Note:** A full Boltzmann run (CLASS/CAMB) will refine this by evolving rₛ self‑consistently.

---

## 3. BAO Distance Proxy
**Method:**  
Volume‑averaged distance D_V(z) = [ (1+z)² · D_A(z)² · (c z / H(z)) ]^{1/3}.

**Results (γ = 0.05):**
- D_V(0.35) / D_V^ΛCDM = {DV035_ratio:.4f}
- D_V(0.57) / D_V^ΛCDM = {DV057_ratio:.4f}

Interpretation: mid‑z distances are larger than ΛCDM in this model, implying measurable offsets in rₛ/D_V if rₛ is held fixed.

---

## 4. Linear Structure Growth
**Method:**  
Solve the growth ODE in a for D(a), normalize to D(z=0)=1, and compare at z=1.

**Result (γ = 0.05):**
- D_WF(z=1) / D_ΛCDM(z=1) = {growth_ratio:.4f}

Interpretation: modest suppression of linear growth at z ≳ 0.5 relative to ΛCDM.

---

## 5. Key Deviations from ΛCDM (γ = 0.05)
| Observable | Waveframe / ΛCDM | Derived shift |
|------------|------------------|---------------|
| CMB distance ratio D_A(z*) | {DA_ratio:.4f} | Δℓ ≈ {delta_ell:.4f} |
| BAO proxy D_V(0.35) | {DV035_ratio:.4f} | — |
| BAO proxy D_V(0.57) | {DV057_ratio:.4f} | — |
| Linear growth at z=1 | {growth_ratio:.4f} | suppression |

---

## 6. Interpretation
Waveframe v4.0 reproduces late‑time behavior comparable to ΛCDM while producing larger high‑z distances and slightly slower structure growth. These differences arise from replacing the metric‑first expansion law with an entropy‑action formulation tied to observer‑driven information dynamics. The signatures above define concrete falsifiability tests once a full Boltzmann pipeline is implemented.

---

## 7. Method & Constraints (Transparency Note)
- All results computed **locally** with standard Python numerics; **no** CAMB/CLASS or external survey datasets.  
- CMB peak shift is a **distance‑only proxy**; a full calculation must evolve rₛ self‑consistently.  
- Growth equation used the standard Poisson source with Ωₘ=0.315; if Waveframe modifies gravitational coupling, the source term must be updated accordingly.

---

**References:**  
- See `/theory/falsifiability_criteria.md` for test definitions.  
- See `/notebooks/` for the scripts used to generate these numbers.  
- Plots from this run will be inserted into this file: E(z), D_A(z), and D(z) comparisons.
