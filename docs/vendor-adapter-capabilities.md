# Vendor Adapter Capabilities

Last reviewed: 2026-05-04

This document defines the shared vocabulary used when designing vendor adapters.
For quick product lookup, use [the docs index](README.md). For detailed vendor
surfaces and source URLs, use the [vendor detail index](vendors/README.md).

Vendor capabilities change over time. Do not update adapter behavior from
memory. Verify current official documentation first, then update:

1. `vendors/<vendor>/capabilities.yaml`
2. `docs/vendors/<product>.md`
3. [docs/README.md](README.md), if the quick-reference table changes
4. Any affected adapter and generated output

## Rich Profile

The Common Rich Profile is the practical target for first-class adapters. It
represents the strongest emerging shared model across products that support more
than plain instruction files.

The profile includes:

- Always-on project instructions.
- Path-scoped or directory-scoped rules.
- Model-selected skills using `SKILL.md` or an equivalent progressively loaded
  mechanism.
- Manual workflow prompts, slash commands, or command-like workflows.
- MCP or equivalent external tool configuration.
- Runtime permissions, approval policy, or execution constraints.
- Event hooks, lifecycle hooks, or plugin event subscriptions.
- Optional specialized agents or subagents where the vendor supports them.

The profile describes capability classes, not identical file paths. A product
can support rules without exposing a dedicated `rules/` directory, or support
manual workflows through skills rather than command files. Adapter output should
follow the verified native surface for that product.

The profile does not require:

- A committed custom-agent profile format.
- Vendor plugin systems.
- First-class plugin-package mechanisms.
- Custom model-callable tools.
- Cross-vendor config imports.
- External repo setup fields.
- Non-durable memory systems.
- Vendor-specific enterprise deployment surfaces.

## Product Fit

The canonical quick-reference table lives in [docs/README.md](README.md).
Product-specific details, caveats, and source URLs live under
[docs/vendors/](vendors/README.md). Do not repeat product fit or feature support
tables or summaries here.

## Cross-Vendor Concepts

### Always-On Project Instructions

Canonical concept: repository-wide instruction context.

Adapters should choose the target product's verified always-on instruction
surface, such as a repository instruction file, an always-on rule file, or a
configured fallback instruction file. See [docs/README.md](README.md) for the
product summary and [docs/vendors/](vendors/README.md) for source-backed
details.

### Path-Scoped Instructions

Canonical concept: guidance that applies only to matching files or subtrees.

Adapters should use the target product's verified mechanism for directory
scope, file globs, or fallback nested instruction files. If the product has no
native path-scoped surface, emit compact guidance through the closest supported
instruction mechanism.

### Model-Selected Rules or Skills

Canonical concept: guidance available to the model when it decides the task
matches.

Adapters should preserve skill structure where the target product supports
progressively loaded skills. Where no native skill format exists, use the
closest verified model-selected rule or command-like surface and keep the
canonical procedure in `core/skills/`.

### Manual Workflow Prompts

Canonical concept: user-invoked repeatable workflows.

Adapters should use the target product's verified command, prompt, workflow, or
skill-invocation mechanism. If no committed custom workflow surface exists, keep
the workflow as a canonical skill and expose only a compact pointer.

### Specialized Agents

Canonical concept: role-specific agent behavior.

Adapters should emit custom agent profiles only for products with verified
committed agent-profile formats. Product-level agent concepts are not enough by
themselves; the repository needs an official committed file surface before
generating agent output.

### Runtime Enforcement and Permissions

Canonical concept: deterministic execution control distinct from prompt policy.

Adapters should treat runtime controls as execution adapters. They may enforce,
gate, or log behavior, but they should not be the only place where project
policy is stated and must not redefine canonical prompt policy.

### Tool and Data Integrations

Canonical concept: external tools or data sources made available to the model.

Adapters should represent tool and data integrations as runtime configuration
or installable bundles where the product supports them. Canonical rules and
skills may describe when to use a tool, but vendor runtime files own the
mechanics of making that tool available.

### Pluggable Vendor Tools

Canonical concept: a vendor-native installable or loadable bundle that can carry
multiple capabilities together, such as rules, skills, commands, agents, hooks,
tools, or integrations.

Do not confuse MCP servers with vendor plugins. MCP adds tools and data access;
a vendor plugin may bundle MCP with instructions, hooks, skills, commands, or
other vendor-native behavior. Do not confuse skills with vendor plugins either:
skills are reusable procedures, while plugin packages may contain skills plus
other capabilities. Product-specific plugin support belongs in the quick table
and vendor detail pages, not in this concept document.

### Compatibility Imports

Canonical concept: one vendor reading another vendor's configuration format.

Compatibility imports are useful but can hide policy duplication. Adapters that
rely on another product's file format must document that import behavior in the
vendor detail page and avoid emitting conflicting copies of canonical policy.

## Cross-Vendor Superset

The current superset this project should model is:

- Always-on project instructions.
- Path-scoped instructions by glob or directory.
- Nested directory-scoped instructions.
- Model-selected rules.
- Model-selected skills with supporting files.
- Manual workflow prompts or slash commands.
- Specialized subagents.
- Custom agent profiles.
- Runtime settings and permissions.
- Hooks, lifecycle commands, and plugin event subscriptions.
- MCP server configuration.
- Custom model-callable tools.
- Vendor plugin systems.
- First-class plugin-package mechanisms.
- Compatibility imports from other vendors' config formats.
- Agent skill permissions and trigger controls.
- Auto-generated or local memory systems that should not be treated as durable
  repo policy.
- External repository setup fields.
- Generated compact summaries.
- Vendor capability metadata including source URLs, last-reviewed dates, and
  confidence.

Not every vendor supports every concept. Canonical content should be rich enough
to express the superset, while each adapter degrades deliberately when the target
surface lacks a native equivalent.

## Lowest Common Denominator

The lowest common denominator across the target tools is:

- Markdown instruction text.
- A repository-level Markdown instruction file, with adapter-specific filenames
  where needed.
- Basic nested directory scoping through instruction files where the vendor
  supports it.
- Concise project purpose and conventions.
- Build, test, lint, and verification commands when they exist.
- Safety and Git workflow constraints.
- Short workflow pointers that describe what to do, without assuming
  slash-command or skill invocation.
- Pointers to canonical docs for details.

The lowest common denominator does not include path-scoped frontmatter,
automatic skill discovery, slash commands, subagents, hooks, custom agents,
custom tools, MCP configuration, vendor plugins, compatibility imports, or local
memory systems.
