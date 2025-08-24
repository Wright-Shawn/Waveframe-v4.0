# Empirical Predictions

This document defines how Waveframe v4.0 is tested against observations, with **explicit targets, notebooks, and figures**. If we miss the targets under any reasonable parameterization, that configuration is **ruled out**.

> Related context: falsifiability criteria in the main README.

---

## 1) Observables & Targets

| Observable | Definition | Range | Target vs ΛCDM | Dataset | Notebook | Figure | Status |
|---|---|---|---:|---|---|---|---|
| SN Ia distance modulus μ(z) | μ = 5 log10[D_L(z)/10 pc] | z∈[0,1.5] | ≤ 0.03 mag RMS | Pantheon+, DES | `Notebooks/sn_distance_modulus.ipynb` | `Figures/sn_residuals.png` | ☐ Pending |
| Expansion E(z) | E(z)=H(z)/H₀ | z∈[0,2] | ≤ 3% | BAO, cosmic chronometers | `Notebooks/hubble_Ez_compare.ipynb` | `Figures/Ez_comparison.png` | ☐ Pending |
| Growth fσ₈(z) | f=d ln D/d ln a; observable fσ₈ | z∈[0,1] | −2% … +4% | RSD (BOSS/eBOSS, DES) | `Notebooks/growth_fsigma8.ipynb` | `Figures/fs8_tracks.png` | ☐ Pending |
| CMB θ\* | acoustic scale at recombination | z≈1100 | ≤ 0.3% | Planck 2018 | `Notebooks/cmb_theta_star.ipynb` | `Figures/theta_star.png` | ☐ Pending |
| D_A(z\*) | angular diameter distance to recombination | z≈1100 | ≤ 1% | Planck 2018 | `Notebooks/cmb_distances.ipynb` | `Figures/DA_recomb.png` | ☐ Pending |

**Pass/Fail:** a row is *Pass* when the best-fit Waveframe track sits fully inside the tolerance band across the stated range (or within 1σ of the dataset’s reported uncertainty, whichever is tighter).

---

## 2) Minimal Modeling Stack

- **Background:** compute Waveframe’s H(z) from your entropy–action law (README: S(t)=π/H², H(t) ∝ 1/√(t−t₀)), then map to z via 1+z=a₀/a. Produce E(z) and integrals for distances.  
- **Distances:**  
  - \( D_C(z) = c \int_0^z \frac{dz'}{H(z')} \),  
  - \( D_L(z) = (1+z) D_C(z) \),  
  - \( \mu(z) = 5\log_{10}[D_L(z)/10\,\text{pc}] \).  
- **Growth:** integrate the linear growth ODE using your background H(z) and effective \(\Omega_m(z)\) (ΛCDM-limit check included).  
- **CMB scales (distance-only first pass):** compute \( D_A(z_\*) \) and \(\theta_\* = r_s(z_\*)/D_A(z_\*)\) with a proxy \(r_s\) (flagged as an approximation until a full Boltzmann run).

---

## 3) Fitting & Uncertainty

- **SN Ia:** χ² on μ(z) with covariance (start diagonal if needed, then upgrade).  
- **BAO/CC:** χ² on E(z) points (BAO-derived H/H₀ or H(z) chronometers).  
- **RSD:** χ² on fσ₈(z).  
- **CMB (distance-only):** require \(|\Delta \theta_\*| \le 0.3\%\) and \(|\Delta D_A(z_\*)| \le 1\%\).  

**Procedure:** grid search or MCMC over Waveframe parameters; record best-fit, χ²/dof, AIC/BIC. Save JSON of best-fit params in `Analysis/best_fit.json`.

---

## 4) Reproducibility Contract

- **Inputs:** small CSV extracts in `Analysis/inputs/` (or fetch scripts with hashes).  
- **Run:**  
  - `python Notebooks/sn_distance_modulus.ipynb` (papermill/nbconvert)  
  - `python Notebooks/hubble_Ez_compare.ipynb`  
  - `python Notebooks/growth_fsigma8.ipynb`  
  - `python Notebooks/cmb_theta_star.ipynb`  
- **Outputs:** figures emitted to `Figures/` and a one-page summary `Analysis/predictions_summary.md`.  
- **CI:** a CPU-only job runs the background + SN/BAO checks and uploads `Figures/` as artifacts.

---

## 5) ΛCDM Limit Checks (Sanity)

- Waveframe parameters admit a subspace that reduces to ΛCDM behavior.  
- Tests:
  1. \(E(z)\) matches ΛCDM within ≤0.5% across z∈[0,2].  
  2. Growth ODE returns the standard growth when in the ΛCDM subspace.  
  3. Distances and \(\theta_\*\) converge to Planck-like values within stated tolerances.

Add unit tests in `tests/test_limits.py`.

---

## 6) Status Tracker

- [ ] SN Ia μ(z) residuals plotted, RMS computed  
- [ ] E(z) comparison figure + χ²/DoF  
- [ ] fσ₈(z) tracks + envelope  
- [ ] CMB distance proxies  
- [ ] ΛCDM-limit unit tests green  
- [ ] `Analysis/predictions_summary.md` generated  
- [ ] CI artifact: `Figures/` uploaded

---

## 7) Notes & Caveats

- CMB items are **distance proxies** until a Boltzmann solver is integrated.  
- Growth uses linear theory; non-linear corrections are out of scope for v4.0.  
- Tolerances are **commitments**; missing them constitutes **falsification** for that parameterization.
