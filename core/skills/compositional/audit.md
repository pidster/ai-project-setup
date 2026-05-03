---
id: skill.compositional.audit
kind: skill
scope: compositional
category: workflow
domain: audit
summary: Audit security, dependency, and configuration risk.
depends_on:
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - rule.atomic.security
  - rule.atomic.source-code
optional_tools: []
---

# Audit

Use project discovery to identify dependency manifests, lockfiles, security
configuration, CI checks, generated artifacts, and repository-defined audit
commands.

Prefer existing repository audit, dependency, and configuration checks over
generic commands.

Inspect results for actionable risk. Separate known vulnerabilities,
misconfiguration, stale generated output, unsupported dependencies, and policy
drift from informational noise.

Do not suppress, ignore, or downgrade audit findings without explicit rationale.
Report the command used, finding severity, affected surface, recommended fix,
and any unresolved external dependency or vendor risk.
