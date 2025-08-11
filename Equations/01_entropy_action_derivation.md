# Entropy-Action Derivation — Waveframe V4.0

## 1. Purpose
This document provides the formal derivation of the Waveframe V4.0 expansion law from the observer entropy principles defined in the `theory/` folder.
Each step is tagged as **[Mainstream]**, **[Waveframe Axiom]**, or **[Waveframe Result]** for clarity.

---

## 2. Starting Axioms (from Theory)
1. **[Waveframe Axiom]** — At any time t, the observer has access to a finite entropy S(t).
2. **[Waveframe Axiom]** — The accessible entropy is proportional to the area of the observer's informational horizon.
3. **[Waveframe Axiom]** — A positive entropy growth rate (dS/dt > 0) corresponds to an increase in the observable universe's resolution.
4. **[Waveframe Axiom]** — The Hubble flow is a measure of entropy acquisition rate, not pre-existing metric expansion.

---

## 3. Horizon Entropy Definition

**[Mainstream]** — In de Sitter space, the Bekenstein–Hawking entropy of a cosmological horizon with radius R_H = c / H is:

S ∝ A_H ∝ 1 / H²

**[Waveframe Axiom]** — Extend this proportionality to *any* observer-defined horizon in a general cosmological setting, not just de Sitter space.

Thus:

S(t) = π / [H(t)]²

- **S(t)**: Horizon entropy (natural units, dimensionless).  
- **H(t)**: Observer’s Hubble parameter (s⁻¹ in SI units).  

---

## 4. Information-Action Principle

**[Waveframe Axiom]** — Cosmic evolution extremizes an **information-action functional**:

I = ∫ L_info dt  

where L_info is a Lagrangian density describing the rate of change of accessible microstates.

Let:

L_info = f(S) · (dS/dt)

where f(S) encodes the efficiency of converting entropy growth into resolvable spacetime.

---

## 5. Assumption: Constant Average Entropy Acquisition Rate

**[Waveframe Axiom]** — Assume the average entropy acquisition rate is constant over long timescales:

dS/dt = α  (α > 0 constant)

---

## 6. Derivation of H(t)

From S(t) = π / [H(t)]²:

**[Mainstream]** — Apply derivative rules:

d/dt [ π / H(t)² ] = α

**[Waveframe Result]** — This gives:

-2π H'(t) / [H(t)]³ = α

Rearranging:

H'(t) = - (α / 2π) · [H(t)]³

Separate variables:

∫ H(t)^(-3) dH(t) = - (α / 2π) ∫ dt

Integrate:

-1 / (2 H(t)²) = - (α / 2π) (t - t₀)

Multiply through:

1 / H(t)² = (α / π) (t - t₀)

---

## 7. Final Form

Taking the square root and inverting:

H(t) = √[ π / (α (t - t₀)) ]

Thus:

**[Waveframe Result]** — H(t) ∝ 1 / √(t − t₀)

This is the Waveframe V4.0 expansion law, arising directly from a constant average entropy growth assumption.

---

## 8. Interpretation
- **t₀**: Observer’s initial reference time (when entropy measurement starts).  
- **α**: Effective rate of entropy acquisition (microphysical origin to be determined).  
- The form H(t) ∝ (t − t₀)^(-1/2) is universal for any process with constant average entropy growth in a horizon-bound system.

---

## 9. Forward References
- See `theory/03_entropy_action_formalism.md` for conceptual discussion of the information-action principle.
- See `equations/02_hubble_law_from_entropy_growth.md` for generalizations where dS/dt is not constant.
