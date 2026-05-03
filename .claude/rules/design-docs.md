---
paths:
  - "docs/**/*.md"
---

# Design Documentation Rules

Keep design intent, review findings, and implementation plans separate.

When editing documentation:

- Preserve vendor neutrality unless the document explicitly scopes itself to one
  vendor.
- Prefer generic source-code, language, toolchain, and package-management
  concepts over one ecosystem's terminology.
- Record unresolved design choices as open questions.
- Keep vendor-specific adaptation mechanics separate from canonical policy.
- Avoid duplicating long policy sections already covered by `AGENTS.md` or
  `docs/design-intent.md`.
