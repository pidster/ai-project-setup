#!/usr/bin/env python3
"""Validate canonical rule and skill metadata.

This first validator intentionally uses only the Python standard library so it
can run before the repository has packaging or dependency-management tooling.
It parses the limited YAML frontmatter shape used by current canonical items.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
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

ID_RE = re.compile(r"^(rule|skill)\.[a-z0-9-]+(\.[a-z0-9-]+)+$")
KINDS = {"rule", "skill"}
SCOPES = {"atomic", "compositional"}
CATEGORIES = {"domain", "language", "tool", "workflow", "policy"}
LIST_FIELDS = {"depends_on", "extends", "commands", "optional_tools"}
REQUIRED_FIELDS = {"id", "kind", "scope", "summary"}


@dataclass(frozen=True)
class Item:
    path: Path
    metadata: dict[str, Any]

    @property
    def item_id(self) -> str:
        return str(self.metadata.get("id", ""))

    @property
    def kind(self) -> str:
        return str(self.metadata.get("kind", ""))

    @property
    def scope(self) -> str:
        return str(self.metadata.get("scope", ""))

    @property
    def category(self) -> str:
        return str(self.metadata.get("category", ""))

    @property
    def dependencies(self) -> list[str]:
        return list_values(self.metadata.get("depends_on")) + list_values(
            self.metadata.get("extends")
        )


def rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def list_values(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if value == "[]":
        return []
    if value == "{}":
        return {}
    if value in {"true", "false"}:
        return value == "true"
    return value.strip('"').strip("'")


def parse_frontmatter(text: str, path: Path) -> dict[str, Any]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{rel(path)}: missing opening frontmatter delimiter")

    try:
        closing_index = lines[1:].index("---") + 1
    except ValueError as exc:
        raise ValueError(f"{rel(path)}: missing closing frontmatter delimiter") from exc

    metadata: dict[str, Any] = {}
    current_key: str | None = None

    for number, line in enumerate(lines[1:closing_index], start=2):
        if not line.strip():
            continue
        if line.startswith("  - "):
            if current_key is None:
                raise ValueError(f"{rel(path)}:{number}: list item without a key")
            metadata.setdefault(current_key, []).append(parse_scalar(line[4:]))
            continue
        if line.startswith(" "):
            raise ValueError(f"{rel(path)}:{number}: unsupported nested frontmatter")
        if ":" not in line:
            raise ValueError(f"{rel(path)}:{number}: expected key: value")

        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        current_key = key

        if not raw_value:
            metadata[key] = []
        else:
            metadata[key] = parse_scalar(raw_value)

    return metadata


def canonical_paths() -> list[Path]:
    paths: list[Path] = []
    for root in CANONICAL_ROOTS:
        if root.exists():
            paths.extend(path for path in root.glob("*.md") if path.is_file())
    return sorted(paths)


def load_items(errors: list[str]) -> list[Item]:
    items: list[Item] = []
    for path in canonical_paths():
        try:
            metadata = parse_frontmatter(path.read_text(encoding="utf-8"), path)
        except OSError as exc:
            errors.append(f"{rel(path)}: could not read file: {exc}")
            continue
        except ValueError as exc:
            errors.append(str(exc))
            continue
        items.append(Item(path=path, metadata=metadata))
    return items


def validate_metadata(items: list[Item], errors: list[str]) -> dict[str, Item]:
    by_id: dict[str, Item] = {}
    seen_paths: dict[str, Path] = {}

    for item in items:
        path = item.path
        metadata = item.metadata
        missing = sorted(REQUIRED_FIELDS - metadata.keys())
        if missing:
            errors.append(f"{rel(path)}: missing required fields: {', '.join(missing)}")
            continue

        item_id = item.item_id
        if not ID_RE.match(item_id):
            errors.append(f"{rel(path)}: invalid id: {item_id}")
        if item.kind not in KINDS:
            errors.append(f"{rel(path)}: invalid kind: {item.kind}")
        if item.scope not in SCOPES:
            errors.append(f"{rel(path)}: invalid scope: {item.scope}")
        if item.category and item.category not in CATEGORIES:
            errors.append(f"{rel(path)}: invalid category: {item.category}")
        if not str(metadata.get("summary", "")).strip():
            errors.append(f"{rel(path)}: summary must not be empty")

        if item_id.startswith("rule.") and item.kind != "rule":
            errors.append(f"{rel(path)}: rule id must use kind: rule")
        if item_id.startswith("skill.") and item.kind != "skill":
            errors.append(f"{rel(path)}: skill id must use kind: skill")
        if "/core/rules/" in str(path) and item.kind != "rule":
            errors.append(f"{rel(path)}: files under core/rules must use kind: rule")
        if "/core/skills/" in str(path) and item.kind != "skill":
            errors.append(f"{rel(path)}: files under core/skills must use kind: skill")

        if path.parent.name == "tools":
            if item.scope != "atomic" or item.category != "tool":
                errors.append(
                    f"{rel(path)}: tool skills must use scope: atomic and category: tool"
                )

        for field in LIST_FIELDS:
            value = metadata.get(field)
            if value is None:
                continue
            if not isinstance(value, list):
                errors.append(f"{rel(path)}: {field} must be a list")
                continue
            non_strings = [entry for entry in value if not isinstance(entry, str)]
            if non_strings:
                errors.append(f"{rel(path)}: {field} entries must be strings")
            if len(value) != len(set(value)):
                errors.append(f"{rel(path)}: {field} contains duplicate entries")

        if item_id in by_id:
            first_path = seen_paths[item_id]
            errors.append(
                f"{rel(path)}: duplicate id {item_id}; first seen in {rel(first_path)}"
            )
        else:
            by_id[item_id] = item
            seen_paths[item_id] = path

    return by_id


def validate_dependencies(items: list[Item], by_id: dict[str, Item], errors: list[str]) -> None:
    for item in items:
        for dependency_id in item.dependencies:
            dependency = by_id.get(dependency_id)
            if dependency is None:
                errors.append(f"{rel(item.path)}: missing dependency: {dependency_id}")
                continue
            if item.kind == "rule" and dependency.kind == "skill":
                errors.append(
                    f"{rel(item.path)}: rules must not depend on skills: {dependency_id}"
                )
            # Workflow-to-workflow reuse is allowed for compositional skills.
            # Cycle detection below prevents recursive workflow graphs.
            if (
                item.kind == "skill"
                and item.scope == "atomic"
                and dependency.kind == "skill"
                and dependency.scope == "compositional"
            ):
                errors.append(
                    f"{rel(item.path)}: atomic skills must not depend on "
                    f"compositional skills: {dependency_id}"
                )


def validate_cycles(by_id: dict[str, Item], errors: list[str]) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()
    stack: list[str] = []

    def visit(item_id: str) -> None:
        if item_id in visited:
            return
        if item_id in visiting:
            cycle_start = stack.index(item_id)
            cycle = stack[cycle_start:] + [item_id]
            errors.append(f"dependency cycle: {' -> '.join(cycle)}")
            return

        visiting.add(item_id)
        stack.append(item_id)
        item = by_id[item_id]
        for dependency_id in item.dependencies:
            if dependency_id in by_id:
                visit(dependency_id)
        stack.pop()
        visiting.remove(item_id)
        visited.add(item_id)

    for item_id in sorted(by_id):
        visit(item_id)


def main() -> int:
    errors: list[str] = []
    items = load_items(errors)
    by_id = validate_metadata(items, errors)
    validate_dependencies(items, by_id, errors)
    validate_cycles(by_id, errors)

    if errors:
        print("canonical validation failed", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"canonical validation passed ({len(items)} items)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
