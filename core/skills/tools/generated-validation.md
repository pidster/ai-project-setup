---
id: skill.tool.generated-validation
kind: skill
scope: atomic
category: tool
domain: validation
tool: python
summary: Validate that generated vendor outputs are up to date.
depends_on:
  - skill.atomic.project-discovery
commands:
  - python3 core/skills/tools/generated_validation.py
---

# Generated Validation

Use this skill when canonical content, vendor capability data, or adapter
rendering behavior changes.

Run the deterministic freshness validator:

```sh
python3 core/skills/tools/generated_validation.py
```

The validator runs each implemented renderer in check mode and reports generated
outputs that are missing or stale.

Do not run `py_compile` or `compileall` as part of normal validation. Direct
execution already catches syntax errors and avoids creating repo-local bytecode
cache artifacts.
