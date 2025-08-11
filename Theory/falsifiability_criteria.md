# Falsifiability Criteria — Waveframe V4.0

## Purpose
Define the **non-negotiable observational tests** that determine whether the Waveframe V4.0 entropy–action cosmology is viable. These tests must be applied to **any** proposed α(t) profile within the model.

---

## 1. Early-Universe Constraints

**1.1 Big Bang Nucleosynthesis (BBN)**  
- Condition: H(t) during **T ≈ 0.1–10 MeV** must match ΛCDM within **±5%**.  
- Justification: Deviations at this level alter light-element abundances beyond observed limits.

**1.2 Cosmic Microwave Background (CMB) Acoustic Scale**  
- Condition: The sound horizon at recombination r_s(z*) and the angular diameter distance D_A(z*) must both match Planck best-fit ΛCDM within **±0.5%** at z* ≈ 1100.  
- Justification: These scales are measured at high precision and serve as “anchor points” for the cosmic expansion history.

---

## 2. Late-Universe Expansion History

**2.1 Hubble Parameter H(z)**  
- Condition: H(z) predictions must agree with combined BAO + SN Ia constraints within **1σ uncertainties** over the range **0 ≤ z ≤ 2**.  
- Justification: This redshift range directly probes the model’s late-time “personality” while anchored by observations.

**2.2 Luminosity Distance d_L(z)**  
- Condition: Residuals against Pantheon+ SN Ia dataset must yield χ² per degree of freedom within **10%** of ΛCDM best-fit.

---

## 3. Structure Formation

**3.1 Growth Rate fσ₈(z)**  
- Condition: Predictions must lie within the 1σ envelopes of current RSD (redshift-space distortion) measurements over **0 ≤ z ≤ 1**.  
- Justification: Modified expansion rates directly affect structure growth.

---

## 4. Internal Consistency

**4.1 Recoverability of ΛCDM**  
- Any α(t) form must have a parameter limit that **exactly** reproduces ΛCDM H(z) over all z.  
- Ensures that the model is a superset rather than an unrelated theory.

**4.2 Parameter Transparency**  
- α(t) must be defined by a finite, explicit set of parameters — no hidden time dependence or curve fitting to the data post-hoc.  
- Prevents “cheating” via unconstrained functional freedom.

---

## 5. Pass/Fail Definition

The model is **falsified** if:  
- It fails **any** of the early-universe criteria (BBN, CMB), **or**  
- It fails **two or more** of the late-universe tests at the defined thresholds.

The model is **provisionally viable** if:  
- It passes all early-universe tests, and  
- It passes at least **three out of four** late-universe tests within the stated limits.

---

## 6. Testing Protocol

1. Choose α(t) form and parameters **before** comparing to data.  
2. Compute H(z), d_L(z), r_s, D_A, fσ₈(z) using standard cosmology code (e.g., CLASS, CAMB).  
3. Compare directly to ΛCDM best-fit observational benchmarks.  
4. Record χ² and residuals for transparency.  
5. Archive all results and code in repository for reproducibility.
