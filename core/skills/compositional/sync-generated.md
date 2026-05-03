---
id: skill.compositional.sync-generated
kind: skill
scope: compositional
category: workflow
domain: sync-generated
summary: Regenerate and validate derived files, schemas, clients, lockfiles, and snapshots.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.tool.validation
  - rule.atomic.source-code
optional_tools: []
---

# Sync Generated

Use project discovery to identify generated files, source inputs, generator
commands, manifests, lockfiles, snapshots, and freshness validation.

Regenerate derived output through the intended generator or package manager.
Do not hand-author generated files unless the repository explicitly documents
that workflow.

Keep generated-output changes tied to the source inputs or generator changes
that caused them. If generated output changes unexpectedly, inspect the
generator version, environment, ordering, and source data before accepting it.

Run freshness validation when available. Report generators run, source inputs,
generated outputs changed, validation performed, and any unexplained churn.
