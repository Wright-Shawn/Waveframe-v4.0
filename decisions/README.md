# Decisions — Architecture Decision Records (ADRs)

This folder contains **Architecture Decision Records (ADRs)** for Waveframe v4.0.  
Each ADR documents a key tradeoff in the project, making the workflow **transparent and auditable**.

## Purpose
The goal is not only to track *what* was done, but *why* it was done.  
Together with the [Workflow Log](../WORKFLOW_LOG.md) and [Changelog](../CHANGELOG.md), these ADRs form the project’s **audit trail**.

## Format of an ADR
Each ADR follows a simple template:

- **Context** — the problem or choice point  
- **Decision** — what was chosen  
- **Status** — accepted, rejected, or superseded  
- **Consequences** — impacts and tradeoffs  
- **Related Artifacts** — links to logs, figures, or files  

Example:
```markdown
# ADR 000X: Title

- Date: YYYY-MM-DD
- Status: Accepted
- Context: …
- Decision: …
- Consequences: …
- Related Artifacts: …
```

## Existing ADRs
- [0001-project-framing-awo-first.md](0001-project-framing-awo-first.md) — AWO-first framing, physics as case study  
- [0002-licensing-cc-by-nc-sa.md](0002-licensing-cc-by-nc-sa.md) — Licensing strategy  
- [0003-doc-format-unicode-markdown.md](0003-doc-format-unicode-markdown.md) — Documentation format  
- [0004-release-and-doi-policy-zenodo.md](0004-release-and-doi-policy-zenodo.md) — Release & DOI policy  
- [0005-audit-trail-logs-and-evidence.md](0005-audit-trail-logs-and-evidence.md) — Audit trail design  

## Usage
- **Add new ADRs** whenever a significant tradeoff or design choice is made.  
- **Keep status updated** (Accepted / Superseded / Rejected).  
- **Cross-link** ADRs to the workflow log, changelog, or figures when relevant.  

---

By maintaining ADRs, this project demonstrates that **AI-assisted workflows can be reproducible, auditable, and citable** — the core aim of **AI Workflow Orchestration (AWO)**.
