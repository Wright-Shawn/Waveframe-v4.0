# Waveframe v4.0: AI-Orchestrated Proof of Concept in Cosmology

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16872200.svg)](https://doi.org/10.5281/zenodo.16872200)
![CI](https://img.shields.io/github/actions/workflow/status/Wright-Shawn/Waveframe-v4.0/ci.yml?branch=main)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](./LICENSE)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey.svg)](./LICENSE-NC.md)
[![CITATION.cff](https://img.shields.io/badge/cite-CITATION.cff-brightgreen.svg)](./CITATION.cff)
![Last Commit](https://img.shields.io/github/last-commit/Wright-Shawn/Waveframe-v4.0/main)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0006--6043--9295-green.svg)](https://orcid.org/0009-0006-6043-9295)


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16872200.svg)](https://doi.org/10.5281/zenodo.16872200)

![CI](https://github.com/Wright-Shawn/Waveframe-v4.0/actions/workflows/ci.yml/badge.svg)

## What This Is (Plain Language)

Waveframe v4.0 is a self-directed research project that uses AI tools, guided by human oversight, to design and test a new cosmology model.  
It’s less about proving physics and more about showcasing an **AI-assisted research workflow** — taking an idea from concept to derivations, implementations, and falsifiable predictions.  

All code was generated, refined, and tested using AI, with my role as orchestrator: defining problems, managing multiple workstreams, validating outputs, and producing reproducible results. The project structure and process mirror modern AI/ML workflows, making it relevant for **AI workflow design**, **technical documentation**, and **scientific modeling**.

---

## Skills Demonstrated

- **Parallel AI Thread Management** — running multiple prompt streams for derivations, predictions, and documentation.  
- **Human-in-the-Loop Validation** — refining AI outputs for accuracy and coherence.  
- **Numerical Modeling & Analysis** — comparing models to ΛCDM under constraints.  
- **Reproducibility & Documentation** — packaging results in a fully version-controlled, traceable GitHub repo.  

---

## Overview

Waveframe v4.0 is a proof-of-concept cosmological framework created through a multi-threaded, AI-assisted research process with continuous human oversight. It replaces the metric-first assumptions of ΛCDM with an entropy–action, observer-driven expansion law, treating observation itself as the generator of spacetime.  

This project did not emerge from a single “magic prompt.”  
It was built through hundreds of iterative inputs, cross-model critiques, and synthesis steps, managed like parallel R&D streams. The result is a mathematically explicit, falsifiable model — packaged in a structured, version-controlled GitHub repository.

While speculative in physics, the primary purpose of Waveframe v4.0 is to demonstrate **AI Workflow Designer skillsets**:

- **Parallel Prompt Orchestration** – Managing separate threads for derivations, critiques, predictions, and documentation.  
- **Human-in-the-Loop Validation** – Filtering, merging, and refining AI outputs into coherent results.  
- **Numerical Analysis Implementation** – Running model-vs-ΛCDM comparisons locally in Python under hardware constraints.  
- **Reproducible Documentation** – Delivering clear, traceable methods and results.  

---

## Orchestration (AI-Assisted Development)

Waveframe v4.0 was built via parallel prompt streams, targeted critiques, and human gating. The raw process is documented in `ORCHESTRATION.md`, with source dialogue and a chronological workflow in `docs/`.  

The skill demonstrated here is **AI Workflow Design**: turning ambiguous research goals into auditable artifacts.

---

## Why It Matters

Waveframe v4.0 demonstrates how complex, interdisciplinary research can be executed with limited resources by combining:  
- Well-defined theoretical framing  
- Modular development structure  
- Built-in falsifiability criteria  
- Complete, reproducible outputs  

**For recruiters and reviewers:**  
- A working example of AI-human research orchestration from concept to deliverables  
- End-to-end traceability of methods, inputs, and outputs  
- Demonstrated ability to manage complexity under constraints  

---

## Core Tenets

1. **Observer-defined horizons** replace the idea of a single, global geometry.  
2. **Spacetime is emergent, not fundamental.**  
3. **Entropy = Horizon Area** defines the system’s information content:  
   - S(t) = π / [H(t)]², where H(t) is the observer’s Hubble parameter (s⁻¹).  
4. **Expansion emerges** from resolution-dependent information intake:  
   - H(t) ∝ 1 / √(t − t₀).  
5. **Field equations → Information-action principle.**  
6. **Metric tensor → Entropic structure** tied to causal boundaries.  

---

## Research Goals

- Show that an AI-orchestrated workflow can produce a fully-formed cosmological framework, complete with derivations, predictions, and falsifiability criteria.  
- Derive standard cosmological observables from an entropy-first, observer-limited perspective.  
- Recover ΛCDM behaviors in stated limits without scalar fields, Λ, or inflation.  
- Predict measurable deviations in CMB, BAO, and structure growth.  
- Package the work in a transparent, reproducible repository for technical review.  

---

## Falsifiability Criteria

Waveframe v4.0 is designed to be testable. The following pass/fail tests are non-negotiable:  

1. **BBN Constraints** – Match ΛCDM within ≈5% for T ~ 0.1–10 MeV.  
2. **CMB Acoustic Peaks** – Reproduce ΛCDM sound horizon & angular diameter distance at z ~ 1100.  
3. **Distance–Redshift Relation** – Fit SN Ia and BAO data within uncertainties.  
4. **Growth of Structure** – Keep fσ₈(z) consistent with RSD and weak lensing.  
5. **Limit-Case Recovery** – Reduce to ΛCDM and earlier Waveframe models.  
6. **Unique Predictions** – At least one measurable deviation not degenerate with dark-energy models.  

If these fail under best-fit parameters, the model is considered falsified.  

---

## Deliverables in This Repository

- `/theory` – Conceptual framework and derivations  
- `/equations` – Final equations with assumptions and constraints  
- `/notebooks` – Python analysis scripts for model-vs-ΛCDM comparisons  
- `/analysis` – Results summaries, comparisons, figures, CSV outputs  
- `/figures` – Plots for E(z), D_A(z), and growth factor  
- Licensing & attribution documents  

---

## Demos

See `/demos` for transferable workflow examples:  

- `streamlit_app.py` — interactive dashboard (entropy vs. redshift).  
- `report_generator.py` — converts CSV results into a human-readable report.  
- `pipelines/langflow_waveframe_template.json` — starter no-code orchestration graph.  

**Run locally:**  
```bash
pip install -r demos/requirements.txt
streamlit run demos/streamlit_app.py
```

---

## Planned No-Code Work

Future extensions will package workflows into:  
- **Streamlit** apps for interactive analytics and visualization.  
- **Langflow/Flowise** pipelines for drag-and-drop orchestration.  

---

## Method Limitations

- All calculations were run locally without CAMB/CLASS or external datasets.  
- CMB/BAO predictions are distance-only proxies (no Boltzmann solver yet).  
- This is not a replacement for ΛCDM but a demonstration of **AI-assisted workflow execution**.  

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
Last Updated: 2025-08-13  
