---
id: skill.tool.vendor-validation
kind: skill
scope: atomic
category: tool
domain: validation
tool: python
summary: Validate declarative vendor capability metadata.
depends_on:
  - skill.atomic.project-discovery
commands:
  - python3 core/skills/tools/vendor_validation.py
---

# Vendor Validation

Use this skill when vendor capability files are added, removed, or edited.

Run the deterministic validator:

```sh
python3 core/skills/tools/vendor_validation.py
```

The validator checks vendor capability metadata shape, review metadata,
source-list presence, support flag values, preferred output lists, and obvious
rendering-logic keys that would violate the declarative-data boundary.

This validator does not verify that vendor capability claims are still current.
When changing vendor behavior or capability claims, verify the vendor's current
official documentation separately and record source URLs, review date, and
confidence in the capability file.
