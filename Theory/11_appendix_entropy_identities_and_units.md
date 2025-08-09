# Appendix: Entropy Identities and Units

## 1. Purpose
This appendix collects the key entropy-related identities used in Waveframe V4.0 (XR), along with units and conversion factors.  
It serves as a reference for derivations in the theory folder.

---

## 2. Fundamental Relations

### 2.1 Horizon Entropy
S(t) = π ÷ H(t)²  
- **S(t)**: Horizon entropy (dimensionless in natural units).  
- **H(t)**: Observer’s Hubble parameter (s⁻¹ in SI units).  

### 2.2 Entropy-Rendering Relation
H(t) ∝ 1 ÷ √(t − t₀)  
- Links entropy growth to the statistical acquisition of resolved states.  
- t₀ is the observer’s initial reference time.

### 2.3 Entropy and Information
S = k_B ln(Ω)  
- **k_B**: Boltzmann constant (1.380649 × 10⁻²³ J/K).  
- **Ω**: Number of accessible microstates.

---

## 3. Derived Quantities

### 3.1 Entropy Rate
dS/dt = -2π ÷ H³ · (dH/dt)  
- In natural units (c = G = ħ = k_B = 1), S is dimensionless.

### 3.2 Effective Horizon Radius
R_H = c ÷ H  
- **c**: Speed of light (2.99792458 × 10⁸ m/s).  
- Converts H(t) to a physical length scale.

### 3.3 Area Relation
A_H = 4π R_H²  
- **A_H**: Horizon area (m² in SI units).  
- Links to entropy via holographic principle: S ∝ A_H.

---

## 4. Units Summary

| Quantity | Symbol | SI Units | Natural Units |
|----------|--------|----------|---------------|
| Entropy | S | J/K | Dimensionless |
| Hubble Parameter | H | s⁻¹ | s⁻¹ |
| Horizon Radius | R_H | m | 1/E |
| Horizon Area | A_H | m² | 1/E² |
| Time | t | s | s |
| Boltzmann Constant | k_B | J/K | 1 |

---

## 5. Notes on Conventions
- Unless otherwise stated, XR uses **natural units** with c = G = ħ = k_B = 1.
- All entropy values are **per observer horizon** — no global entropy is assumed.
- Conversion to SI units is only required when interfacing with empirical datasets.

---

## 6. Forward References
- For formalism using these identities, see `03_entropy_action_formalism.md`.
- For predictions derived from S(t), see `06_cosmological_predictions_and_falsifiability.md`.
