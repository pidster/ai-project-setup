# Vendor Adapter Capabilities

Last reviewed: 2026-05-02

This document records the current vendor instruction and extension surfaces this
project should account for when designing vendor adapters. Vendor capabilities
change over time, so do not update adapter behavior from memory. Verify current
official documentation first, then update this document with sources and review
dates.

## Sources

- Claude Code memory and rules:
  <https://code.claude.com/docs/en/memory>
- Claude Code settings:
  <https://docs.claude.com/en/docs/claude-code/settings>
- Claude Code slash commands:
  <https://docs.claude.com/en/docs/claude-code/slash-commands>
- Claude Code subagents:
  <https://docs.claude.com/en/docs/claude-code/subagents>
- Claude Code skills:
  <https://docs.claude.com/en/docs/claude-code/skills>
- Claude Code hooks:
  <https://docs.claude.com/en/docs/claude-code/hooks>
- Claude Code plugins:
  <https://docs.claude.com/en/docs/claude-code/plugins>
- GitHub Copilot custom instructions:
  <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
- GitHub Copilot response customization:
  <https://docs.github.com/en/copilot/concepts/prompting/response-customization>
- GitHub Copilot custom-instruction support matrix:
  <https://docs.github.com/en/copilot/reference/custom-instructions-support>
- GitHub Copilot agent skills:
  <https://docs.github.com/en/copilot/concepts/agents/about-agent-skills>
- GitHub Copilot custom agents:
  <https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents>
- GitHub Copilot custom-agent configuration:
  <https://docs.github.com/en/copilot/reference/custom-agents-configuration>
- GitHub Copilot hooks:
  <https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-hooks>
- GitHub Copilot MCP for coding agent:
  <https://docs.github.com/en/copilot/concepts/coding-agent/mcp-and-coding-agent>
- Cursor rules:
  <https://docs.cursor.com/en/context/rules>
- Cursor custom commands:
  <https://docs.cursor.com/en/agent/chat/commands>
- Cursor modes:
  <https://docs.cursor.com/agent>
- Cursor CLI MCP:
  <https://docs.cursor.com/cli/mcp>
- OpenCode rules:
  <https://opencode.ai/docs/rules>
- OpenCode config:
  <https://opencode.ai/docs/config/>
- OpenCode agents:
  <https://opencode.ai/docs/agents/>
- OpenCode commands:
  <https://dev.opencode.ai/docs/commands/>
- OpenCode skills:
  <https://opencode.ai/docs/skills/>
- OpenCode plugins:
  <https://opencode.ai/docs/plugins/>
- OpenCode custom tools:
  <https://opencode.ai/docs/custom-tools/>
- OpenCode permissions:
  <https://opencode.ai/docs/permissions>
- Windsurf AGENTS.md:
  <https://docs.windsurf.com/windsurf/cascade/agents-md>
- Windsurf memories and rules:
  <https://docs.windsurf.com/windsurf/cascade/memories>
- Windsurf skills:
  <https://docs.windsurf.com/windsurf/cascade/skills>
- Windsurf workflows:
  <https://docs.windsurf.com/windsurf/cascade/workflows>
- Windsurf hooks:
  <https://docs.windsurf.com/windsurf/cascade/hooks>
- Devin AGENTS.md:
  <https://docs.devin.ai/onboard-devin/agents-md>
- Devin repository setup:
  <https://docs.devin.ai/onboard-devin/new-repo-setup>
- Devin skills:
  <https://docs.devin.ai/product-guides/skills>
- Devin for Terminal rules:
  <https://cli.devin.ai/docs/extensibility/rules>
- Devin for Terminal extensibility overview:
  <https://cli.devin.ai/docs/extensibility>
- Devin for Terminal skills:
  <https://cli.devin.ai/docs/extensibility/skills/overview>
- Devin for Terminal custom subagents:
  <https://cli.devin.ai/docs/subagents>
- Devin for Terminal hooks:
  <https://cli.devin.ai/docs/extensibility/hooks/overview>
- Devin for Terminal configuration:
  <https://cli.devin.ai/docs/extensibility/configuration>
- OpenAI Codex AGENTS.md behavior:
  <https://openai.com/index/introducing-codex/>
- Codex agent loop and instruction aggregation:
  <https://openai.com/index/unrolling-the-codex-agent-loop/>
- OpenAI Codex config:
  <https://github.com/openai/codex/blob/main/docs/config.md>
