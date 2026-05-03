---
id: rule.atomic.security
kind: rule
scope: atomic
category: policy
domain: security
summary: Security invariants for code, configuration, and generated artifacts.
depends_on:
  - rule.atomic.source-code
---

# Security

Do not introduce secrets, credentials, private keys, or tokens into committed
files.

Do not weaken authentication, authorization, validation, escaping, or transport
security without explicit approval and documented rationale.

Treat generated scripts, hooks, plugins, and tool integrations as executable
security surfaces.
