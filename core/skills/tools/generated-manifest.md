---
id: skill.tool.generated-manifest
kind: skill
scope: atomic
category: tool
domain: validation
tool: python
summary: Generate and check the generated-output manifest.
depends_on:
  - skill.atomic.project-discovery
commands:
  - python3 core/skills/tools/generated_manifest.py
---

# Generated Manifest

Use this skill when generated vendor outputs are added, removed, or regenerated.

Write the generated-output manifest:

```sh
python3 core/skills/tools/generated_manifest.py
```

Check the manifest without changing files:

```sh
python3 core/skills/tools/generated_manifest.py --check
```

The manifest records generated files, their renderer marker, and canonical source
IDs found in the generated content. This makes generated-output reviews easier
without replacing renderer freshness checks.

Do not run `py_compile` or `compileall` as part of normal validation. Direct
execution already catches syntax errors and avoids creating repo-local bytecode
cache artifacts.
