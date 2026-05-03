---
id: skill.compositional.perf-check
kind: skill
scope: compositional
category: workflow
domain: perf-check
summary: Run benchmarks or profiling and compare results against a meaningful baseline.
depends_on:
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.compositional.build
  - skill.compositional.test
  - rule.atomic.source-code
optional_tools: []
---

# Perf Check

Use project discovery to identify benchmarks, profiling commands, load tests,
performance budgets, CI perf checks, and existing baselines.

Prefer repository-defined benchmark or profiling commands over invented
measurements.

Compare results against a meaningful baseline whenever possible. Account for
warmup, sample size, machine variance, external services, caches, and generated
artifact changes before drawing conclusions.

Report the command used, baseline source, result summary, variance or confidence
limits, suspected cause of regressions, and any environment limitation.
