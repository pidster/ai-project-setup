---
id: skill.compositional.incident-investigation
kind: skill
scope: compositional
category: workflow
domain: incident-investigation
summary: Gather evidence, timeline, suspected cause, mitigation, and follow-up for an incident.
depends_on:
  - skill.atomic.project-discovery
  - skill.compositional.debug
  - skill.compositional.observability
  - rule.atomic.security
optional_tools: []
---

# Incident Investigation

Start by preserving evidence: reports, alerts, logs, traces, metrics, recent
changes, deployments, configuration, external dependencies, and user impact.

Build a timeline from observable facts. Separate confirmed evidence from
hypotheses, assumptions, and missing data.

Identify suspected cause, contributing factors, blast radius, mitigation,
rollback or recovery options, and follow-up validation. Do not expose secrets or
private user data in notes or artifacts.

Report current status, impact, timeline, evidence, suspected cause, mitigation
taken, validation performed, and recommended follow-up work.
