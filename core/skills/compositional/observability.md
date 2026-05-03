---
id: skill.compositional.observability
kind: skill
scope: compositional
category: workflow
domain: observability
summary: Add logs, metrics, traces, and alerts without leaking sensitive data.
depends_on:
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.compositional.test
  - rule.atomic.security
  - rule.atomic.source-code
optional_tools: []
---

# Observability

Use project discovery to identify logging, metrics, tracing, alerting,
dashboards, telemetry libraries, privacy constraints, and operational
conventions.

Add observability that helps diagnose meaningful system behavior, user impact,
failure modes, or performance risk. Avoid noisy, redundant, or high-cardinality
signals that will not be acted on.

Do not log secrets, credentials, private data, tokens, or sensitive payloads.
Preserve existing redaction, sampling, retention, and access-control patterns.

Verify with tests, local logs, telemetry assertions, or configuration checks when
available. Report signal names, emitted context, privacy considerations,
validation performed, and any dashboard or alert follow-up.
