---
id: skill.compositional.ci-fix
kind: skill
scope: compositional
category: workflow
domain: ci-fix
summary: Inspect failing CI, reproduce locally where possible, patch, and verify.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.compositional.debug
  - skill.compositional.test
  - rule.atomic.source-code
optional_tools: []
---

# CI Fix

Inspect failing jobs, failing commands, logs, changed files, and relevant CI
configuration before editing code.

Reproduce locally when the required tooling, services, credentials, and runtime
conditions are available. If local reproduction is not practical, preserve the
CI evidence and state the limitation.

Patch the underlying issue rather than weakening CI, tests, validation, typing,
security checks, or timeouts to make the failure disappear.

Verify with the closest local command and any broader validation justified by
the failure surface. Report the CI failure, reproduction status, fix, validation
performed, and any remaining CI-only risk.
