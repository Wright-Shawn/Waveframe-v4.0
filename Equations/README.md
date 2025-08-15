# Equations Folder — Waveframe v4.0

## Purpose

This folder contains the mathematical derivations and Python scripts for the Waveframe v4.0 cosmology model.
The .md files explain the theory step-by-step, while the .py files implement those equations for testing and visualization.

⸻

## Contents

File	Description

01_entropy_action_derivation.md	Derivation of the entropy–action relationship and master equation for H(t).

entropy_variational_solver.py	Numerical solver for entropy–action field equations.

hubble_entropy_growth.py	Computes H(z) from a chosen α(t) parameterization.

limit_case_LCDM.py	Demonstrates how the model reduces to ΛCDM in special cases.

structure_growth.py	Calculates structure growth factor and fσ₈(z).


⸻

## Usage

 •	Read the .md files for the theory.

 •	Run the .py scripts with Python to generate predictions and plots.

Example:

python limit_case_LCDM.py
