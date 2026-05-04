# Claude Adapter

Renders canonical content into a Claude Code marketplace package.

Current outputs:

- `dist/claude/marketplace/.claude-plugin/marketplace.json`
- `dist/claude/marketplace/plugins/ai-project-setup/.claude-plugin/plugin.json`
- `dist/claude/marketplace/plugins/ai-project-setup/skills/*/SKILL.md`

Native install commands:

```sh
claude plugin marketplace add https://raw.githubusercontent.com/pidster/ai-project-setup/main/dist/claude/marketplace/.claude-plugin/marketplace.json
claude plugin install ai-project-setup@ai-project-setup
```

Run:

```sh
python3 adapters/claude/render.py
```

Check freshness:

```sh
python3 adapters/claude/render.py --check
```

Future plugin output may include `commands/`, `agents/`, and plugin hooks.
