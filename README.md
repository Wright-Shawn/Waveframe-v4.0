# Waveframe v4.0: AI-Orchestrated Proof of Concept in Cosmology

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16872200.svg)](https://doi.org/10.5281/zenodo.16872200)
![CI](https://img.shields.io/github/actions/workflow/status/Wright-Shawn/Waveframe-v4.0/ci.yml?branch=main)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](./LICENSE)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey.svg)](./LICENSE-NC.md)
[![CITATION.cff](https://img.shields.io/badge/cite-CITATION.cff-brightgreen.svg)](./CITATION.cff)
![Last Commit](https://img.shields.io/github/last-commit/Wright-Shawn/Waveframe-v4.0/main)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0006--6043--9295-green.svg)](https://orcid.org/0009-0006-6043-9295)

---

## What This Is

Waveframe v4.0 is a self-directed research project using **AI-assisted workflow design** to build a falsifiable cosmological framework.  
The aim is not to replace ΛCDM, but to demonstrate how **multi-threaded AI collaboration + human orchestration** can produce explicit models, derivations, and predictions in a reproducible way.

<p align="center">
  <img src="Figures/Ez_Hz_H0.png" alt="Expansion history comparison: ΛCDM vs Waveframe" width="600"/>
</p>

*Figure: Expansion history E(z) = H(z)/H₀ compared between ΛCDM and several Waveframe parameterizations.*

---

## Skills Demonstrated

- **Parallel AI Thread Management** — derivations, predictions, and documentation streams  
- **Human-in-the-Loop Validation** — refining AI outputs for accuracy and coherence  
- **Numerical Modeling & Analysis** — comparing Waveframe predictions to ΛCDM  
- **Reproducibility & Documentation** — version-controlled, auditable repository  

---

## Overview of the Model

Waveframe v4.0 replaces metric-first assumptions with an **entropy–action, observer-driven expansion law**.  
The project was developed through iterative inputs, critiques, and synthesis — managed like parallel R&D streams — and packaged into an explicit, testable framework.

**Core Tenets**:
1. **Observer-defined horizons** replace a single global geometry  
2. **Spacetime is emergent** rather than fundamental  
3. **Entropy = Horizon Area**, S(t) = π / [H(t)]²  
4. **Expansion emerges** from resolution-dependent information intake, H(t) ∝ 1 / √(t − t₀)  
5. **Field equations → Information-action principle**  
6. **Metric tensor → Entropic structure** tied to causal boundaries  

---

## Research Goals

- Show that an AI-orchestrated workflow can produce a coherent cosmological framework  
- Derive cosmological observables from an entropy-first, observer-limited perspective  
- Recover ΛCDM behaviors in the correct limits  
- Predict measurable deviations in CMB, BAO, and structure growth  
- Package results in a transparent, reproducible repository  

---

## Falsifiability Criteria

Key pass/fail checks:  

1. **BBN Constraints** – Match ΛCDM within ≈5% for T ~ 0.1–10 MeV  
2. **CMB Acoustic Peaks** – Reproduce ΛCDM sound horizon & angular diameter distance at z ~ 1100  
3. **Distance–Redshift Relation** – Fit SN Ia and BAO data within uncertainties  
4. **Growth of Structure** – Keep fσ₈(z) consistent with RSD and weak lensing  
5. **Limit-Case Recovery** – Reduce to ΛCDM and earlier Waveframe models  
6. **Unique Predictions** – At least one measurable deviation not degenerate with dark-energy models  

Failure under best-fit parameters = falsification.

---

## Deliverables in This Repository

- `/Theory` – Conceptual framework and derivations  
- `/Equations` – Final equations with assumptions and constraints  
- `/Notebooks` – Python analysis scripts for model-vs-ΛCDM comparisons  
- `/Analysis` – Results summaries, comparisons, figures, CSV outputs  
- `/Figures` – Generated plots (E(z), D_A(z), growth factor)  
- `/Docs` – Supporting documentation (framework, falsifiability, workflow log, version history)  
- `/Demos` – Streamlit app, report generator, and pipeline templates  
- Licensing & attribution documents  

---

## Method Limitations

- All calculations are custom; no CAMB/CLASS solvers yet  
- CMB/BAO predictions are distance-only proxies  
- The model is not a replacement for ΛCDM, but a **workflow demonstration**  

---

## Demos

Lightweight demos illustrate how the workflow can be extended:

- `streamlit_app.py` — interactive dashboard plotting entropy vs. redshift  
- `report_generator.py` — converts analysis CSVs into a formatted report  
- `pipelines/langflow_waveframe_template.json` — orchestration starter template  

Run locally:  
```bash
pip install -r Demos/requirements.txt
streamlit run Demos/streamlit_app.py
```

---

## Related Works

- Wright, S.C. (2025). *Waveframe v3.1: Entropic Cosmology with Observer Horizons* (Zenodo: doi.org/10.5281/zenodo.16800001).  
- Wright, S.C. (2025). *Waveframe v2.0: Horizon-Limited Entropic Geometry* (Zenodo: doi.org/10.5281/zenodo.16700001).  
- Tegmark, M. (2014). *Our Mathematical Universe*.  
- Verlinde, E. (2011). *On the Origin of Gravity and the Laws of Newton*.  
- Bousso, R. (2002). *The Holographic Principle*.  
- Susskind, L. (1995). *The World as a Hologram*.  
- Barrow, J.D. (1988). *The World Within the World*.  

---

## Licensing & Attribution

- **Code**: Apache License 2.0 (`LICENSE`)  
- **Theory, equations, figures, docs**: CC BY-NC 4.0 (`LICENSE-NC.md`)  

Attribution is required. Commercial use prohibited without permission.  
See `LICENSE_POLICY.md` for scope examples.  

---

## Author

**Shawn C. Wright**  
ORCID: [0009-0006-6043-9295](https://orcid.org/0009-0006-6043-9295)  

---

## Version

Version: Waveframe v4.0  
Repository: [github.com/Wright-Shawn/Waveframe-v4.0](https://github.com/Wright-Shawn/Waveframe-v4.0)  
Last Updated: 2025-08-20 
