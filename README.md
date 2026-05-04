# AI Project Setup

Vendor-neutral building blocks for making repositories easier, safer, and more
effective for AI coding tools.

This project aims to provide canonical rules, reusable skills, and vendor
adapters for tools such as Claude Code, GitHub Copilot, Codex, OpenCode,
Windsurf, Devin, and Cursor.

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
  devin/
  opencode/
  windsurf/

adapters/
  claude/
  codex/
  cursor/
  copilot/
  devin/
  opencode/
  windsurf/

dist/
  claude/
  codex/
  cursor/
  copilot/
  devin/
  opencode/
  windsurf/
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
| Devin for Terminal | Full, but no verified `.devin/rules/` directory |
| Codex | Full, but no verified custom slash-command prompt files |
| Cursor | Partial |
| Devin product | Partial |

Claude Code and OpenCode currently look like the strongest first-class
plugin-package targets. Other vendors may still support rich file sets, skills,
hooks, or external setup, but do not all expose one unified plugin bundle format.
The Devin adapter uses `AGENTS.md` for committed rule guidance, `.agents/skills`
for Devin product skills, and `.devin/skills`, `.devin/agents`,
`.devin/hooks.v1.json`, and `.devin/config.json` for Devin for Terminal.
The Codex adapter currently emits only the baseline `AGENTS.md`; verified Codex
surfaces also include `.agents/skills`, `.codex/agents`, `.codex/rules`,
`.codex/config.toml`, hooks, MCP, and plugins.

## Current Documents

- `docs/design-intent.md`: initial architecture and design intent.
- `docs/design-intent-review.md`: first review pass against the design.
- `docs/vendor-adapter-capabilities.md`: verified vendor capability matrix,
  superset, common rich profile, LCD, and plugin-package notes.
- `docs/activity-skill-backlog.md`: implemented compositional activity skills
  and the original batching rationale.
- `AGENTS.md`: primary repository instructions for AI agents.
- `docs/AGENTS.md`: scoped documentation-editing instructions.

## Current Instruction Files

This repository includes guidance files for several AI tool surfaces:

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
   plugin-package outputs where supported by verified vendor capabilities.
