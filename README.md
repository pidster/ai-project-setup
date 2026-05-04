# AI Project Setup

Vendor-neutral building blocks for making repositories easier, safer, and more
effective for AI coding tools.

This project aims to provide canonical rules, reusable skills, and vendor
adapters for the supported products listed in `docs/README.md`.

The basic idea: author the guidance once, then project it into each tool's native
configuration surface without letting vendor-specific files become separate
policy sources.

## Status

This repository is in early implementation.

The repo contains design intent, vendor capability research, instruction files,
canonical rules and skills, schema definitions, validation tooling, vendor
capability data, implemented renderers, and generated outputs.

## Why This Exists

AI coding tools are converging on similar concepts, but not the same file
formats. Maintaining those concepts independently for every vendor would drift
quickly. This repo keeps policy and workflow knowledge canonical, then adapts it
for each tool.

Use `docs/vendor-adapter-capabilities.md` for the canonical feature vocabulary
and `docs/README.md` for the quick compatibility table.

## Design Model

The project treats AI-tool configuration as a content compiler.

Intended architecture:

```text
core/
  rules/
  skills/
  schemas/
  manifest.yaml

vendors/
  <vendor>/

adapters/
  <vendor>/

dist/
  <vendor>/
```

Current boundaries:

- `core/`: canonical rules, skills, schemas, and manifests.
- `vendors/`: declarative vendor capability data.
- `adapters/`: rendering logic and templates.
- `dist/`: generated vendor artifacts.
- `docs/`: design notes, reviews, and rationale.

Preserve these ownership boundaries when adding content and tooling.

## Core Concepts

Rules define what must be true: policy, invariants, constraints, and gates.

Skills define how to do repeatable work: procedures, diagnostics, tool usage,
sequencing, and reporting.

Atomic items own one focused domain. Examples: `git`, `source-code`,
`security`, `cargo`, `npm`, `playwright`.

Compositional items coordinate multiple atomic items. Examples: `pre-commit`,
`commit`, `test`, `coverage`, `debug`, `update-dependencies`.

Vendor configs adapt canonical content to a tool's mechanics. They should handle
file placement, frontmatter, globs, invocation hints, capability notes, and
execution caveats. They should not redefine policy.

## Capability Model

The project should design toward the common rich profile, not the lowest common
denominator. The canonical capability definitions live in
`docs/vendor-adapter-capabilities.md`; the current product compatibility summary
lives in `docs/README.md`.

## Current Documents

- `docs/README.md`: documentation index, canonical compatibility table, and
  vendor detail links.
- `docs/design-intent.md`: initial architecture and design intent.
- `docs/design-intent-review.md`: first review pass against the design.
- `docs/vendor-adapter-capabilities.md`: cross-vendor vocabulary, rich profile,
  concept mappings, and adapter degradation rules.
- `docs/vendors/*.md`: per-product capability details, source URLs, caveats, and
  adapter notes.
- `docs/activity-skill-backlog.md`: implemented compositional activity skills
  and the original batching rationale.
- `AGENTS.md`: primary repository instructions for AI agents.
- `docs/AGENTS.md`: scoped documentation-editing instructions.

## Instruction Files

Hand-authored instruction files should remain thin adapters pointing back to the
same project policy. Generated vendor outputs live under `dist/`. Use
`docs/README.md` for product compatibility and `docs/vendors/` for
source-backed vendor details.

## Activity Skill Backlog

The implemented compositional activity skills include:

- daily change loop: `pre-commit`, `commit`, `test`, `build`
- quality loop: `review`, `coverage`, `debug`, `ci-fix`
- maintenance loop: `audit`, `update-dependencies`, `cleanup`,
  `sync-generated`
- collaboration loop: `pr-create`, `pr-address-comments`, `merge`, `rebase`
- runtime loop: `service-start`, `e2e-test`, `visual-check`, `perf-check`

See `docs/activity-skill-backlog.md` for the full implemented list and original
batching notes.

## Development Principles

- Verify current vendor docs before changing adapter behavior.
- Keep canonical content vendor-neutral.
- Keep language policy generic by default; add language-specific extensions only
  where they materially differ.
- Keep language rules separate from tool procedures.
- Generate vendor outputs from canonical content.
- Mark generated files as generated.
- Prefer Python for project scripting and validation tooling.
- Use `jq`, `yq`, and `mdq` for focused JSON, YAML, and Markdown inspection when
  that is simpler than a script.
- Do not stage unrelated changes.

## Near-Term Work

Likely next steps:

1. Expand validation coverage for vendor adapter policy drift.
2. Deepen renderer coverage beyond the initial output shapes for each supported
   vendor.
3. Add richer vendor-specific projections, such as command, hook, agent, or
   plugin outputs where supported by verified vendor capability and plugin-model
   data.