- OpenAI Codex AGENTS.md docs:
  <https://github.com/openai/codex/blob/main/docs/agents_md.md>
- OpenAI Codex skills:
  <https://github.com/openai/codex/blob/main/docs/skills.md>
- OpenAI Skills catalog and skill format:
  <https://github.com/openai/skills>

## Full Vendor Surfaces

### Claude Code

Status: verified from current Claude Code docs.

Instruction and extension surfaces:

- `CLAUDE.md` or `.claude/CLAUDE.md`: project instructions.
- `CLAUDE.local.md`: local personal project instructions; should not be
  committed.
- `.claude/rules/**/*.md`: modular project rules. Rules without `paths`
  frontmatter load at launch; rules with `paths` load when matching files are
  read.
- `~/.claude/rules/**/*.md`: user-level rules.
- `@path` imports inside `CLAUDE.md`.
- `.claude/skills/<skill>/SKILL.md`: project skills with optional supporting
  files.
- `.claude/commands/**/*.md`: project slash commands.
- `.claude/agents/*.md`: project subagents with YAML frontmatter.
- `.claude/settings.json`: shared project settings, including permissions,
  environment variables, hooks, sandbox settings, MCP server settings, and
  exclusions.
- `.claude/settings.local.json`: local project settings.
- Hooks configured through settings.
- Plugins that can include commands, agents, hooks, skills, and MCP servers.
- MCP servers configured through settings.
- Plugin-defined tools and integrations.

Adapter notes:

- Use root `CLAUDE.md` as the compact entry point.
- Import `AGENTS.md` from `CLAUDE.md` when sharing cross-tool instructions.
- Use `.claude/rules/` for path-scoped rules, comparable to Copilot
  `.github/instructions/` and Cursor glob rules.
- Use `.claude/skills/` for rich capabilities with supporting files.
- Use `.claude/commands/` for manually invoked workflows.
- Do not model Claude settings as policy. Settings can enforce permissions and
  runtime behavior, while canonical rules define project policy.
- Use plugins and MCP as tool-integration adapters, not as canonical rules.

### GitHub Copilot

Status: verified from current GitHub Docs.

Instruction and extension surfaces:

- `.github/copilot-instructions.md`: repository-wide custom instructions.
- `.github/instructions/**/*.instructions.md`: path-specific custom
  instructions with `applyTo` frontmatter.
- `AGENTS.md`: agent instructions. Copilot uses the nearest `AGENTS.md` in the
  directory tree where supported.
- Root `CLAUDE.md` or `GEMINI.md`: accepted as agent-instruction alternatives in
  some Copilot contexts.
- `.github/prompts/**/*.prompt.md`: reusable prompt files where supported;
  currently a preview feature in supported IDEs.
- `.github/skills/<skill>/SKILL.md`: project agent skills. Copilot also scans
  `.claude/skills/` and `.agents/skills/` for project skills.
- Personal skills can live in `~/.copilot/skills`, `~/.claude/skills`, or
  `~/.agents/skills`.
- Custom agents are Markdown agent profiles that specify prompts, tools, and MCP
  servers. They are used by Copilot CLI and Copilot coding-agent contexts that
  support custom agents.
- Repository-level custom agent profiles live at
  `.github/agents/<custom-agent-name>.md`.
- Organization or enterprise custom agent profiles can live in a `.github-private`
  repository under `/agents/<custom-agent-name>.md`.
- MCP servers can extend Copilot coding agent with tools. Copilot coding agent
  supports MCP tools, but not MCP resources or MCP prompts.
- Hooks are JSON files under `.github/hooks/*.json` and execute shell commands at
  agent lifecycle points. Hook support applies to Copilot cloud agent and GitHub
  Copilot CLI.
- Hook triggers include session lifecycle, prompt, and tool-call points as defined
  by GitHub's hook reference.
- Organization and personal instructions exist outside the repository and may
  also apply.

Adapter notes:

- Use `.github/copilot-instructions.md` for compact repository-wide summaries.
- Use `.github/instructions/` for path-scoped guidance.
- Treat prompt files as manually selected workflow prompts, not always-on
  policy.
- Use `.github/skills/` when projecting canonical skills into Copilot-specific
  output; use `.agents/skills/` when the goal is cross-vendor skill reuse.
- Use custom agents for role-specific execution profiles, not for canonical
  policy.
- Use hooks for enforcement, logging, or validation. Do not make hooks the only
  place a policy is stated.
- Avoid relying solely on `AGENTS.md`, because Copilot feature support varies.

