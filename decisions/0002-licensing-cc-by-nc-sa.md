# ADR 0002: Licensing — CC BY-NC-SA 4.0 for the Proof-of-Concept

- **Status:** Accepted
- **Date:** 2025-08-10
- **Context**
  Need to prevent commercial exploitation of the POC materials while promoting open study and attribution. Considered software-style permissive licenses and copyleft.

- **Decision**
  Use **Creative Commons BY-NC-SA 4.0** for this Waveframe v4.0 repository.

- **Options Considered**
  - Apache 2.0 (permissive, commercial OK)
  - GPLv3 (copyleft, commercial OK)
  - **CC BY-NC-SA 4.0 (chosen)** — non-commercial, share-alike, attribution

- **Consequences**
  - Clear non-commercial terms for the POC.
  - GitHub license detection may show mixed/warning banners; accept the tradeoff and document it.
  - If future code modules are split out, re-evaluate per-repo licensing (e.g., Apache 2.0 for runnable code).

- **Related Artifacts**
  - `/LICENSE` (CC BY-NC-SA 4.0 text)
  - `/README.md#License`
  - `/WORKFLOW_LOG.md` (licensing phase)

- **Future Considerations**
  If parts evolve into reusable software, create a separate **code** repo under Apache 2.0 and link it from this POC.
