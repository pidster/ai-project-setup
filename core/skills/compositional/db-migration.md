---
id: skill.compositional.db-migration
kind: skill
scope: compositional
category: workflow
domain: db-migration
summary: Create, review, validate, and document database migrations and rollback risk.
depends_on:
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.compositional.test
  - skill.compositional.data-change
  - rule.atomic.security
  - rule.atomic.source-code
optional_tools: []
---

# DB Migration

Use project discovery to identify migration tools, schema files, generated
clients, seed data, rollback conventions, local database setup, and CI migration
checks.

Create or modify migrations through the repository's intended migration tooling.
Do not hand-edit generated migration metadata unless the ecosystem requires it.

Review migration safety: ordering, transactional behavior, reversibility,
backfills, data loss, locking, permissions, and compatibility with deployed
application versions.

Verify with migration validation, affected tests, generated clients or schemas,
and rollback checks where available. Report operational risk and any manual
deployment steps.
