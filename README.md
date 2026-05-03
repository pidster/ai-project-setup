# AI Project Setup

Vendor-neutral building blocks for making repositories easier, safer, and more
effective for AI coding tools.

This project aims to provide canonical rules, reusable skills, and vendor
adapters for tools such as Claude Code, GitHub Copilot, Codex, OpenCode,
Windsurf/Devin, and Cursor.

The basic idea: author the guidance once, then project it into each tool's native
configuration surface without letting vendor-specific files become separate
policy sources.

## Status

This repository is currently in design setup.

The repo contains design intent, vendor capability research, instruction files,
an activity-skill backlog, and an initial project skeleton. It has schema stubs,
starter canonical content, vendor capability stubs, adapter placeholders, and
generated-output placeholders. It does not yet contain working renderers or
generated vendor packages.

## Why This Exists

AI coding tools are converging on similar concepts, but not the same file
formats:

- always-on project instructions
- path-scoped rules
- reusable skills
- manual commands or workflows
- custom agents or subagents
- hooks and runtime enforcement
- MCP/tool integrations
- plugin/package mechanisms

Maintaining these independently for every vendor would drift quickly. This repo
is intended to keep the policy and workflow knowledge canonical, then adapt it
for each tool.

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
  claude/
  codex/
  cursor/
  copilot/
  opencode/
  windsurf-devin/

adapters/
  claude/
  codex/
  cursor/
  copilot/
  opencode/
  windsurf-devin/

dist/
  claude/
  codex/
  cursor/
  copilot/
  opencode/
  windsurf-devin/
```

Current boundaries:

- `core/`: canonical rules, skills, schemas, and manifests.
- `vendors/`: declarative vendor capability data.
- `adapters/`: rendering logic and templates.
- `dist/`: generated vendor artifacts.
- `docs/`: design notes, reviews, and rationale.

These directories now exist as a scaffold. Preserve their ownership boundaries
when adding real content and tooling.

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

## Capability Tiers

The vendor research currently tracks three capability tiers.

Superset: everything any supported vendor exposes. This includes skills, hooks,
agents, commands, MCP, plugins, custom tools, imports, runtime permissions, and
external setup fields.

Common Rich Profile: the practical target for first-class adapters. It covers
the emerging shared model: always-on instructions, scoped rules, skills, manual
workflows, MCP/tool config, permissions, hooks, and optional agents.

Lowest Common Denominator: the fallback projection. It is basically Markdown
instructions, a repository-level instruction file, concise conventions, real
verification commands, and safety constraints.

The project should design toward the Common Rich Profile, not the LCD.

## Vendor Fit

Current verified fit for the Common Rich Profile:

| Vendor | Fit |
| --- | --- |
| Claude Code | Full |
| GitHub Copilot | Full |
| OpenCode | Full |
| Windsurf | Full except committed custom agents |
| Devin for Terminal | Full |
| Codex | Partial |
| Cursor | Partial |
| Devin product | Partial |

Claude Code and OpenCode currently look like the strongest first-class
plugin-package targets. Other vendors may still support rich file sets, skills,
hooks, or external setup, but do not all expose one unified plugin bundle format.

## Current Documents

- `docs/design-intent.md`: initial architecture and design intent.
- `docs/design-intent-review.md`: first review pass against the design.
- `docs/vendor-adapter-capabilities.md`: verified vendor capability matrix,
  superset, common rich profile, LCD, and plugin-package notes.
- `docs/activity-skill-backlog.md`: candidate compositional activity skills and
  suggested implementation batches.
- `AGENTS.md`: primary repository instructions for AI agents.
- `docs/AGENTS.md`: scoped documentation-editing instructions.

## Current Instruction Files

This repository includes initial guidance files for several AI tool surfaces:

- `AGENTS.md`
- `CLAUDE.md`
- `.claude/rules/*.md`
- `.github/copilot-instructions.md`
- `.github/instructions/*.instructions.md`
- `.cursor/rules/*.mdc`
- `.windsurf/rules/*.md`
- `docs/AGENTS.md`

These files should remain thin adapters pointing back to the same project
policy. Do not let them drift into separate vendor-specific rule sets.

## Activity Skill Backlog

The current candidate backlog includes:

- daily change loop: `pre-commit`, `commit`, `test`, `build`
- quality loop: `review`, `coverage`, `debug`, `ci-fix`
- maintenance loop: `audit`, `update-dependencies`, `cleanup`,
  `sync-generated`
- collaboration loop: `pr-create`, `pr-address-comments`, `merge`, `rebase`
- runtime loop: `service-start`, `e2e-test`, `visual-check`, `perf-check`

See `docs/activity-skill-backlog.md` for the full list.

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
2. Extend renderer coverage beyond the initial Codex and Cursor outputs.
3. Add snapshot-style checks for generated output reviewability.
4. Add more compositional activity skills after renderer and validation seams are
   proven.

Good first vendor pair: Codex and Cursor for instruction/rule contrast, or Claude
Code and OpenCode for first-class plugin-package exploration.
