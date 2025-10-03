# Extended Methodology & Workflow Details

This document provides the extended context for **Waveframe v4.0**,  
covering methodology, scaffolds for falsifiability, empirical criteria,  
and orchestration details.  

---

## Orchestration (AI-Assisted Development)

Waveframe v4.0 was developed through **parallel AI prompt streams, targeted critiques, and human-in-the-loop gating**.  
The orchestration process is logged in `/Docs/` and summarized here:

- **Parallel AI threads** handled derivations, predictions, and documentation.  
- **Critic roles** checked outputs for consistency, validity, and errors.  
- **Human validation** acted as the final gatekeeper before commits.  
- **Decision logs** in `/decisions` capture tradeoffs and rationale.  

This workflow demonstrates **AI Workflow Orchestration (AWO):**  
turning ambiguous research into reproducible, auditable artifacts.

---

## Overview of the Model

Waveframe explores an **entropy–action, observer-driven expansion law** as an alternative to ΛCDM.  
The physics is exploratory; the emphasis is on **packaging the research in a reproducible workflow**.

**Core Tenets**:
1. **Observer-defined horizons** replace a single global geometry.  
2. **Spacetime is emergent**, not fundamental.  
3. **Entropy = Horizon Area**, S(t) = π / [H(t)]².  
4. **Expansion emerges** from resolution-dependent information intake, H(t) ∝ 1 / √(t − t₀).  
5. **Field equations → Information-action principle.**  
6. **Metric tensor → Entropic structure** tied to causal boundaries.  

---

## Research Goals

- Show that an AI-orchestrated workflow can package a speculative cosmological model.  
- Demonstrate falsifiability scaffolds in a scientific repo.  
- Recover ΛCDM behaviors in the correct limits.  
- Predict measurable deviations in observables (CMB, BAO, growth of structure).  
- Provide a transparent, reproducible audit trail.

---

## Falsifiability Scaffolds

Waveframe is not positioned as a finished theory.  
Instead, it demonstrates **how falsifiability can be scaffolded** inside a research repo.  

**Checks included** (scaffolded, not fully validated):  
1. **BBN Constraints** – match ΛCDM within ~5% at T ≈ 0.1–10 MeV.  
2. **CMB Acoustic Peaks** – reproduce ΛCDM angular scales at z ≈ 1100.  
3. **Distance–Redshift Relation** – compare SN Ia / BAO curves to ΛCDM.  
4. **Growth of Structure** – test fσ₈(z) vs RSD/weak lensing surveys.  
5. **Limit-Case Recovery** – ensure parameters reduce to ΛCDM.  
6. **Unique Predictions** – at least one divergence measurable against data.  

Each check is treated as **pass/fail**.  
Details are placeholders where the implementation is incomplete, but the workflow shows *how testing would be wired in*.

---

## Empirical Predictions (Audit-Ready)

Each observable links to:  
- A deviation target window vs ΛCDM  
- Dataset to test against  
- Notebook & figure that generate the comparison  

| Observable | z / range | Δ target vs ΛCDM | Dataset | Notebook | Figure | Status |
|------------|-----------|------------------|---------|----------|--------|--------|
| SN Ia μ(z) | 0–1.5 | ≤ 0.03 mag RMS | Pantheon+/DES | `Notebooks/sn_distance_modulus.ipynb` | `Figures/sn_residuals.png` | ☐ Pending |
| E(z) | 0–2 | ≤ 3% | BAO chronometers | `Notebooks/hubble_Ez_compare.ipynb` | `Figures/Ez_comparison.png` | ☐ Pending |
| Growth fσ₈(z) | 0–1 | −2% … +4% | RSD (BOSS/eBOSS, DES) | `Notebooks/growth_fsigma8.ipynb` | `Figures/fs8_tracks.png` | ☐ Pending |
| CMB θ\* | z≈1100 | ≤ 0.3% | Planck 2018 | `Notebooks/cmb_theta_star.ipynb` | `Figures/theta_star.png` | ☐ Pending |
| D_A(z\*) | z≈1100 | ≤ 1% | Planck 2018 | `Notebooks/cmb_distances.ipynb` | `Figures/DA_recomb.png` | ☐ Pending |

Interpretation rule: if best-fit parameters violate any target → configuration is **falsified**.

---

## Method Limitations

- Calculations are **custom, lightweight numerics** (no CAMB/CLASS solvers yet).  
- CMB/BAO are handled with **distance-only proxies**.  
- Many predictions are **scaffolded placeholders** (to show workflow, not accuracy).  
- Waveframe is **not a replacement for ΛCDM**. It is a **workflow demo**.

---

## Why This Matters

The value of Waveframe v4.0 lies in the **workflow itself**:  

- Turning speculative ideas into **auditable repos**.  
- Showing how to **wire falsifiability** into AI-assisted research.  
- Delivering results as **software-quality, reproducible artifacts**.  

This is an experiment in **continuous research integration (CRI)**,  
where scientific ideas are managed with the same discipline as production software.

---
