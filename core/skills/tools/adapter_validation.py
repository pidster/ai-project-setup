#!/usr/bin/env python3
"""Validate adapter and generated-output policy-drift guardrails."""

from __future__ import annotations

from pathlib import Path
import sys
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
CANONICAL_ROOTS = (
    REPO_ROOT / "core" / "rules" / "atomic",
    REPO_ROOT / "core" / "rules" / "languages",
    REPO_ROOT / "core" / "rules" / "compositional",
    REPO_ROOT / "core" / "skills" / "atomic",
    REPO_ROOT / "core" / "skills" / "tools",
    REPO_ROOT / "core" / "skills" / "compositional",
)

IMPLEMENTED_RENDERERS = {
    "claude": {
        "renderer": REPO_ROOT / "adapters" / "claude" / "render.py",
        "outputs": [],
    },
    "codex": {
        "renderer": REPO_ROOT / "adapters" / "codex" / "render.py",
        "outputs": [],
    },
    "cursor": {
        "renderer": REPO_ROOT / "adapters" / "cursor" / "render.py",
        "outputs": [
            {
                "path": REPO_ROOT
                / "dist"
                / "cursor"
                / "repo-files"
                / ".cursor"
                / "rules"
                / "canonical-guidance.mdc",
                "source_ids": "all",
            }
        ],
    },
    "devin": {
        "renderer": REPO_ROOT / "adapters" / "devin" / "render.py",
        "outputs": [],
    },
    "opencode": {
        "renderer": REPO_ROOT / "adapters" / "opencode" / "render.py",
        "outputs": [],
    },
    "copilot": {
        "renderer": REPO_ROOT / "adapters" / "copilot" / "render.py",
        "outputs": [],
    },
    "windsurf": {
        "renderer": REPO_ROOT / "adapters" / "windsurf" / "render.py",
        "outputs": [],
    },
}


def rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if value == "[]":
        return []
    if value == "{}":
        return {}
    if value in {"true", "false"}:
        return value == "true"
    return value.strip('"').strip("'")


def parse_frontmatter(path: Path) -> dict[str, Any]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{rel(path)}: missing frontmatter")
    closing_index = lines[1:].index("---") + 1

    metadata: dict[str, Any] = {}
    current_key: str | None = None
    for line in lines[1:closing_index]:
        if not line.strip():
            continue
        if line.startswith("  - "):
            if current_key is None:
                raise ValueError(f"{rel(path)}: list item without key")
            metadata.setdefault(current_key, []).append(parse_scalar(line[4:]))
            continue
        key, raw_value = line.split(":", 1)
        current_key = key.strip()
        raw_value = raw_value.strip()
        metadata[current_key] = [] if not raw_value else parse_scalar(raw_value)
    return metadata


def canonical_id_map() -> dict[str, dict[str, Any]]:
    items: dict[str, dict[str, Any]] = {}
    for root in CANONICAL_ROOTS:
        for path in sorted(root.glob("*.md")):
            if path.is_file():
                metadata = parse_frontmatter(path)
                items[str(metadata["id"])] = metadata
    return items


def skill_name(item_id: str) -> str:
    return item_id.rsplit(".", 1)[-1]


def append_skill_outputs(
    outputs: list[dict[str, Any]],
    source_items: dict[str, dict[str, Any]],
    output_root: Path,
) -> None:
    for item_id, metadata in sorted(source_items.items()):
        if metadata.get("kind") == "skill":
            outputs.append(
                {
                    "path": output_root / skill_name(item_id) / "SKILL.md",
                    "source_ids": [item_id],
                }
            )


def append_workflow_outputs(
    outputs: list[dict[str, Any]],
    source_items: dict[str, dict[str, Any]],
    output_root: Path,
) -> None:
    for item_id, metadata in sorted(source_items.items()):
        if metadata.get("kind") == "skill" and metadata.get("scope") == "compositional":
            outputs.append(
                {
                    "path": output_root / f"{skill_name(item_id)}.md",
                    "source_ids": [item_id],
                }
            )


