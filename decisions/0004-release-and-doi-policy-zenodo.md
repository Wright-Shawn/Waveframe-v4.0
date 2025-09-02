# ADR 0004: Release & DOI Policy — Zenodo Archival with Concept + Version DOIs

- **Status:** Accepted
- **Date:** 2025-08-24
- **Context**
  Releases must be citable and immutable. First attempt used a pre-release flag; Zenodo did not mint a DOI. Need a strict, repeatable policy.

- **Decision**
  - Publish only **full releases** (no pre-release) on the default branch.
  - Zenodo integration ON; each release mints a **Version DOI** and rolls up to a **Concept DOI**.
  - Keep tags immutable; bumps use semver (e.g., `v4.0.1`).

- **Options Considered**
  - Ad-hoc tags without archival
  - **GitHub Release + Zenodo (chosen)**
  - Self-hosted archival

- **Consequences**
  - Public, permanent records: reproducibility + audit trail.
  - README shows **Concept DOI**; releases and `CITATION.cff` include **Version DOI**.
  - Document failures (e.g., pre-release issue) in the workflow log.

- **Related Artifacts**
  - `/CITATION.cff` (DOI fields)
  - `/README.md` (DOI badge)
  - `/WORKFLOW_LOG.md` (failure → fix)

- **Future Considerations**
  Automate a release checklist to prevent pre-release mistakes.
