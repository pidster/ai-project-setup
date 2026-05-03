---
id: skill.compositional.data-change
kind: skill
scope: compositional
category: workflow
domain: data-change
summary: Validate structured data, fixtures, migrations, and generated data changes.
depends_on:
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.compositional.test
  - skill.compositional.sync-generated
  - rule.atomic.source-code
optional_tools: []
---

# Data Change

Use project discovery to identify data formats, schemas, fixtures, seeds,
generated data, validation commands, migration rules, and consumers.

Prefer structured parsers, schema validators, and repository-defined data checks
over ad hoc string inspection.

Keep source data, generated data, and migration artifacts distinct. Regenerate
derived data through the intended workflow and inspect unexpected churn.

Verify consumers affected by the data change. Report changed data sets, schema or
format impact, validation performed, generated artifacts, and any migration or
backward-compatibility risk.
