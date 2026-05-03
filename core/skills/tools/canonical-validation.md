---
id: skill.tool.canonical-validation
kind: skill
scope: atomic
category: tool
domain: validation
tool: python
summary: Validate canonical rule and skill metadata and dependency graph.
depends_on:
  - skill.atomic.project-discovery
commands:
  - python3 core/skills/tools/canonical_validation.py
---

# Canonical Validation

Use this skill when canonical rules or skills are added, removed, or edited.

Run the deterministic validator:

```sh
python3 core/skills/tools/canonical_validation.py
```

The validator checks canonical Markdown frontmatter, stable IDs, dependency
references, dependency cycles, dependency direction, and tool-skill metadata.

When validation fails, report the failing file, the exact invariant, and the
smallest correction that preserves canonical boundaries.