### Cursor

Status: verified from current Cursor docs.

Instruction and extension surfaces:

- `.cursor/rules/*.mdc`: project rules with MDC frontmatter.
- Rule activation types are represented by `description`, `globs`, and
  `alwaysApply`.
- Nested `.cursor/rules/` directories can scope rules to subdirectories.
- `AGENTS.md`: supported as a simple alternative to `.cursor/rules`.
- Cursor CLI also reads root `AGENTS.md` and `CLAUDE.md` and applies them as
  rules alongside `.cursor/rules`.
- `.cursor/commands/*.md`: project custom commands. They appear as slash-command
  workflows in chat.
- Custom modes exist in the product and can configure different capabilities and
  tools for workflows, but current docs do not define a repo-committed custom
  mode file format.
- MCP servers are supported for Cursor CLI through the same MCP configuration
  used by the editor.
- `.cursorrules`: legacy and deprecated.
- User rules and memories exist outside the repository.
- No current official Cursor docs found for repo-native `SKILL.md` agent skills.
- No current official Cursor docs found for repo-native event hooks comparable to
  Claude, Copilot, OpenCode, Windsurf, or Devin hooks.

Adapter notes:

- Use `.cursor/rules/*.mdc` for full-fidelity scoped rules.
- Use `alwaysApply: true` only for short project-wide instructions.
- Use `globs` for path-scoped guidance.
- Use `description` for agent-requested rules.
- Use `.cursor/commands/` for manually invoked workflows.
- Do not project canonical skills into Cursor as `SKILL.md` unless Cursor adds
  native skill support. Use agent-requested rules or commands as the closest
  available adapter surfaces.

### OpenCode

Status: verified from current OpenCode docs.

Instruction and extension surfaces:

- `AGENTS.md`: primary project rules.
- `CLAUDE.md`: project fallback when `AGENTS.md` is absent.
- `~/.config/opencode/AGENTS.md`: global rules.
- `opencode.json`: project config.
- `opencode.json` `instructions`: additional local, globbed, or remote
  instruction files.
- `.opencode/commands/*.md`: project custom commands.
- `~/.config/opencode/commands/*.md`: global custom commands.
- `opencode.json` `command`: JSON-defined custom commands.
- `opencode.json` `agent`: primary and subagent configuration.
- `.opencode/agents/*.md` and `~/.config/opencode/agents/*.md`: Markdown agent
  definitions.
- `default_agent` in `opencode.json`: selects the default primary agent.
- `.opencode/skills/<name>/SKILL.md`: project skills loaded on demand by the
  native `skill` tool.
- `~/.config/opencode/skills/<name>/SKILL.md`: global skills.
- OpenCode also scans `.claude/skills/`, `~/.claude/skills/`, `.agents/skills/`,
  and `~/.agents/skills/`.
- `permission.skill` can allow, deny, or ask before loading skills, globally or
  per agent.
- `.opencode/plugins/*.js` or `.opencode/plugins/*.ts`: project plugins.
- `~/.config/opencode/plugins/`: global plugins.
- `opencode.json` `plugin`: npm plugin packages.
- Plugins can subscribe to command, file, installation, LSP, message, permission,
  server, session, todo, shell, tool, and TUI events.
- Plugins can add custom tools.
- `.opencode/tools/`: custom tools callable by the model.
- `opencode.json` `mcp`: MCP server configuration.
- `opencode.json` `permission`: action approvals for read, edit, glob, grep,
  list, bash, task, skill, LSP, todo, web, external-directory, and loop-safety
  guards.
- Claude Code compatibility for some Claude instruction and skill locations,
  unless disabled by environment variables.

Adapter notes:

- Use `AGENTS.md` as the baseline rule output.
- Use `opencode.json` when an adapter needs to compose multiple instruction
  files without duplicating content.
- Use `.opencode/commands/` for manual workflows.
- Use OpenCode agents for role-specific behavior, not canonical policy.
- Use `.opencode/skills/` for OpenCode-specific skills and `.agents/skills/` for
  cross-vendor skills.
- Use plugins and custom tools for executable integrations; represent their
  behavior in canonical rules or skills before enforcing it in runtime hooks.

### Windsurf

Status: verified from current Windsurf docs.

Instruction and extension surfaces:

- `AGENTS.md` or `agents.md`: location-scoped instructions. Root files are
  always on; subdirectory files auto-scope to that subtree.
