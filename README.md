# Waveframe v4.0: AI-Orchestrated Proof of Concept in Cosmology

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16872200.svg)](https://doi.org/10.5281/zenodo.16872200)
![CI](https://img.shields.io/github/actions/workflow/status/Wright-Shawn/Waveframe-v4.0/ci.yml?branch=main)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](./LICENSE)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey.svg)](./LICENSE-NC.md)
[![CITATION.cff](https://img.shields.io/badge/cite-CITATION.cff-brightgreen.svg)](./CITATION.cff)
![Last Commit](https://img.shields.io/github/last-commit/Wright-Shawn/Waveframe-v4.0/main)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0006--6043--9295-green.svg)](https://orcid.org/0009-0006-6043-9295)

---

## What This Is (Plain Language)

Waveframe v4.0 is a self-directed research project that uses AI tools, guided by human oversight, to design and test a new cosmological model.  
The focus is not on replacing ΛCDM, but on demonstrating an **AI-assisted research workflow**: from concept → derivations → falsifiable predictions.  

All code was generated and refined with AI, with my role as orchestrator: defining problems, managing multiple workstreams, validating outputs, and producing reproducible results. The repo mirrors modern AI/ML workflows, showing skills in **workflow design, numerical modeling, and transparent documentation**.

## What is this?

Waveframe v4.0 is an observer-driven cosmological framework that replaces metric-first assumptions with an entropy–action expansion law. It is designed to be explicit, falsifiable, and implemented in open, reproducible notebooks.

<p align="center">
  <img src="Figures/Ez_Hz_H0.png" alt="Expansion history comparison: ΛCDM vs Waveframe" width="600"/>
</p>

*Figure: Expansion history E(z) = H(z)/H₀ compared between ΛCDM and several Waveframe parameterizations.*

---

## Skills Demonstrated

- **Parallel AI Thread Management** — derivations, predictions, and documentation streams.  
- **Human-in-the-Loop Validation** — refining AI outputs for accuracy and coherence.  
- **Numerical Modeling & Analysis** — comparing Waveframe predictions to ΛCDM under constraints.  
- **Reproducibility & Documentation** — version-controlled, traceable repository.  

---

## Overview

Waveframe v4.0 is a proof-of-concept cosmological framework created through multi-threaded, AI-assisted research with continuous human oversight. It replaces metric-first assumptions of ΛCDM with an entropy–action, observer-driven expansion law, treating observation itself as the generator of spacetime.  

This project was built through iterative inputs, cross-model critiques, and synthesis steps — managed like parallel R&D streams. The result is a mathematically explicit, falsifiable model packaged in a structured, version-controlled repository.

---

## Orchestration (AI-Assisted Development)

The workflow was built via parallel prompt streams, targeted critiques, and human gating. The raw process is documented in `ORCHESTRATION.md`, with source dialogue and a chronological workflow in `/Docs/`.  

This demonstrates **AI Workflow Design**: turning ambiguous research goals into auditable artifacts.

---

## Core Tenets

1. **Observer-defined horizons** replace the idea of a single, global geometry.  
2. **Spacetime is emergent, not fundamental.**  
3. **Entropy = Horizon Area** defines system information:  
   - S(t) = π / [H(t)]².  
4. **Expansion emerges** from resolution-dependent information intake:  
   - H(t) ∝ 1 / √(t − t₀).  
5. **Field equations → Information-action principle.**  
6. **Metric tensor → Entropic structure** tied to causal boundaries.  

---

## Research Goals

- Show that an AI-orchestrated workflow can produce a coherent cosmological framework.  
- Derive standard cosmological observables from an entropy-first, observer-limited perspective.  
- Recover ΛCDM behaviors in stated limits without scalar fields, Λ, or inflation.  
- Predict measurable deviations in CMB, BAO, and structure growth.  
- Package the work in a transparent, reproducible repository.  

---

## Falsifiability Criteria

Waveframe v4.0 is designed to be testable. Key pass/fail checks:

1. **BBN Constraints** – Match ΛCDM within ≈5% for T ~ 0.1–10 MeV.  
2. **CMB Acoustic Peaks** – Reproduce ΛCDM sound horizon & angular diameter distance at z ~ 1100.  
3. **Distance–Redshift Relation** – Fit SN Ia and BAO data within uncertainties.  
4. **Growth of Structure** – Keep fσ₈(z) consistent with RSD and weak lensing.  
5. **Limit-Case Recovery** – Reduce to ΛCDM and earlier Waveframe models.  
6. **Unique Predictions** – At least one measurable deviation not degenerate with dark-energy models.  

Failure to meet these under best-fit parameters constitutes falsification.

---

## Deliverables in This Repository

- `/Theory` – Conceptual framework and derivations  
- `/Equations` – Final equations with assumptions and constraints  
- `/Notebooks` – Python analysis scripts for model-vs-ΛCDM comparisons  
- `/Analysis` – Results summaries, comparisons, figures, CSV outputs  
- `/Figures` – Plots for E(z), D_A(z), and growth factor  
- `/Docs` – Supporting documentation including theoretical framework, falsifiability criteria, workflow log, version history, and dialogue excerpts  
- `/Demos` – Streamlit app, report generator, sample data, and no-code pipeline templates  
- Licensing & attribution documents  

---

## Method Limitations

- All calculations run locally without CAMB/CLASS or external solvers.  
- CMB/BAO predictions are distance-only proxies (no Boltzmann solver yet).  
- This is not a replacement for ΛCDM, but a demonstration of **AI-assisted workflow execution**.  

---

## Demos

This repository includes lightweight demos to illustrate how the workflow can be extended or visualized:

- `streamlit_app.py` — interactive dashboard plotting entropy vs. redshift.  
- `report_generator.py` — converts analysis CSVs into a formatted report.  
- `pipelines/langflow_waveframe_template.json` — starter orchestration graph.  

**Run locally:**  
```bash
pip install -r Demos/requirements.txt
streamlit run demos/streamlit_app.py

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
