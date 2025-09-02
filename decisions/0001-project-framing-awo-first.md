# ADR 0001: Project Framing — AWO First, Physics as Case Study

- **Status:** Accepted
- **Date:** 2025-07-30
- **Context**
  Waveframe v4.0 could be read as “a physics repo.” That misses the point. The core deliverable is **AI Workflow Orchestration (AWO)**: auditability, reproducibility, artifact discipline. Physics is the stress test, not the product.

- **Decision**
  Frame Waveframe v4.0 explicitly as an **AWO proof-of-concept**. Physics content exists to demonstrate the method under non-trivial conditions.

- **Options Considered**
  1) Physics-first framing (traditional)  
  2) AWO-first framing (chosen)

- **Consequences**
  - README, logs, and structure emphasize workflow artifacts (logs/ADRs/DOIs/licensing) over claims about cosmology.
  - Evaluation focuses on audit trail quality and reproducibility, not only theoretical novelty.

- **Related Artifacts**
  - `/README.md` (Positioning)
  - `/WORKFLOW_LOG.md`
  - `/CHANGELOG.md`

- **Future Considerations**
  If the AWO framing drifts, add a “Why this repo exists” box to README and pin ADR links.