def populate_dynamic_outputs(source_items: dict[str, dict[str, Any]]) -> None:
    rule_ids = [
        item_id
        for item_id, metadata in sorted(source_items.items())
        if metadata.get("kind") == "rule"
    ]

    claude_outputs = IMPLEMENTED_RENDERERS["claude"]["outputs"]
    claude_outputs.clear()
    append_skill_outputs(
        claude_outputs,
        source_items,
        REPO_ROOT
        / "dist"
        / "claude"
        / "marketplace"
        / "plugins"
        / "ai-project-setup"
        / "skills",
    )

    codex_outputs = IMPLEMENTED_RENDERERS["codex"]["outputs"]
    codex_outputs.clear()
    append_skill_outputs(
        codex_outputs,
        source_items,
        REPO_ROOT
        / "dist"
        / "codex"
        / "marketplace"
        / "plugins"
        / "ai-project-setup"
        / "skills",
    )

    copilot_outputs = IMPLEMENTED_RENDERERS["copilot"]["outputs"]
    copilot_outputs.clear()
    copilot_outputs.append(
        {
            "path": REPO_ROOT
            / "dist"
            / "copilot"
            / "repo-files"
            / ".github"
            / "copilot-instructions.md",
            "source_ids": rule_ids,
        }
    )
    append_skill_outputs(
        copilot_outputs,
        source_items,
        REPO_ROOT / "dist" / "copilot" / "repo-files" / ".github" / "skills",
    )

    opencode_outputs = IMPLEMENTED_RENDERERS["opencode"]["outputs"]
    opencode_outputs.clear()
    opencode_outputs.append(
        {
            "path": REPO_ROOT / "dist" / "opencode" / "repo-files" / "AGENTS.md",
            "source_ids": rule_ids,
        }
    )
    append_skill_outputs(
        opencode_outputs,
        source_items,
        REPO_ROOT / "dist" / "opencode" / "repo-files" / ".opencode" / "skills",
    )

    devin_outputs = IMPLEMENTED_RENDERERS["devin"]["outputs"]
    devin_outputs.clear()
    devin_outputs.extend(
        [
            {
                "path": REPO_ROOT / "dist" / "devin" / "repo-files" / "AGENTS.md",
                "source_ids": "all",
            },
            {
                "path": REPO_ROOT
                / "dist"
                / "devin"
                / "repo-files"
                / ".devin"
                / "config.json",
                "source_ids": "all",
            },
            {
                "path": REPO_ROOT
                / "dist"
                / "devin"
                / "repo-files"
                / ".devin"
                / "agents"
                / "canonical-guidance"
                / "AGENT.md",
                "source_ids": "all",
            },
            {
                "path": REPO_ROOT
                / "dist"
                / "devin"
                / "repo-files"
                / ".devin"
                / "hooks.v1.json",
                "source_ids": [],
            },
        ]
    )
    append_skill_outputs(
        devin_outputs,
        source_items,
        REPO_ROOT / "dist" / "devin" / "repo-files" / ".agents" / "skills",
    )
    append_skill_outputs(
        devin_outputs,
        source_items,
        REPO_ROOT / "dist" / "devin" / "repo-files" / ".devin" / "skills",
    )

    windsurf_outputs = IMPLEMENTED_RENDERERS["windsurf"]["outputs"]
    windsurf_outputs.clear()
    windsurf_outputs.extend(
        [
            {
                "path": REPO_ROOT / "dist" / "windsurf" / "repo-files" / "AGENTS.md",
                "source_ids": "all",
            },
            {
                "path": REPO_ROOT
                / "dist"
                / "windsurf"
                / "repo-files"
                / ".windsurf"
                / "rules"
                / "canonical-rules.md",
                "source_ids": rule_ids,
            },
            {
                "path": REPO_ROOT
                / "dist"
                / "windsurf"
                / "repo-files"
                / ".windsurf"
                / "hooks.json",
                "source_ids": [],
            },
        ]
    )
    append_skill_outputs(
        windsurf_outputs,
        source_items,
        REPO_ROOT / "dist" / "windsurf" / "repo-files" / ".windsurf" / "skills",
    )
    append_workflow_outputs(
        windsurf_outputs,
        source_items,
        REPO_ROOT / "dist" / "windsurf" / "repo-files" / ".windsurf" / "workflows",
    )


def vendor_dirs() -> set[str]:
    vendors_root = REPO_ROOT / "vendors"
    return {
        path.parent.name
        for path in vendors_root.glob("*/capabilities.yaml")
        if path.is_file()
    }


def validate_renderer_registry(errors: list[str]) -> None:
    vendors = vendor_dirs()
    for vendor, registration in sorted(IMPLEMENTED_RENDERERS.items()):
        if vendor not in vendors:
            errors.append(f"adapters/{vendor}: implemented renderer has no vendor capability file")

        renderer = registration["renderer"]
        if not isinstance(renderer, Path) or not renderer.exists():
            errors.append(f"adapters/{vendor}: missing renderer {rel(renderer)}")
        elif renderer.parent != REPO_ROOT / "adapters" / vendor:
            errors.append(f"{rel(renderer)}: renderer must live under adapters/{vendor}/")

        outputs = registration["outputs"]
        if not isinstance(outputs, list) or not outputs:
            errors.append(f"adapters/{vendor}: renderer must declare at least one output")
            continue
        for output_registration in outputs:
            if not isinstance(output_registration, dict):
                errors.append(f"adapters/{vendor}: output registration must be a map")
                continue
            output = output_registration.get("path")
            if not isinstance(output, Path):
                errors.append(f"adapters/{vendor}: output registration path must be a path")
                continue
            expected_root = REPO_ROOT / "dist" / vendor
            if expected_root not in output.parents and output != expected_root:
                errors.append(f"{rel(output)}: generated output must live under dist/{vendor}/")
            source_ids = output_registration.get("source_ids")
            if source_ids != "all" and not isinstance(source_ids, list):
                errors.append(f"{rel(output)}: output registration must declare source IDs")


def validate_generated_outputs(source_ids: list[str], errors: list[str]) -> None:
    for vendor, registration in sorted(IMPLEMENTED_RENDERERS.items()):
        for output_registration in registration["outputs"]:
            output = output_registration["path"]
            if not output.exists():
                errors.append(f"{rel(output)}: missing generated output")
                continue
            text = output.read_text(encoding="utf-8")
            if "Generated by adapters/" not in text or "Do not edit directly" not in text:
                errors.append(f"{rel(output)}: missing generated-file marker")
            if "Canonical policy and procedure remain in `core/`." not in text:
                errors.append(f"{rel(output)}: missing canonical-boundary notice")
            expected_ids = (
                source_ids
                if output_registration["source_ids"] == "all"
                else output_registration["source_ids"]
            )
            missing_ids = [item_id for item_id in expected_ids if f"`{item_id}`" not in text]
            if missing_ids:
                errors.append(
                    f"{rel(output)}: missing canonical source IDs: {', '.join(missing_ids)}"
                )


def main() -> int:
    errors: list[str] = []

    try:
        source_items = canonical_id_map()
        source_ids = sorted(source_items)
        populate_dynamic_outputs(source_items)
    except (OSError, ValueError) as exc:
        errors.append(str(exc))
        source_ids = []

    validate_renderer_registry(errors)
    validate_generated_outputs(source_ids, errors)

    if errors:
        print("adapter validation failed", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"adapter validation passed ({len(IMPLEMENTED_RENDERERS)} renderers)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
