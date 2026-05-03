---
id: skill.compositional.docs-update
kind: skill
scope: compositional
category: workflow
domain: docs-update
summary: Update documentation affected by code, API, behavior, or workflow changes.
depends_on:
  - skill.atomic.project-discovery
  - skill.compositional.review
  - rule.atomic.source-code
optional_tools: []
---

# Docs Update

Use project discovery to identify documentation ownership, scoped documentation
instructions, generated docs, public API references, examples, and release or
workflow notes affected by the change.

Update documentation that describes behavior, configuration, commands, public
interfaces, generated outputs, or operational workflows changed by the work.

Keep design intent, review findings, implementation plans, and vendor-specific
adaptation mechanics separate when the repository has those boundaries.

Do not duplicate long policy sections across documents. Prefer links, source
references, or concise summaries when canonical content already owns the policy.
