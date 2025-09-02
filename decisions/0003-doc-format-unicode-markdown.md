# ADR 0003: Documentation Format — Unicode Markdown over LaTeX

- **Status:** Accepted
- **Date:** 2025-08-17
- **Context**
  LaTeX is standard in physics, but recruiters and non-academics live on GitHub. Rendering, diffability, and accessibility beat typesetting polish for this POC.

- **Decision**
  Author core docs in **Unicode Markdown** (GitHub-native), reserving LaTeX only when strictly necessary for equations/papers.

- **Options Considered**
  - LaTeX-first (academic norm)
  - **Markdown-first (chosen)** with optional LaTeX appendices

- **Consequences**
  - Faster review, better diffs, instant rendering on GitHub.
  - Figures stored as dated PNG/SVG under `/figures/` for visual audit.
  - If a formal paper is produced, export/port selectively to LaTeX.

- **Related Artifacts**
  - `/README.md`
  - `/figures/` (date-stamped files)
  - `/WORKFLOW_LOG.md`

- **Future Considerations**
  Add a conversion workflow (Pandoc) if LaTeX publication becomes necessary.
