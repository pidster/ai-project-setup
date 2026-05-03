---
id: skill.tool.validation
kind: skill
scope: atomic
category: tool
domain: validation
tool: python
summary: Run all currently implemented repository validation checks.
depends_on:
  - skill.tool.adapter-validation
  - skill.tool.canonical-validation
  - skill.tool.generated-validation
  - skill.tool.vendor-validation
commands:
  - python3 core/skills/tools/validate_all.py
---

# Validation

Use this skill when a change may affect multiple project boundaries or when a
single command is preferred over running focused validators one at a time.

Run all implemented validators:

```sh
python3 core/skills/tools/validate_all.py
```

The aggregate validator runs focused validation scripts without merging their
responsibilities. Keep domain-specific checks in their own scripts, then add
them to this aggregate runner when they become part of the normal validation
surface.

Do not run `py_compile` or `compileall` as part of normal validation. Direct
execution already catches syntax errors and avoids creating repo-local bytecode
cache artifacts.
