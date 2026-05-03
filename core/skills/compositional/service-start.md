---
id: skill.compositional.service-start
kind: skill
scope: compositional
category: workflow
domain: service-start
summary: Start local services, verify health, and report ports and logs.
depends_on:
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - rule.atomic.source-code
optional_tools: []
---

# Service Start

Use project discovery to identify service manifests, start commands,
environment requirements, ports, logs, health checks, and dependent services.

Prefer repository-defined service scripts, compose files, process managers, or
documented development commands over ad hoc command construction.

Start only the services needed for the requested workflow. Preserve existing
running services unless the user asks to restart them or the project workflow
requires it.

Verify readiness with the narrowest health check available. Report commands run,
service URLs or ports, log locations, readiness status, and any missing
environment or dependency.
