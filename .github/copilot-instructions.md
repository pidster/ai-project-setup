# Copilot Instructions

Follow `AGENTS.md` as the repository's primary instruction source.

This project designs vendor-neutral AI-tool guidance. Preserve this model:

- Canonical rules and skills live in `core/`.
- Vendor capability data lives in `vendors/`.
- Rendering logic and templates live in `adapters/`.
- Generated artifacts live in `dist/`.
- Design rationale lives in `docs/`.

Do not redefine canonical policy in Copilot-specific files. Copilot-specific
content may summarize, compress, or adapt canonical guidance to Copilot's
instruction surface, but policy changes must be made in canonical content first.

Keep language guidance generic by default. Add language-specific extensions only
where a language or ecosystem materially differs. Keep language policy separate
from concrete tool procedure.
