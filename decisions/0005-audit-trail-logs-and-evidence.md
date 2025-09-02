# ADR 0005: Audit Trail — Logs, ADRs, and Dated Evidence

- **Status:** Accepted
- **Date:** 2025-08-31
- **Context**
  The differentiator is auditability. Reviewers must reconstruct “what happened, when, and why” without explanations in DMs.

- **Decision**
  - Maintain two complementary logs:
    - `WORKFLOW_LOG.md` = chronological actions + lessons learned
    - `decisions/` = rationale for key tradeoffs (this folder)
  - Store visual evidence under `/figures/` with **date-stamped filenames** (e.g., `2025-08-31_hubble-render.png`).
  - Keep `CHANGELOG.md` for version deltas tied to tags.

- **Options Considered**
  - Minimal README only
  - **Logs + ADRs + Figures (chosen)**

- **Consequences**
  - Anyone can audit the project by reading the log, ADRs, and release history.
  - Adds mild overhead; pays off in credibility with recruiters and labs.

- **Related Artifacts**
  - `/WORKFLOW_LOG.md`
  - `/CHANGELOG.md`
  - `/figures/`

- **Future Considerations**
  Add a weekly “Snapshot” section (top of README) linking to the latest figure(s) and the most recent log entry.
