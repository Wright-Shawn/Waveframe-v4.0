# Waveframe v4.0: AI-Orchestrated Proof of Concept in Cosmology

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16872200.svg)](https://doi.org/10.5281/zenodo.16872200)

## What This Is (Plain Language)

Waveframe v4.0 is a self-directed research project that uses AI tools, guided by human oversight, to design and test a new cosmology model.
It’s less about proving physics and more about showcasing an AI-assisted research workflow — taking an idea from concept to derivations, implementations, and falsifiable predictions.
All code was generated, refined, and tested using AI, with my role as orchestrator: defining problems, managing multiple workstreams, validating outputs, and producing reproducible results.
The project structure and process mirror modern AI/ML workflows, making it relevant for AI workflow designer and technical documentation roles as well as scientific modeling.

⸻

## Skills Demonstrated

 •	Parallel AI Thread Management — running multiple prompt streams for derivations, predictions, and documentation.

 •	Human-in-the-Loop Validation — refining AI outputs for accuracy and coherence.

 •	Numerical Modeling & Analysis — comparing models to ΛCDM under constraints.

 •	Reproducibility & Documentation — packaging results in a fully version-controlled, traceable GitHub repo.

## Overview

Waveframe v4.0 is a proof-of-concept cosmological framework created through a multi-threaded, AI-assisted research process with continuous human oversight. It replaces the metric-first assumptions of ΛCDM with an entropy–action, observer-driven expansion law, treating observation itself as the generator of spacetime.

This project did not emerge from a single “magic prompt.”
It was built through hundreds of iterative inputs, cross-model critiques, and synthesis steps, managed like parallel R&D streams. The result is a mathematically explicit, falsifiable model — packaged in a structured, version-controlled GitHub repository.

While speculative in physics, the primary purpose of Waveframe v4.0 is to demonstrate AI Workflow Designer skillsets:

 •	Parallel Prompt Orchestration – Managing separate threads for derivations, critiques, predictions, and documentation.

 •	Human-in-the-Loop Validation – Filtering, merging, and refining AI outputs into coherent results.

 •	Numerical Analysis Implementation – Running model-vs-ΛCDM comparisons locally in Python under hardware constraints.

 •	Reproducible Documentation – Delivering clear, traceable methods and results.

⸻

## Why It Matters

Waveframe v4.0 demonstrates how complex, interdisciplinary research can be executed with limited resources by combining:
	•	Well-defined theoretical framing
	•	Modular development structure
	•	Built-in falsifiability criteria
	•	Complete, reproducible outputs

Recruiters and technical reviewers will find:
	•	A working example of AI-human research orchestration from concept to deliverables
	•	End-to-end traceability of methods, inputs, and outputs
	•	Demonstrated ability to manage complexity under constraints

⸻

## Core Tenets

 1.	Observer-defined horizons replace the idea of a single, global geometry.
	•	An observer’s “universe” is bounded by their causal horizon, an information boundary rather than a fixed metric surface.

 2.	Spacetime is emergent, not fundamental.
	•	Matter and geometry arise from quantum collapse events on causal surfaces.

 3.	Entropy = Horizon Area defines the system’s information content:
	•	S(t) = π / [H(t)]², where H(t) is the observer’s Hubble parameter (in s⁻¹).

 4.	Expansion emerges from resolution-dependent information intake:
	•	H(t) ∝ 1 / √(t − t₀), where t₀ is the observer’s reference start time for measurement.

 5.	Field equations are replaced with an information-action principle.
	•	Dynamics follow entropy growth and causal boundary changes instead of curvature.

 6.	The metric tensor is replaced by an entropic structure tied to causal boundaries.

⸻

## Research Goals

 •	Show that an AI-orchestrated workflow can produce a fully-formed cosmological framework, complete with derivations, predictions, and falsifiability criteria.

 •	Derive standard cosmological observables from an entropy-first, observer-limited perspective.

 •	Recover ΛCDM behaviors in stated limits without scalar fields, Λ, or inflation.

 •	Predict measurable deviations in CMB, BAO, and structure growth.

 •	Package the work in a transparent, reproducible repository for technical review.

⸻

## Falsifiability Criteria

Waveframe v4.0 is designed to be testable. The following pass/fail tests are non-negotiable:
	1.	BBN Constraints –
Match ΛCDM within ≈5% for cosmic temperatures 0.1–10 MeV to preserve observed light-element abundances.
	2.	CMB Acoustic Peaks –
Reproduce ΛCDM sound horizon and angular diameter distance at z ≈ 1100 within Planck error margins.
	3.	Distance–Redshift Relation –
Fit SN Ia and BAO data for H(z) and luminosity distance d_L(z) within observational uncertainties.
	4.	Growth of Structure –
Keep fσ₈(z) curves consistent with RSD and weak-lensing surveys.
	5.	Limit-Case Recovery –
Reduce to ΛCDM and prior Waveframe models under stated limits.
	6.	Unique Predictions –
Predict at least one measurable deviation not degenerate with existing dark-energy models.

If these fail under best-fit parameters, the model is considered empirically falsified.

⸻

## Deliverables in This Repository
	•	/theory – Conceptual framework and derivations
	•	/equations – Final equations with assumptions and constraints
	•	/notebooks – Python analysis scripts for model-vs-ΛCDM comparisons
	•	/analysis – Results summaries, side-by-side comparisons, figures, and CSV outputs
	•	/figures – Plots for E(z), D_A(z), and growth factor
	•	Licensing & attribution documents

⸻

## Method Limitations
	•	All calculations were run locally, without CAMB/CLASS or external datasets.
	•	CMB and BAO predictions are distance-only proxies; a full treatment would require Boltzmann solver integration.
	•	This work is not a replacement for ΛCDM, but a demonstration of AI-assisted scientific workflow execution.

⸻

# README Additions/Edits (Drop‑In)

## New section: Orchestration (add after Overview)
**Orchestration (AI‑Assisted Development).**  
Waveframe v4.0 was built via parallel prompt streams, targeted critiques, and human gating. The raw process is documented in `ORCHESTRATION.md`, with source dialogue and a chronological workflow in `docs/`. The skill demonstrated here is **AI Workflow Design**: turning ambiguous research goals into auditable artifacts.

## New section: Demos (applied, business‑style)
See `demos/` for transferable examples:
- `streamlit_app.py` — interactive dashboard (entropy vs. redshift; swap in your own CSV).  
- `report_generator.py` — converts a CSV of results into a short, human‑readable report.  
- `pipelines/langflow_waveframe_template.json` — a starter graph for a no‑code pipeline.

Run Streamlit demo locally:
```bash
pip install -r demos/requirements.txt
streamlit run demos/streamlit_app.py
```

## New section: Planned No‑Code Work
We’re extending core workflows to:
- **Streamlit** for interactive apps and dashboards.
- **Langflow/Flowise** for drag‑and‑drop orchestration of data → model → report.

These show that the orchestration method generalizes beyond cosmology into **applied analytics** and **report automation**.


## Licensing & Attribution
	•	Apache License 2.0 – For code and software artifacts
	•	Creative Commons BY-NC 4.0 – For theoretical content, documentation, and figures
Attribution is required; commercial use or resale prohibited without permission.
Code is under Apache-2.0 (see LICENSE).
Docs/figures/theory are under CC BY-NC-SA 4.0 (see LICENSE-NC.md).
See LICENSE_POLICY.md for scope examples.
⸻

## Author

- **Shawn C. Wright**  
  ORCID: [0009-0006-6043-9295](https://orcid.org/0009-0006-6043-9295)


## Version
 
Version: Waveframe v4.0
Repository: github.com/Wright-Shawn/Waveframe-v4.0
Last Updated: 2025-08-13
