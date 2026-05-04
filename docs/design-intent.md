# Initial Design Intent

This project provides vendor-neutral guidance for configuring repositories so AI
tools can work effectively, safely, and consistently. It should support the AI
tool surfaces listed in `docs/README.md` without allowing each vendor format to
become its own source of policy.

The project should be treated as a content compiler: canonical rules and skills
are authored once, then rendered into vendor-specific plugin, rule, skill, or
instruction formats.

## Goals

- Maintain one source of truth for each policy or procedure.
- Preserve vendor neutrality in canonical content.
- Generate vendor-specific outputs without policy drift.
- Support atomic building blocks and compositional workflows.
- Keep language guidance generic by default, with language-specific extensions
  only where they add material value.
- Make generated outputs reproducible and reviewable.

## Core Concepts

### Rules

Rules define what must be true. They express policy, invariants, constraints, and
quality gates.

Examples:

- Do not stage unrelated changes.
- Do not weaken validation or authorization to make tests pass.
- Mutating backend endpoints require appropriate request protection.
- UI changes require browser verification where browser tooling is available.

Rules should avoid step-by-step workflows unless the command behavior itself is
the policy.

### Skills

Skills define how to do repeatable work. They express procedures, diagnostics,
tool usage, sequencing, and reporting.

Examples:

- How to use Git safely.
- How to discover a repository's language toolchain.
- How to choose and run package-manager commands.
- How to run a pre-commit validation workflow.

Skills may compose rules and other skills.

### Atomic Items

Atomic items own one domain. They are the smallest reusable unit that still has a
clear purpose.

Atomic rules may cover domains such as:

- source-code
- tests
- dependencies
- git-safety
- security
- generated-files
- configuration
- data-files
- ui
- api-contracts

Atomic skills may cover domains such as:

- git
- project-discovery
- language-toolchain
- data-files
- services

Tool-specific skills are still atomic, but they are named as tool skills to make
their role explicit. They may cover concrete tools such as:

- cargo
- npm
- npx
- pnpm
- maven
- gradle
- pytest
- playwright

Atomic items should be focused, reusable, and boring. They should not decide the
whole lifecycle of a task.

### Compositional Items

Compositional items coordinate multiple atomic items to complete a larger
workflow. They decide sequencing, scope, stop or fail behavior, and reporting.
They should not duplicate detailed recipes owned by atomic items.

Compositional rules may cover cross-cutting lifecycle policy such as:

- agent-process
- delivery-gates
- multi-agent-work
- git-workflow

Compositional skills may cover workflows such as:

- pre-commit
- commit
- merge
- test
- build
- audit

Compositional skills may call atomic skills. They may also depend on other
compositional skills when the dependency represents reusable workflow
sequencing, such as `commit` depending on `pre-commit`.

Atomic skills may reference compositional workflows, but should not depend on
them for normal operation.

### Vendor Configs

Vendor configs map canonical rules and skills into a specific AI tool's mechanics.
They adapt canonical guidance to tool capabilities, but they do not redefine
policy.

Examples:

- vendor-specific frontmatter for a skill.
- rule globs and descriptions.
- compact instruction wrappers.
- runtime execution caveats.

Vendor-specific material should be limited to file placement, formatting,
frontmatter, invocation hints, capability notes, and execution caveats.

## Proposed Repository Shape

```text
core/
  rules/
    atomic/
    languages/
    compositional/
  skills/
    atomic/
    tools/
    compositional/
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

`core/` is the canonical source of truth. `vendors/` contains declarative data
about each vendor's capabilities, constraints, and preferred output locations.
`adapters/` contains rendering logic and templates. `dist/` contains generated
artifacts.

## Canonical Metadata

Each canonical item should be a structured Markdown document with frontmatter.

Example atomic skill:

```yaml
id: skill.atomic.git
kind: skill
scope: atomic
category: domain
domain: git
summary: Safe and efficient Git operations for AI agents.
depends_on:
  - rule.atomic.git-safety
commands:
  - git
```

Example tool skill:

```yaml
id: skill.tool.cargo
kind: skill
scope: atomic
category: tool
domain: tool
tool: cargo
summary: Cargo command strategy for Rust projects.
depends_on:
  - rule.language.rust
commands:
  - cargo
```

Example compositional skill:

```yaml
id: skill.compositional.pre-commit
kind: skill
scope: compositional
category: workflow
summary: Run repository-appropriate checks before committing.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
optional_tools:
  - skill.tool.cargo
  - skill.tool.npm
  - skill.tool.maven
  - skill.tool.playwright
```

## Generic Language Model

The canonical architecture should not center one programming language.

Language-neutral rules should own broad source policy:

- Preserve existing project style.
- Prefer small, cohesive changes.
- Avoid unused abstractions.
- Respect public API compatibility.
- Keep generated code separate from hand-authored code.
- Keep error handling intentional.
- Do not weaken validation, authorization, or typing to make tests pass.

Language-specific rules should extend generic source policy only where the
language or ecosystem materially differs.

Example:

```yaml
id: rule.language.rust
kind: rule
scope: atomic
domain: language
language: rust
extends:
  - rule.atomic.source-code
