# Repository Instructions

Do not be a sycophant. Do be helpful. When you identify discrepancies between
these instructions, user instructions, existing project guidance, or tool-specific
rules, stop and bring the discrepancy to the user's attention.

## Project Purpose

This repository designs and publishes vendor-neutral guidance for configuring
repositories so AI tools can work effectively, safely, and consistently.

Target AI tool surfaces include Claude, Copilot, Codex, OpenCode,
Windsurf/Devin, and Cursor.

The project's core design is documented in:

- `docs/design-intent.md`
- `docs/design-intent-review.md`
- `docs/vendor-adapter-capabilities.md`

Treat those documents as the current design source until the repository has a
formal schema and generated artifacts.

## Core Architecture

This repository should behave like a content compiler:

- Canonical rules and skills are authored once.
- Vendor-specific files adapt canonical content to each tool surface.
- Vendor-specific files must not become independent sources of policy.

Keep these boundaries intact:

- `core/`: canonical rules, skills, schemas, manifests.
- `vendors/`: declarative vendor capability data.
- `adapters/`: rendering logic and templates.
- `dist/`: generated vendor artifacts.
- `docs/`: design notes, reviews, and rationale.

If a directory does not exist yet, preserve the intended boundary when creating
it.

## Rules, Skills, and Vendor Configs

Rules define what must be true. They express policy, invariants, constraints,
and gates.

Skills define how to do repeatable work. They express procedures, diagnostics,
tool usage, sequencing, and reporting.

Atomic items own one focused domain. They should be reusable building blocks.

Compositional items coordinate multiple atomic items to complete a larger
workflow. They own sequencing, stop or fail behavior, and reporting.

Vendor configs map canonical rules and skills into a specific AI tool's
mechanics. They may adapt formatting, frontmatter, file placement, globs,
invocation hints, capability notes, and execution caveats. They must not redefine
canonical policy.

## Language and Tool Guidance

Do not center the model on one programming language.

Use generic language-neutral policy first, then add language-specific extensions
only where the language or ecosystem materially differs.

Keep language rules separate from tool procedures:

- Source policy belongs in rules such as `rule.atomic.source-code`.
- Language-specific policy belongs in rules such as `rule.language.rust`.
- Concrete tool procedure belongs in skills such as `skill.tool.cargo`.

Compositional workflows should select concrete tools from repository evidence,
such as manifest files, lockfiles, command availability, framework markers, file
globs, and explicit configuration.

## Editing Guidance

Prefer small, cohesive changes that preserve the design boundaries.

When adding canonical content:

- Add structured metadata before body content.
- Use stable IDs.
- Keep atomic items focused.
- Put workflow sequencing in compositional items.
- Avoid duplicating policy across rules, skills, and vendor configs.

When adding vendor support:

- Verify the vendor's current official documentation before changing adapter
  behavior.
- Record source URLs, review date, and confidence in the vendor capability docs.
- Start from canonical content.
- Capture vendor capabilities declaratively.
- Put rendering behavior in adapters.
- Mark generated output as generated.
- Do not hand-author competing policy in vendor output.

When documenting design decisions:

- Record rationale and open questions.
- Separate design intent from review findings.
- Prefer clear constraints over broad aspirations.

## Validation Expectations

As tooling is added, validation should check:

- Unique canonical IDs.
- Existing dependencies.
- No dependency cycles.
- Atomic skills do not depend on compositional skills.
- Rules do not depend on skills unless explicitly justified.
- Tool skills use `scope: atomic` and `category: tool`.
- Vendor capability files are declarative data only.
- Generated output is up to date.

Until validation tooling exists, review changes manually against these
expectations.

## Git and Delivery

Do not stage unrelated changes.

Before committing, review the diff and explain any design-impacting changes.

If tests or validation commands do not exist yet, state that clearly instead of
inventing a successful verification result.
