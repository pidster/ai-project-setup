# Adapters

Adapters render canonical content from `core/` into vendor-specific outputs.

Adapters may handle:

- file naming
- file placement
- frontmatter
- globs and path scoping
- compact summaries
- invocation hints
- runtime caveats

Adapters must not redefine canonical policy.

Implemented renderer entry points:

- `python3 adapters/codex/render.py`
- `python3 adapters/cursor/render.py`
- `python3 adapters/opencode/render.py`

Run `python3 core/skills/tools/adapter_validation.py` to check adapter
policy-drift guardrails, and `python3 core/skills/tools/generated_validation.py`
to check that generated outputs and the generated-output manifest are up to
date.
