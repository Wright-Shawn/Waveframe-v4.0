ntropy-Action Derivation — Waveframe V4.0

## 1. Purpose
This document provides the formal derivation of the Waveframe V4.0 expansion law from the observer entropy principles defined in the `theory/` folder.

---

## 2. Starting Axioms (from Theory)
1. **Finite entropy bound** — At any time t, the observer has access to a finite entropy S(t).
2. **Observer horizon** — The accessible entropy is proportional to the area of the observer's informational horizon.
3. **Entropy growth drives expansion** — A positive entropy growth rate (dS/dt > 0) corresponds to an increase in the observable universe's resolution.
4. **Emergent geometry** — The Hubble flow is a measure of entropy acquisition rate, not pre-existing metric expansion.

---

## 3. Horizon Entropy Definition

From the holographic principle applied to an observer horizon:

S(t) = π / [H(t)]²

- **S(t)**: Horizon entropy (natural units, dimensionless).  
- **H(t)**: Observer’s Hubble parameter (s⁻¹ in SI units).  

This relation is proportional to the Bekenstein–Hawking entropy formula for a cosmological horizon, with constants set to unity in natural units (c = G = ħ = k_B = 1).

---

## 4. Information-Action Principle

We postulate that cosmic evolution extremizes an **information-action functional**:

I = ∫ L_info dt  

where L_info is a Lagrangian density describing the rate of change of accessible microstates.

Let:

L_info = f(S) · (dS/dt)

where f(S) encodes the efficiency of converting entropy growth into resolvable spacetime.

---

## 5. Assumption: Constant Average Entropy Acquisition Rate

If the average entropy acquisition rate is constant over long timescales:

dS/dt = α  (α > 0 constant)

From S(t) = π / [H(t)]²:

d/dt [ π / H(t)² ] = α

⇒ -2π H'(t) / [H(t)]³ = α

---

## 6. Solving for H(t)

Rearranging:

H'(t) = - (α / 2π) · [H(t)]³

Separate variables:

∫ H(t)^(-3) dH(t) = - (α / 2π) ∫ dt

⇒ -1 / (2 H(t)²) = - (α / 2π) (t - t₀)

Multiply through:

1 / H(t)² = (α / π) (t - t₀)

---

## 7. Final Form

Taking the square root and inverting:

H(t) = √[ π / (α (t - t₀)) ]

Thus:

H(t) ∝ 1 / √(t − t₀)

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