```

Tool skills should stay distinct from language rules. For example, Rust policy
belongs in `rule.language.rust`, while Cargo procedure belongs in
`skill.tool.cargo`.

Compositional workflows should depend on generic discovery and toolchain skills
by default, then select concrete tool skills based on repository evidence. A
pre-commit workflow should not mean "run Cargo"; it should mean "detect the
affected ecosystems, then run the appropriate checks through the relevant tool
skills."

## Selection Model

Canonical items should be selectable by repository evidence and task intent.
Examples of evidence include file globs, manifest files, command availability,
lockfiles, framework markers, and explicit user configuration.

Selection should prefer inclusion by evidence over hardcoded language or vendor
assumptions. For example:

- `Cargo.toml` may select `rule.language.rust` and `skill.tool.cargo`.
- `package.json` may select JavaScript or TypeScript package-manager skills.
- `playwright.config.*` may select `skill.tool.playwright`.
- UI file changes may select UI rules and browser-verification workflows.

This keeps generic workflows portable while still allowing concrete tool skills
to run when they are relevant.

## Vendor Capability Maps

Each vendor should have an explicit capability map. The project should not assume
all tools support equivalent primitives.

Example shape:

```yaml
vendor: example
last_reviewed: 2026-05-02
confidence: provisional
sources:
  - https://vendor.example/docs/agent-config
supports:
  scoped_rules: true
  globs: true
  skill_invocation: false
  frontmatter: true
  generated_summary: true
preferred_outputs:
  - .vendor/rules/*.md
```

Adapters should use these capability maps to decide whether to preserve
full-fidelity structure, emit compact summaries, or use a hybrid output.

Capability maps must be based on contemporary vendor documentation, not memory.
When a vendor surface changes, update the capability map, source links, and
review date before changing adapter behavior.

## Rendering Modes

### Full-Fidelity Render

Use when a vendor supports multiple scoped files, explicit skills, or rich rule
formats. Preserve atomic and compositional structure where possible.

Use this when a product supports multiple scoped files, explicit skills, or rich
rule formats. Product-specific fit and caveats are recorded in `docs/README.md`
and `docs/vendors/`.

### Compact Render

Use when a vendor has a limited instruction surface. Emit a concise generated
summary that prioritizes required rules, high-value workflows, command safety,
and repository-local commands.

Use this when only plain instruction files are verified for a product surface.

### Hybrid Render

Use when a vendor supports some rich surfaces but lacks a native equivalent for
one canonical concept. Emit native surfaces where available and compact guidance
for missing concepts.

Use this for products whose native support is rich in some areas but missing a
direct equivalent for one canonical concept.

## Validation Expectations

The project should validate canonical content before rendering.

Minimum checks:

- Every canonical `id` is unique.
- Every dependency exists.
- No dependency graph cycles exist.
- Atomic skills do not depend on compositional skills.
- Compositional skills may depend on compositional skills for workflow reuse,
  but cycles remain invalid.
- Rules do not depend on skills unless an explicit exception is justified.
- Required metadata fields exist for each `kind` and `scope`.
- Tool skills use `scope: atomic` and `category: tool`.
- Vendor adapters do not define canonical policy.
- Vendor capability files contain data only, not rendering logic.
- Generated outputs are up to date.

Later checks may include Markdown linting, schema validation, broken link checks,
and snapshot tests for generated vendor output.

## Policy Drift Guardrails

Vendor outputs should be generated from canonical content. Hand-authored
vendor-specific overlays should be narrowly scoped.

Allowed vendor adaptation:

- frontmatter
- file naming
- file placement
- globs
- invocation hints
- compact summaries
- runtime capability notes
- execution caveats

Disallowed vendor adaptation:

- redefining canonical rules
- creating conflicting vendor-only policy
- duplicating detailed skill recipes owned by canonical atomic skills
- changing workflow gates without a canonical rule or skill change

If a vendor requires different behavior, represent it as either canonical
applicability metadata or a vendor caveat that explains the runtime limitation.

## Initial Milestone

The first implementation milestone was intentionally narrow:

1. Define the canonical metadata schema.
2. Add a small set of language-neutral atomic rules.
3. Add one or two language-specific extensions as examples.
4. Add atomic skills for Git, project discovery, and language toolchain handling.
5. Add tool skills for one or two concrete tools.
6. Add one compositional skill, such as pre-commit.
7. Add two vendor adapters that exercise different output shapes.
8. Validate dependency direction and required metadata.
9. Generate outputs reproducibly.

The repository now has canonical metadata, canonical rules and skills, vendor
capability data, validation tooling, implemented renderers, and generated
outputs. The next expansion point is deeper coverage within each vendor's
native output surfaces.
