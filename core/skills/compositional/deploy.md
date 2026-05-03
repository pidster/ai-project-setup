---
id: skill.compositional.deploy
kind: skill
scope: compositional
category: workflow
domain: deploy
summary: Run deployment checks or prepare deployment artifacts safely.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.compositional.build
  - skill.compositional.test
  - skill.compositional.release
  - rule.atomic.security
  - rule.atomic.source-code
optional_tools: []
---

# Deploy

Use project discovery to identify deployment documentation, environments,
artifacts, secrets requirements, approvals, infrastructure configuration,
rollback procedures, and deployment validation.

Do not invent deployment commands. Prefer documented repository workflows,
release pipelines, CI jobs, or deployment tooling.

Verify that artifacts, configuration, generated output, environment variables,
permissions, and migrations match the target environment before deployment.

Report the target environment, artifact or revision, checks performed, deployment
status, rollback path, and any missing approval, secret, or environment
dependency.
