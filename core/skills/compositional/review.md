---
id: skill.compositional.review
kind: skill
scope: compositional
category: workflow
domain: review
summary: Review a local or pull-request diff for correctness, risk, and maintainability.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - rule.atomic.source-code
  - rule.atomic.security
optional_tools: []
---

# Review

Inspect the changed files, surrounding code, tests, configuration, generated
artifacts, and relevant project guidance before forming findings.

Prioritize bugs, behavioral regressions, security issues, missing validation,
missing tests, generated-output drift, and maintainability risks. Do not treat
style preferences as findings unless they affect correctness or project
consistency.

Ground findings in concrete files, commands, inputs, or expected behavior.
Separate confirmed issues from assumptions and open questions.

When no issues are found, say that directly and call out any residual validation
or test coverage gaps.
