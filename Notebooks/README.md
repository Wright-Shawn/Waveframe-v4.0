# Notebooks — Waveframe V4.0

This folder contains Jupyter notebooks used for core computational analysis, model validation, and comparison to observational data in the Waveframe V4.0 project.

---

## Quickstart (recommended entry point)

### `00_quickstart.ipynb`
**Purpose:**  
- A lightweight viewer/plotter for CSV results in `Analysis/`.  
- Automatically detects common observables (`E(z)`, `D_A(z)`, `H(z)`, `fσ₈(z)`) and plots them.  
- Intended as the **first notebook to run** for reviewers or new users.  

**Dependencies:**  
- `requirements.txt` (root of repo)  
- CSVs in `Analysis/`

**Outputs:**  
- Interactive plots (optionally saves them under `Figures/auto/`)

---

## Core Analysis Notebooks

### 1. `compare_to_LCDM.ipynb`
**Purpose:**  
- Compares Waveframe V4.0 expansion history `H(z)` to ΛCDM for given α(t) parameterizations.  
- Plots relative differences and computes χ² for observational datasets (SN Ia, BAO).

**Dependencies:**  
- `equations/hubble_entropy_growth.py`  
- Observational datasets from `Analysis/`

**Outputs:**  
- Hubble comparison plots  
- χ² statistics

---

### 2. `falsifiability_tests.ipynb`
**Purpose:**  
- Implements the full falsifiability criteria defined in `docs/Falsifiability.md`.  
- Automates pass/fail checks for early-universe constraints, distance–redshift fits, structure growth, parameter economy, and unique predictions.

**Dependencies:**  
- `equations/*`  
- Observational datasets from `Analysis/`

**Outputs:**  
- Pass/fail status report  
- Log file of criteria results

---

### 3. `structure_growth_fsigma8.ipynb`
**Purpose:**  
- Integrates the linear growth equation for density perturbations using Waveframe’s `H(z)`.  
- Computes `fσ₈(z)` and compares to redshift-space distortion (RSD) measurements.

**Dependencies:**  
- `equations/structure_growth.py`  
- RSD datasets from `Analysis/`

**Outputs:**  
- Growth rate overlay plots  
- Growth index values

---

### 4. `hubble_distance_modulus.ipynb`
**Purpose:**  
- Calculates luminosity distance `D_L(z)` and distance modulus `μ(z)` from Waveframe `H(z)`.  
- Fits to Pantheon+ SN Ia dataset.

**Dependencies:**  
- `equations/hubble_entropy_growth.py`  
- Pantheon+ data from `Analysis/`

**Outputs:**  
- Distance modulus overlay plots  
- Fit residuals

---

## Usage Notes
- All notebooks assume Python 3.10+ with `numpy`, `scipy`, `matplotlib`, and `pandas` installed.  
- Run notebooks from the repository root to ensure relative paths to `equations/` and `Analysis/` work correctly.  
- For reproducibility, outputs are stored in `Analysis/` when applicable.  
