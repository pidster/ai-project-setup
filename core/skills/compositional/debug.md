---
id: skill.compositional.debug
kind: skill
scope: compositional
category: workflow
domain: debug
summary: Reproduce, isolate, diagnose, and verify a focused fix.
depends_on:
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.compositional.test
  - rule.atomic.source-code
optional_tools: []
---

# Debug

Start by reproducing the failure or unexpected behavior with the narrowest
available command, input, fixture, log, or scenario.

Isolate the failing surface before patching. Prefer reading code paths,
configuration, recent changes, and existing tests over speculative edits.

Add focused diagnostics only when they materially shorten the investigation.
Remove temporary diagnostics before delivery unless they are intentional
observability improvements.

Verify the fix with the original reproducer and the smallest broader validation
that covers likely regressions. Report commands run, failures observed, root
cause, fix, and remaining risk.
