# Entropy–Action Derivation — Waveframe V4.0

## 1. Purpose
This document provides the formal derivation of the Waveframe V4.0 expansion law from the observer entropy principles defined in the `theory/` folder.  
Each step is tagged as **[Mainstream]**, **[Waveframe Axiom]**, or **[Waveframe Result]** for clarity.

---

## 2. Starting Axioms (from Theory)
1. **[Waveframe Axiom]** — At any time $t$, the observer has access to a finite entropy $S(t)$.  
2. **[Waveframe Axiom]** — The accessible entropy is proportional to the area of the observer’s informational horizon.  
3. **[Waveframe Axiom]** — A positive entropy growth rate $(dS/dt > 0)$ corresponds to an increase in the observable universe’s resolution.  
4. **[Waveframe Axiom]** — The Hubble flow is treated as an *operational measure* of entropy acquisition rate.  
   - *Falsifiability note*: This implies that deviations from the proportionality $H(t) \propto dS/dt$ would empirically disprove the model.  

---

## 3. Horizon Entropy Definition

**[Mainstream]** — In de Sitter space, the Bekenstein–Hawking entropy of a cosmological horizon with radius $R_H = c/H$ is:  

$$
S \propto A_H \propto \frac{1}{H^2}
$$

**[Waveframe Axiom]** — Extend this proportionality to *any* observer-defined horizon in a general cosmological setting, not just de Sitter space.  

Thus:  

$$
S(t) = \frac{\pi}{H(t)^2}
$$

- $S(t)$: Horizon entropy (natural units, dimensionless).  
- $H(t)$: Observer’s Hubble parameter ($s^{-1}$ in SI units).  

---

## 4. Information–Action Principle

**[Waveframe Axiom]** — Cosmic evolution extremizes an **information–action functional**:  

$$
I = \int L_{\text{info}} \, dt
$$

where $L_{\text{info}}$ is a Lagrangian density describing the rate of change of accessible microstates.  

Define:  

$$
L_{\text{info}} = f(S) \cdot \frac{dS}{dt}
$$

where $f(S)$ encodes the efficiency of converting entropy growth into resolvable spacetime.  

**[Clarification]** — To connect entropy to action, assume a proportionality constant $\kappa$ such that:  

$$
I \propto \int S \,\frac{dS}{dt}\, dt
$$

with $\kappa$ absorbed into the normalization of $I$. This provides the bridge between the entropy–area relation and the entropy–action formalism.  

---

## 5. Definition: Observer Entropy

**[Waveframe Definition]** — *Observer entropy* $S_{\text{obs}}$ is defined as the entropy associated with the informational horizon of a specific observer, proportional to the accessible horizon area:  

$$
S_{\text{obs}}(t) = \frac{\pi}{H(t)^2}
$$

This explicitly grounds “observer entropy” in the same horizon–area formalism as cosmological entropy.  

---

## 6. Assumption: Constant Average Entropy Acquisition Rate

**[Waveframe Axiom]** — Assume the average entropy acquisition rate is constant over long timescales:  

$$
\frac{dS}{dt} = \alpha, \quad \alpha > 0 \;\; \text{constant}
$$

---

## 7. Derivation of $H(t)$

From $S(t) = \pi / H(t)^2$:  

**[Mainstream]** — Apply derivative rules:  

$$
\frac{d}{dt} \left(\frac{\pi}{H(t)^2}\right) = \alpha
$$

**[Waveframe Result]** — Differentiate and rearrange:  

$$
-\frac{2\pi H'(t)}{H(t)^3} = \alpha
$$

$$
H'(t) = - \frac{\alpha}{2\pi} \, [H(t)]^3
$$

Separate variables:  

$$
\int H(t)^{-3} \, dH(t) = -\frac{\alpha}{2\pi} \int dt
$$

Integrate:  

$$
-\frac{1}{2H(t)^2} = -\frac{\alpha}{2\pi} (t - t_0)
$$

Multiply through:  

$$
\frac{1}{H(t)^2} = \frac{\alpha}{\pi} (t - t_0)
$$

---

## 8. Final Form

Taking the square root and inverting:  

$$
H(t) = \sqrt{\frac{\pi}{\alpha (t - t_0)}}
$$

Thus:  

**[Waveframe Result]** —  

$$
H(t) \propto \frac{1}{\sqrt{t - t_0}}
$$

This is the Waveframe V4.0 expansion law, arising directly from a constant average entropy growth assumption.  

---

## 9. Interpretation
- $t_0$: Observer’s initial reference time (when entropy measurement starts).  
- $\alpha$: Effective rate of entropy acquisition (microphysical origin to be determined).  
- The form $H(t) \propto (t - t_0)^{-1/2}$ is universal for any process with constant average entropy growth in a horizon-bound system.  

---

## 10. Forward References
- See `theory/03_entropy_action_formalism.md` for conceptual discussion of the information–action principle.  
- See `equations/02_hubble_law_from_entropy_growth.md` for generalizations where $dS/dt$ is not constant.  

---

### Key Revisions Made
- Clarified **Axiom 4** as falsifiable.  
- Added **missing proportionality justification** in entropy–action formalism.  
- Explicitly defined **observer entropy**.  
- Inserted **intermediate equation** for clarity in expansion law derivation.  
- Promoted key relations to **block equations** for readability.  
