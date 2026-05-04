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

Status: proven mechanically, with multiple renderers implemented and remaining
work focused on deeper per-vendor output coverage.

The design identifies three rendering modes: full-fidelity, compact, and hybrid.
Implemented renderers now cover the current vendor adapter set listed in
`docs/README.md`. They exercise compact instruction output, rule-style output,
native skill output, workflow output, and generated runtime placeholders.

Findings:

- The capability-map approach avoids assuming every AI tool supports scoped
  rules or skill invocation.
- Compact rendering remains necessary for product surfaces with a small
  committed instruction surface.
- Hybrid rendering is realistic for tools that support some rich concepts but
  lack a native equivalent for one part of the common profile.

Remaining risk:

- Vendor capabilities change over time. Capability maps and plugin-model maps
  now record source URLs, review dates, and confidence, but the project still
  needs semantic checks that keep related structured files consistent.

## Review 5: Validation and Drift Prevention

Status: executable checks implemented for core metadata, vendor capability
metadata, vendor plugin-model metadata, adapter guardrails, generated-output
freshness, and generated-output manifest freshness.

The validation expectations cover the important graph and metadata invariants.

Findings:

- Dependency direction, unique IDs, missing dependencies, and dependency cycles
  are checked.
- Vendor capability metadata is checked for required declarative fields.
- Vendor plugin-model metadata is checked for required declarative fields,
  allowed model categories, source URLs, review dates, and package-manifest
  consistency.
- Generated outputs are checked for freshness and source ID coverage.
- Vendor adapter policy drift remains harder to validate semantically.

Remaining validation additions:

- Require adapter overlays to use an allowlisted schema.
- Add semantic consistency checks between capability maps, plugin-model maps,
  documentation tables, and renderer behavior.
- Add semantic checks or review workflows for adapter policy drift beyond
  mechanical source ID and generated marker checks.

## Review 6: First Milestone

Status: complete.

The first milestone proved the model without attempting every vendor immediately.

The initial milestone considered contrasting vendor surfaces so the renderer
model would exercise compact instruction output, scoped rules, and richer
skill-style output without trying to cover every product immediately.

Current renderer coverage has expanded beyond the first milestone. Use
`docs/README.md` for the current product compatibility table and adapter links.
