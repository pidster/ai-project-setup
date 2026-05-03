---
id: skill.compositional.format
kind: skill
scope: compositional
category: workflow
domain: format
summary: Run formatters safely and limit formatting churn.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - rule.atomic.source-code
optional_tools: []
---

# Format

Use project discovery to identify formatter commands, configuration files,
language ecosystems, generated files, and CI formatting checks.

Prefer repository-defined formatting commands over generic formatter invocations.

Limit formatting to files affected by the requested change when the formatter
and project workflow support that safely. Broaden only when project conventions
or tooling require it.

Do not mix broad formatting churn with behavioral changes unless explicitly
requested. Report the formatter command used, scope formatted, and any unrelated
formatting changes left untouched.