- `.windsurf/rules/*.md`: workspace rules with `trigger` frontmatter.
- Rule triggers: `always_on`, `glob`, `model_decision`, and `manual`.
- Rules can include `description` and `globs`.
- Rules can live in workspace, parent, global, and enterprise system locations.
- Workspace rules are limited to 12,000 characters per file; global rules are
  limited to 6,000 characters.
- `.windsurf/workflows/*.md`: manually invoked slash-command workflows. Windsurf
  discovers workflows in current workspace, subdirectories, and parent
  directories up to the git root.
- `.windsurf/skills/<skill-name>/SKILL.md`: workspace skills with supporting
  files and progressive disclosure.
- Global skills live under `~/.codeium/windsurf/skills/`.
- Enterprise system skills can be deployed to OS-specific system directories.
- Windsurf also discovers `.agents/skills/` and, when Claude config reading is
  enabled, `.claude/skills/`.
- `.windsurf/hooks.json`: workspace hooks.
- User hooks and enterprise system hooks are also supported.
- Hook events cover pre/post MCP tool use, file read/write/edit, command
  execution, user prompt handling, Cascade responses, and transcript access.
- Hooks can block pre-actions by exiting with code `2`.
- Memories exist outside version control and should not be treated as durable
  project policy.
- No current official Windsurf docs found for repo-committed custom subagent
  profiles comparable to Claude `.claude/agents/`, Copilot custom agents,
  OpenCode agents, or Devin `.devin/agents/`.

Adapter notes:

- Use root `AGENTS.md` for the simplest always-on project guidance.
- Use `.windsurf/rules/` for explicit activation control.
- Use `glob` rules for path-scoped guidance.
- Use skills for complex procedures with supporting files.
- Use workflows for manual slash-command runbooks.
- Use hooks for enforcement, logging, validation, and lifecycle automation.

### Devin

Status: verified from current Devin docs.

Instruction and extension surfaces:

- `AGENTS.md`: project instructions. Devin supports placing it at the root or
  elsewhere in the repository.
- Devin for Terminal also reads `AGENT.md` and `CLAUDE.md` as equivalent
  always-on rules.
- Devin for Terminal loads workspace-root rule files at session start and
  discovers subdirectory rule files lazily.
- Devin for Terminal imports rules from `.cursor/rules/*.md`, `.cursorrules`,
  and `.windsurf/rules/*.md` when enabled.
- `.devin/config.json`: project configuration for permissions, MCP servers,
  imports, and hooks.
- `.devin/config.local.json`: local project overrides.
- `~/.config/devin/config.json`: user configuration.
- `.agents/skills/<skill-name>/SKILL.md`: recommended repo skill location for
  Devin product sessions.
- Devin also scans `.github/skills/<skill-name>/SKILL.md` and
  `.claude/skills/<skill-name>/SKILL.md`.
- Devin for Terminal supports `.devin/skills/<skill-name>/SKILL.md` with skill
  frontmatter for allowed tools, triggers, model overrides, permissions, and
  optional subagent execution.
- Devin for Terminal skills can be invoked by users as `/skill-name` or selected
  by the model.
- `.devin/agents/<agent-name>/AGENT.md`: custom subagent profiles with system
  prompt, model, allowed tools, and permissions.
- `.agents/agents/<agent-name>/AGENT.md`: alternate custom subagent location.
- Devin for Terminal imports Claude Code `.claude/agents/*.md` as subagents when
  Claude config import is enabled.
- `.devin/hooks.v1.json`: project lifecycle hooks using a Claude-compatible hook
  format.
- `.devin/config.json`, `.devin/config.local.json`, and user config can also
  contain hooks.
- Hooks can be command hooks or prompt hooks and can enforce policies, add
  context, modify permissions, log actions, and trigger side effects.
- Repo setup fields outside the repository configure upkeep, dependency
  maintenance, lint commands, test commands, and repo-specific knowledge.
- Devin docs recommend using repo setup so Devin knows how to verify work.

Adapter notes:

- Use `AGENTS.md` as the portable committed instruction file.
- Treat Devin repo setup as an external environment adapter, not a committed
  vendor rule format.
- Keep lint/test command guidance canonical so it can be copied into Devin repo
  setup or surfaced in `AGENTS.md`.
- Use `.agents/skills/` for cross-vendor skills intended for Devin product
  sessions; use `.devin/skills/` for Devin for Terminal-specific skill features.
- Use `.devin/agents/` for custom subagent profiles only when targeting Devin for
  Terminal.
