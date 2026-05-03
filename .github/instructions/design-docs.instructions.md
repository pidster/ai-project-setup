---
applyTo: "docs/**/*.md"
---

# Design Documentation Instructions

Design documents should keep intent, review findings, and implementation details
separate.

When editing docs:

- Preserve vendor neutrality unless the document is explicitly about one vendor.
- Prefer generic language and tool models over Rust-specific or JavaScript-specific
  assumptions.
- Call out open questions instead of smoothing over unresolved design choices.
- Keep vendor-specific adaptation separate from canonical policy.
- Do not duplicate long policy sections across multiple documents.
