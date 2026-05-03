# Design Intent Review

Review target: `docs/design-intent.md`

## Review 1: Vendor Neutrality

Status: pass with follow-up questions.

The design keeps canonical rules and skills separate from vendor outputs. The
strongest choice is treating the repository as a content compiler, with `core/`
as source and `dist/` as generated output.

Findings:

- The design correctly prevents vendor formats from becoming policy sources.
- The `vendors/` and `adapters/` split is now clearer: vendor capability data is
  declarative, while adapter rendering logic lives separately.
- The policy-drift guardrails are explicit enough to validate later.

Follow-up questions:

- Should vendor overlays be allowed to add vendor-only warnings, or should all
  warnings be canonical caveats with vendor applicability metadata?
- Should generated vendor artifacts be committed, published as release assets,
  or both?

## Review 2: Atomic and Compositional Boundaries

Status: pass with one design pressure to watch.

The design preserves the key rule: compositional skills may call atomic skills,
but atomic skills should not depend on compositional skills. Compositional
skills may depend on other compositional skills when the dependency represents
workflow reuse rather than lower-level tool procedure.

Findings:

- Tool skills are now explicitly atomic through `scope: atomic` and identified
  separately with `category: tool`.
- Compositional workflows own sequencing, scope, failure behavior, and reporting.
- Compositional-to-compositional dependencies are allowed for workflow reuse,
  provided the dependency graph remains acyclic.
- Atomic skills own detailed recipes for one domain or tool.

Design pressure:

- `git-workflow` could become too broad. If it starts defining lifecycle gates,
  it belongs under compositional rules. If it only defines safe Git mechanics, it
  belongs under atomic Git safety.

## Review 3: Language Generality

Status: pass.

The design no longer centers Rust. The generic source-code rule owns broad source
policy, while language-specific rules extend it only when necessary.

Findings:

- `rule.atomic.source-code` is the right default abstraction.
- `rule.language.rust` and similar language files should refine policy, not
  duplicate the generic source-code rule.
- `skill.tool.cargo` is correctly separate from Rust language policy.

Follow-up questions:

- Should language-specific rules live under `core/rules/languages/` or under
  `core/rules/atomic/languages/` to make their atomic scope explicit in the
  path?
- Should language-specific rules be optional examples at first, or required test
  fixtures for the schema and renderer?

## Review 4: Compatibility Across Vendors

Status: partially proven, with initial renderers implemented.

The design identifies three rendering modes: full-fidelity, compact, and hybrid.
Initial renderers now cover Codex, Cursor, and OpenCode, which exercise compact
instruction output, rule-style output, and skill-style output.

Findings:

- The capability-map approach avoids assuming every AI tool supports scoped
  rules or skill invocation.
- Compact rendering is necessary for tools with a small instruction surface.
- Hybrid rendering is realistic for tools that support scoped memories or rules
  but not composable skills.

Remaining risk:

- Vendor capabilities change over time. The project needs a way to mark
  capability maps with source, last-reviewed date, and confidence.

Suggested metadata:

```yaml
vendor: cursor
last_reviewed: 2026-05-02
confidence: provisional
sources: []
```

## Review 5: Validation and Drift Prevention

Status: executable checks implemented for core metadata, vendor metadata,
adapter guardrails, generated-output freshness, and generated-output manifest
freshness.

The validation expectations cover the important graph and metadata invariants.

Findings:

- Dependency direction, unique IDs, missing dependencies, and dependency cycles
  are checked.
- Vendor capability metadata is checked for required declarative fields.
- Generated outputs are checked for freshness and source ID coverage.
- Vendor adapter policy drift remains harder to validate semantically.

Remaining validation additions:

- Require adapter overlays to use an allowlisted schema.
- Add semantic checks or review workflows for adapter policy drift beyond
  mechanical source ID and generated marker checks.

## Review 6: First Milestone

Status: complete.

The first milestone proved the model without attempting every vendor immediately.

Recommended first vendor pair:

- Codex, because it exercises repo instructions, skills, and execution caveats.
- Cursor, because it exercises scoped rules, globs, and rule-style rendering.

Alternative pair:

- Codex and Copilot, if the first milestone should prove both rich and compact
  rendering immediately.

Implemented first renderers:

- Codex, for compact repository instruction output.
- Cursor, for rule-style output.
- OpenCode, for richer skill-style output.
