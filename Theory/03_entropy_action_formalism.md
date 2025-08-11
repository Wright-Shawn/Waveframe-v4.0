# 03 — Entropy-Action Formalism

This section outlines the formal principle underlying Waveframe XR: a replacement for the Einstein-Hilbert action using an entropy-based variational approach. The goal is to define cosmological dynamics not from curvature, but from entropy evolution over observational horizons.

## Motivation

In standard general relativity, the Einstein field equations are derived from the variation of the Einstein-Hilbert action:

𝐒 = ∫ (𝐑 + ℒₘ) √−g d⁴x

Waveframe XR rejects geometry as fundamental, and instead proposes that evolution arises from the minimization (or stationarity) of an information-based action functional. Here, entropy gradients across an observer-defined causal surface drive expansion.

## Definition of the Entropy Action

We define the entropy action 𝒮ᵢₙ𝒻ₒ as:

𝒮ᵢₙ𝒻ₒ = ∫ 𝛾(z) · dS/dt dt

Where:
- S(t) is the entropy, given by S(t) = π / H(t)²
- 𝛾(z) is a redshift-dependent coupling or information-weighting function
- H(t) is the entropy-derived Hubble parameter

This formulation implies that spacetime evolution is governed by the total information intake over time, weighted by 𝛾(z), which modulates sensitivity to entropy change.

## Variational Principle

We postulate the following condition for physical evolution:

δ𝒮ᵢₙ𝒻ₒ = 0

This leads to the equation of motion for entropy flow. In a simplified model, one version of the action density might be:

ℒ = −𝛾(z) · (∂ₜ S)² / S(t)

Then:

𝒮ᵢₙ𝒻ₒ = ∫ ℒ dt = ∫ −𝛾(z) · (∂ₜ S)² / S(t) dt

Taking the variation δ𝒮 = 0 yields the entropy evolution equation, analogous to Euler-Lagrange equations in classical mechanics.

## Entropy and Expansion

Given that S(t) = π / H(t)², it follows that:

∂ₜ S(t) = −2π · Ḣ / H³

Substituting into the action, we can derive the dynamics of H(t) from first principles. The proportional result:

H(t) ∝ 1 / √(t − t₀)

is not assumed, but shown to be a solution under appropriate choices of 𝛾(z), boundary conditions, and entropy continuity constraints.

## Remarks on Units and Normalization

All variables are assumed to be in Planck units unless otherwise specified. The function 𝛾(z) remains under investigation — it may correspond to an observational entropy potential or encode phase transitions (e.g., recombination, dark energy onset).

## Future Work

- Full derivation of the entropy equation of motion from δ𝒮 = 0
- Inclusion of a boundary entropy term analogous to the Gibbons–Hawking–York boundary term
- Comparison to Einstein-Hilbert action in the limit of smooth curvature
- Interpretation of 𝛾(z) as an effective entropy permeability or rendering coefficient

This action principle is not decorative — it is the core dynamical generator of the model. Any success in reproducing ΛCDM or predicting new anomalies must stem from this foundation.

