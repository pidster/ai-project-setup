---
id: skill.compositional.policy-check
kind: skill
scope: compositional
category: workflow
domain: policy-check
summary: Verify repository instructions and rules are coherent and non-conflicting.
depends_on:
  - skill.atomic.project-discovery
  - skill.compositional.review
  - skill.tool.validation
  - rule.atomic.source-code
optional_tools: []
---

# Policy Check

Use project discovery to identify instruction files, canonical rules, skills,
vendor-specific adapters, generated outputs, scoped documentation instructions,
and validation tooling.

Compare guidance for conflicts, duplication, stale generated output, unclear
source-of-truth boundaries, missing dependencies, unsupported vendor mechanics,
and policy stated only in vendor-specific files.

When guidance conflicts, stop and report the discrepancy instead of silently
choosing one source. Preserve canonical boundaries: policy belongs in canonical
content, while vendor files adapt formatting and mechanics.

Run available validation and review uncovered invariants manually. Report
conflicts, missing coverage, validation performed, and recommended corrective
changes.
