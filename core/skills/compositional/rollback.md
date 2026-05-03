---
id: skill.compositional.rollback
kind: skill
scope: compositional
category: workflow
domain: rollback
summary: Revert deployment or code changes safely with validation.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.compositional.deploy
  - skill.compositional.test
  - rule.atomic.git-safety
  - rule.atomic.security
optional_tools: []
---

# Rollback

Use project discovery to identify rollback procedures, release artifacts,
deployment history, database migrations, configuration changes, feature flags,
and validation commands.

Choose the least risky rollback path for the affected environment: redeploy a
known-good artifact, revert a commit, disable a flag, restore configuration, or
apply a documented database rollback.

Do not discard local or user changes as part of rollback unless explicitly
requested. Treat data and migration rollback as high-risk and preserve evidence
before acting.

Verify restored behavior with health checks, targeted tests, logs, or monitoring
signals. Report rollback target, commands or actions taken, validation
performed, and remaining operational risk.