- If importing other vendors' config, document that import explicitly to avoid
  hidden policy duplication.

### Codex

Status: verified from OpenAI Codex public documentation and system-message
description.

Instruction and extension surfaces:

- `AGENTS.md`: scoped agent instructions. A file applies to the directory tree
  rooted at its containing directory.
- More deeply nested `AGENTS.md` files take precedence for files in their scope.
- Direct user, developer, and system instructions take precedence over
  `AGENTS.md`.
- Codex aggregates instructions from configured home and project sources.
- Codex project configuration can specify fallback instruction filenames.
- Codex supports skills using `SKILL.md` folders with required `name` and
  `description` frontmatter and optional bundled resources.
- Codex skills use progressive disclosure: metadata is always available, the
  skill body loads when triggered, and supporting resources are loaded or used as
  needed.
- `~/.codex/config.toml`: Codex configuration, including MCP servers and project
  document fallback behavior.
- MCP servers can be configured in Codex config, including tool approval behavior
  and parallel-tool-call support where safe.
- Codex supports notification hooks when the agent finishes a turn.
- Codex can use ChatGPT connector apps where available.
- No current official committed repo format found for Codex-specific custom
  subagent profiles comparable to Claude `.claude/agents/`, OpenCode agents, or
  Devin `.devin/agents/`.
- No current official committed repo format found for Codex-specific slash
  command prompt files comparable to `.claude/commands/`, `.cursor/commands/`, or
  `.opencode/commands/`.

Adapter notes:

- Use `AGENTS.md` as the primary Codex output.
- Use nested `AGENTS.md` files for directory-specific guidance.
- Put verification commands in `AGENTS.md` only when they are real and intended
  to be run.
- Use cross-vendor `.agents/skills/` for Codex-consumable skills unless a
  Codex-specific package format is later verified.
- Treat Codex config and MCP settings as environment/runtime adapters, not
  canonical policy.

## Capability Coverage Summary

This table summarizes the second pass across the expanded superset.

| Vendor | Custom Agents | Skills | Path-Based Rules | Custom Prompts or Commands | Event Hooks | MCP, Tools, or Plugins |
| --- | --- | --- | --- | --- | --- | --- |
| Claude Code | `.claude/agents/*.md` | `.claude/skills/*/SKILL.md` | `.claude/rules/*.md` with `paths` | `.claude/commands/**/*.md` | settings hooks | settings MCP, plugins |
| GitHub Copilot | `.github/agents/*.md` | `.github/skills/`, `.claude/skills/`, `.agents/skills/` | `.github/instructions/*.instructions.md`, `AGENTS.md` where supported | `.github/prompts/*.prompt.md`, agent profiles | `.github/hooks/*.json` | MCP tools for coding agent |
| Cursor | No verified repo-native agent-profile format | No verified repo-native `SKILL.md` support | `.cursor/rules/*.mdc`, `AGENTS.md`, `CLAUDE.md` in CLI | `.cursor/commands/*.md`, manual rules | No verified repo-native event hooks | MCP configuration shared by editor and CLI |
| OpenCode | `opencode.json` `agent`, `.opencode/agents/*.md` | `.opencode/skills/`, `.claude/skills/`, `.agents/skills/` | `AGENTS.md`, `CLAUDE.md`, `opencode.json` `instructions` globs | `.opencode/commands/*.md`, `opencode.json` `command` | `.opencode/plugins/` event subscriptions | MCP, plugins, custom tools, permissions |
| Windsurf | No verified repo-committed custom subagent profile format | `.windsurf/skills/`, `.agents/skills/`, optional `.claude/skills/` | `AGENTS.md`, `.windsurf/rules/*.md` with `trigger: glob` | `.windsurf/workflows/*.md` | `.windsurf/hooks.json` | MCP plus hooks observing MCP usage |
| Devin | `.devin/agents/*/AGENT.md`, `.agents/agents/*/AGENT.md` in Devin for Terminal | `.agents/skills/`, `.github/skills/`, `.claude/skills/`, `.devin/skills/` in Terminal | `AGENTS.md`, `AGENT.md`, `CLAUDE.md`; imports Cursor/Windsurf rules in Terminal | Devin for Terminal skills as `/skill-name` | `.devin/hooks.v1.json`, config hooks | `.devin/config.json` MCP, permissions, imports |
| Codex | No verified committed Codex-specific subagent-profile format | Codex `SKILL.md` folders | `AGENTS.md`, nested `AGENTS.md`, fallback filenames | No verified committed Codex-specific slash-command file format | notification hook in config | MCP servers, connector apps |

