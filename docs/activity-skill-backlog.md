# Activity Skill Inventory

This document records the implemented compositional activity skills and the
batching rationale used while building them.

Activity skills should coordinate atomic rules, atomic skills, and concrete tool
skills. They should own sequencing, scope, stop or fail behavior, and reporting.
They should not duplicate detailed recipes owned by atomic or tool skills.

## Initial Batch

These skills cover common day-to-day repository work.

- `pre-commit`: run relevant checks before committing.
- `commit`: inspect diff, stage intentionally, write commit message.
- `test`: select and run relevant tests.
- `coverage`: measure coverage, identify meaningful gaps, avoid vanity coverage.
- `debug`: reproduce, isolate, inspect logs, add focused diagnostics, verify fix.
- `build`: run project build/package checks.
- `audit`: security, dependency, and configuration audit.
- `update-dependencies`: update dependency sets safely, inspect changelogs, run
  checks.
- `ci-fix`: inspect failing CI, reproduce locally where possible, patch.
- `review`: review local or PR diff for correctness, security, tests, and
  maintainability.
- `pr-create`: prepare branch, summary, tests, and risk notes.
- `pr-address-comments`: handle review comments one at a time.

## Additional Implemented Skills

- `lint`: run linters and interpret failures.
- `format`: run formatters safely and limit churn.
- `typecheck`: run static type checks.
- `upgrade-runtime`: upgrade language, runtime, or framework versions.
- `migrate`: structured codebase migration with checkpoints.
- `release`: changelog, versioning, tags, artifacts, and release notes.
- `merge`: update branch, resolve conflicts, run validation.
- `rebase`: safely rebase with conflict handling and validation.
- `deploy`: run deployment checklist or prepare deployment artifacts.
- `rollback`: revert deployment or code changes safely.
- `docs-update`: update docs affected by code, API, or behavior changes.
- `api-change`: modify API contracts, schemas, clients, docs, and compatibility
  checks.
- `data-change`: validate structured data, migrations, fixtures, and generated
  data.
- `db-migration`: create, review, run, and rollback database migrations.
- `service-start`: start local services, health check, ports, and logs.
- `e2e-test`: browser or end-to-end validation.
- `visual-check`: screenshot or browser verification for UI changes.
- `perf-check`: run benchmarks or profiling and compare against baseline.
- `observability`: add logs, metrics, traces, and alerts without leaking secrets.
- `incident-investigation`: gather evidence, timeline, suspected cause, and
  mitigation.
- `scaffold-feature`: create new feature following project patterns.
- `cleanup`: remove dead code, unused dependencies, and stale configs.
- `sync-generated`: regenerate schemas, clients, lockfiles, and snapshots.
- `environment-setup`: install tools and dependencies, then verify local setup.
- `onboard-repo`: inspect repo and generate initial AI-tool guidance.
- `policy-check`: verify repo instructions and rules are coherent and
  non-conflicting.

## Batching Notes

The implementation used batches that proved composition without requiring every
tool ecosystem at once.

Batches:

1. Daily change loop: `pre-commit`, `commit`, `test`, `build`.
2. Quality loop: `review`, `coverage`, `debug`, `ci-fix`.
3. Maintenance loop: `audit`, `update-dependencies`, `cleanup`,
   `sync-generated`.
4. Collaboration loop: `pr-create`, `pr-address-comments`, `merge`, `rebase`.
5. Runtime loop: `service-start`, `e2e-test`, `visual-check`, `perf-check`.
