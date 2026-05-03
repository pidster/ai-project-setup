---
id: skill.compositional.api-change
kind: skill
scope: compositional
category: workflow
domain: api-change
summary: Change API contracts, schemas, clients, documentation, and compatibility checks.
depends_on:
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.compositional.test
  - skill.compositional.docs-update
  - skill.compositional.sync-generated
  - rule.atomic.source-code
  - rule.atomic.security
optional_tools: []
---

# API Change

Use project discovery to identify API contracts, schemas, clients, generated
artifacts, compatibility tests, documentation, versioning rules, and consumers.

Keep contract changes explicit. Distinguish additive, compatible changes from
breaking changes, behavioral changes, and documentation-only updates.

Update generated clients, schemas, fixtures, examples, and docs through the
intended generators or workflows.

Verify changed contracts with focused tests and broaden when shared clients,
authentication, authorization, validation, serialization, or public behavior are
affected. Report compatibility impact and migration requirements.