## Equivalent Variants

These vendor surfaces are not identical, but they are close enough that adapters
can project the same canonical concept into them.

### Always-On Project Instructions

Canonical concept: repository-wide instruction context.

Equivalent surfaces:

- `AGENTS.md`: Codex, OpenCode, Windsurf, Devin, Copilot agent instructions,
  Cursor simple alternative.
- `CLAUDE.md` or `.claude/CLAUDE.md`: Claude Code project instructions;
  OpenCode and Devin for Terminal compatibility fallback.
- `.github/copilot-instructions.md`: Copilot repository-wide instructions.
- `.cursor/rules/*.mdc` with `alwaysApply: true`: Cursor always-on project rule.
- `.windsurf/rules/*.md` with `trigger: always_on`: Windsurf always-on rule.

### Path-Scoped Instructions

Canonical concept: guidance that applies only to matching files or subtrees.

Equivalent surfaces:

- Nested `AGENTS.md`: Codex, OpenCode, Windsurf, Devin, and Copilot agent
  instruction contexts where supported.
- `.claude/rules/*.md` with `paths`: Claude Code.
- `.github/instructions/**/*.instructions.md` with `applyTo`: Copilot.
- `.cursor/rules/*.mdc` with `globs`: Cursor.
- `.windsurf/rules/*.md` with `trigger: glob` and `globs`: Windsurf.

### Model-Selected Rules or Skills

Canonical concept: guidance available to the model when it decides the task
matches.

Equivalent surfaces:

- `.claude/skills/<skill>/SKILL.md`: Claude Code skills.
- `.github/skills/<skill>/SKILL.md`, `.claude/skills/<skill>/SKILL.md`, or
  `.agents/skills/<skill>/SKILL.md`: GitHub Copilot agent skills.
- `.opencode/skills/<skill>/SKILL.md`, `.claude/skills/<skill>/SKILL.md`, or
  `.agents/skills/<skill>/SKILL.md`: OpenCode agent skills.
- `.windsurf/skills/<skill>/SKILL.md`, `.agents/skills/<skill>/SKILL.md`, or
  `.claude/skills/<skill>/SKILL.md` when enabled: Windsurf skills.
- `.agents/skills/<skill>/SKILL.md`, `.github/skills/<skill>/SKILL.md`, or
  `.claude/skills/<skill>/SKILL.md`: Devin product skills.
- `.devin/skills/<skill>/SKILL.md`: Devin for Terminal-specific skills.
- Codex skills using `SKILL.md` folders.
- `.cursor/rules/*.mdc` with description and `alwaysApply: false`: Cursor
  agent-requested rules. Cursor does not currently have a verified repo-native
  `SKILL.md` skill surface.
- `.windsurf/rules/*.md` with `trigger: model_decision`: Windsurf.
- OpenCode subagents and configured agents, when selected by description.

### Manual Workflow Prompts

Canonical concept: user-invoked repeatable workflows.

Equivalent surfaces:

- `.claude/commands/**/*.md`: Claude Code slash commands.
- `.github/prompts/**/*.prompt.md`: Copilot prompt files where supported.
- Copilot custom agents can also encode reusable task prompts in agent profiles.
- `.cursor/commands/*.md`: Cursor custom commands.
- `.opencode/commands/*.md`: OpenCode commands.
- `opencode.json` `command`: OpenCode JSON-defined commands.
- Windsurf workflows.
- Devin for Terminal skills invoked with `/skill-name`.
- Manual Cursor rules invoked with `@ruleName`.

### Specialized Agents

Canonical concept: role-specific agent behavior.

Equivalent surfaces:

- `.claude/agents/*.md`: Claude Code subagents.
- `.github/agents/*.md`: Copilot repository custom agent profiles.
- `opencode.json` `agent`: OpenCode primary and subagent configuration.
- `.opencode/agents/*.md`: OpenCode Markdown agent definitions.
- `.devin/agents/<agent-name>/AGENT.md`: Devin for Terminal custom subagents.
- `.agents/agents/<agent-name>/AGENT.md`: Devin for Terminal alternate custom
  subagent location.
- Codex and Windsurf task agents may exist as product-level concepts, but this
  project should not assume a committed repo file format unless official docs
  define one.

### Runtime Enforcement and Permissions

Canonical concept: deterministic execution control distinct from prompt policy.

Equivalent surfaces:

- `.claude/settings.json`: Claude Code permissions, hooks, sandboxing, MCP,
  environment variables.
- `.github/hooks/*.json`: GitHub Copilot hooks.
- `opencode.json`: OpenCode permissions, agents, commands, MCP, plugins, and
  instructions.
- `.opencode/plugins/`: OpenCode plugins with event hooks and custom tools.
- `.windsurf/hooks.json`: Windsurf workspace hooks.
- `.devin/hooks.v1.json` and `.devin/config*.json`: Devin for Terminal hooks.
- `.devin/config.json`: Devin for Terminal permissions, MCP, imports, and hooks.
- Codex `~/.codex/config.toml`: MCP servers, approval behavior, instruction-file
  fallback behavior, and notification hooks.
- Devin repo setup: external upkeep, lint, and test commands.

These are adapters for execution behavior. They should not redefine canonical
rules.

### Tool and Data Integrations

Canonical concept: external tools or data sources made available to the model.

Equivalent surfaces:

- Claude MCP server settings and plugins.
- Copilot MCP servers for coding agent; tool support only, not MCP prompts or
  resources.
- Cursor MCP configuration shared between editor and CLI.
- OpenCode `opencode.json` `mcp`, plugins, and `.opencode/tools/`.
- Windsurf MCP plus hooks that observe MCP usage.
- Devin for Terminal `mcpServers`.
- Codex MCP servers in `config.toml` and connector apps where available.

### Pluggable Vendor Tools

Canonical concept: a vendor-native installable or loadable bundle that can carry
multiple capabilities together, such as rules, skills, commands, agents, hooks,
tools, or integrations.

This is different from a directory of repo files. A pluggable vendor tool has a
first-class loading, installation, marketplace, package, or plugin mechanism.

Current support:

| Vendor | First-Class Plugin Mechanism | Bundleable Capabilities | Notes |
| --- | --- | --- | --- |
| Claude Code | Yes | Commands, agents, hooks, skills, MCP servers | Claude plugins are the strongest direct match for packaging this project's multi-capability output. |
| OpenCode | Yes | Plugins, event hooks, custom tools, integrations | OpenCode plugins load from `.opencode/plugins/`, global config, or npm packages. They can subscribe to events and add tools. |
| GitHub Copilot | Partial | CLI plugins, custom agents, skills, hooks, MCP | Copilot has plugin concepts in CLI docs and separate first-class surfaces, but this project should verify exact packaging rules before treating it as one unified repo plugin target. |
| Windsurf | Partial | Skills, workflows, rules, hooks; enterprise system-level deployment | Windsurf has several loadable customization surfaces, but current docs do not show a single general-purpose plugin package format comparable to Claude or OpenCode. |
| Devin for Terminal | Partial | Rules, skills, subagents, hooks, MCP, imported vendor config | Devin has a project `.devin/` extensibility directory and imports other vendors' config, but current docs do not show a separate plugin package mechanism. |
| Cursor | No verified first-class plugin bundle for agent capabilities | Rules, commands, MCP, modes | Cursor supports useful customization files, but no verified repo-native plugin package surface for bundling rules, skills, hooks, and agents together. |
| Codex | Partial | Skills, MCP servers, connector apps, config | Codex supports skills and connector apps, but no verified repo-committed plugin package that bundles rules, skills, commands, hooks, and agents together. |
| Devin product | No verified committed plugin package | AGENTS.md, skills, external repo setup | Most rich extensibility appears in Devin for Terminal or external setup. |

Adapter guidance:

- Treat Claude Code and OpenCode as first-class plugin-package targets.
- Treat Copilot, Windsurf, Devin for Terminal, and Codex as bundle candidates only
  after verifying the exact install and packaging mechanics for the target
  surface.
- Treat Cursor and Devin product as file-set or setup adapters unless official
  plugin-package support is verified.
- Do not confuse MCP servers with vendor plugins. MCP adds tools and data access;
  a vendor plugin may bundle MCP with instructions, hooks, skills, commands, or
  other vendor-native behavior.
- Do not confuse skills with vendor plugins. Skills are reusable procedures; a
  plugin package may contain multiple skills plus other capabilities.

### Compatibility Imports

Canonical concept: one vendor reading another vendor's configuration format.

Equivalent surfaces:

- Claude can import files from `CLAUDE.md` using `@path`.
- OpenCode reads `AGENTS.md` or falls back to `CLAUDE.md`; it can also read some
  Claude Code skill locations unless disabled.
- Windsurf discovers `.agents/skills/` and optionally `.claude/skills/`.
- Devin for Terminal imports Cursor rules, Windsurf rules, and Claude Code
  commands, subagents, and hooks when enabled.
- Copilot skills can live in `.github/skills/`, `.claude/skills/`, or
  `.agents/skills/`.
- Codex can use configured fallback instruction filenames.

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

## Common Rich Profile

The common rich profile is the practical target for this project's first-class
adapters. It represents the strongest emerging shared model across the vendors
that support more than plain instruction files.

This profile intentionally excludes vendors or product surfaces that do not yet
support the emerging common set. Those vendors should receive a compact or
degraded adapter instead of forcing the canonical model down to their current
limits.

The common rich profile includes:

- Always-on project instructions.
- Path-scoped or directory-scoped rules.
- Model-selected skills using `SKILL.md` or an equivalent progressively loaded
  mechanism.
- Manual workflow prompts, slash commands, or command-like workflows.
- MCP or equivalent external tool configuration.
- Runtime permissions, approval policy, or execution constraints.
- Event hooks, lifecycle hooks, or plugin event subscriptions.
- Optional specialized agents or subagents where the vendor supports them.

The common rich profile does not require:

- A committed custom-agent profile format.
- Vendor plugin systems.
- First-class plugin-package mechanisms.
- Custom model-callable tools.
- Cross-vendor config imports.
- External repo setup fields.
- Non-durable memory systems.
- Vendor-specific enterprise deployment surfaces.

Current fit:

| Vendor | Fit | Notes |
| --- | --- | --- |
| Claude Code | Full | Supports rules, skills, commands, agents, settings, hooks, MCP, and plugins. |
| GitHub Copilot | Full | Supports instructions, path instructions, skills, custom agents, prompts, hooks, and MCP tools. |
| OpenCode | Full | Supports rules, skills, commands, agents, permissions, MCP, plugins, hooks, and custom tools. |
| Windsurf | Full except committed custom agents | Supports rules, skills, workflows, hooks, MCP, and AGENTS.md. |
| Devin for Terminal | Full | Supports rules, skills, custom subagents, MCP, permissions, hooks, and imports. |
| Codex | Partial | Supports AGENTS.md, skills, MCP, config, connector apps, and notification hooks, but no verified committed slash-command or custom-agent profile format. |
| Cursor | Partial | Supports rules, commands, AGENTS/CLAUDE in CLI, custom modes, and MCP, but no verified repo-native `SKILL.md` skills or event hooks. |
| Devin product | Partial | Supports AGENTS.md, skills, and external repo setup, but most rich configuration is in Devin for Terminal. |

Adapter guidance:

- Use the common rich profile as the default target for canonical schema design.
- Generate rich adapters for full-fit vendors.
- Generate hybrid adapters for partial-fit vendors by mapping missing skills or
  hooks to the closest supported rule, command, or compact instruction surface.
- Do not let partial-fit vendors define the canonical model.
- Re-check this profile whenever a partial-fit vendor adds native skills, hooks,
  custom agents, or command files.

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
- Short workflow pointers that describe what to do, without assuming slash-command
  or skill invocation.
- Pointers to canonical docs for details.

`AGENTS.md` is the closest portable committed baseline across Codex, OpenCode,
Windsurf, Devin, Cursor, and Copilot agent-instruction contexts. Claude Code
uses `CLAUDE.md` or `.claude/CLAUDE.md` as its native project instruction file,
so a Claude adapter should provide `CLAUDE.md` that imports `AGENTS.md`.

For Copilot, keep `.github/copilot-instructions.md` as a compact repository-wide
projection because Copilot support for `AGENTS.md` varies by surface. For Cursor
and Windsurf, `AGENTS.md` is usable, but richer rule files are preferred when the
adapter can generate them.

The lowest common denominator does not include:

- Path-scoped frontmatter.
- Automatic skill discovery.
- Slash commands.
- Subagents.
- Hooks.
- Custom agents.
- Custom model-callable tools.
- MCP server configuration.
- Vendor-specific plugin systems.
- First-class plugin-package mechanisms.
- Cross-vendor config import behavior.
- Non-durable memory systems.
- Skill permissions, model overrides, or trigger controls.
- Runtime permission enforcement.
- External repo setup fields.

Adapters must not flatten the canonical model to this lowest common denominator.
Use it only as the fallback output for vendors or contexts that cannot consume a
richer structure.
