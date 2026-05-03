#!/usr/bin/env python3
"""Validate vendor capability metadata.

This validator intentionally uses only the Python standard library. It supports
the limited YAML shape currently used by vendors/*/capabilities.yaml.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
VENDORS_ROOT = REPO_ROOT / "vendors"

REQUIRED_FIELDS = {"vendor", "last_reviewed", "confidence", "sources", "supports"}
CONFIDENCE_VALUES = {"verified", "provisional", "unknown"}
SUPPORT_VALUES = {"partial", "unknown", "planned", "unsupported"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URI_RE = re.compile(r"^https?://[^\s]+$")

RENDERING_LOGIC_KEYS = {
    "adapter",
    "adapters",
    "emit",
    "generate",
    "generator",
    "renderer",
    "rendering",
    "template",
    "templates",
    "transform",
    "transforms",
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


def parse_yaml_subset(text: str, path: Path) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_key: str | None = None

    for number, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - "):
            if current_key is None:
                raise ValueError(f"{rel(path)}:{number}: list item without a key")
            data.setdefault(current_key, []).append(parse_scalar(line[4:]))
            continue
        if line.startswith("  "):
            if current_key is None or not isinstance(data.get(current_key), dict):
                raise ValueError(f"{rel(path)}:{number}: nested value without a map key")
            if ":" not in line:
                raise ValueError(f"{rel(path)}:{number}: expected nested key: value")
            key, raw_value = line.strip().split(":", 1)
            data[current_key][key.strip()] = parse_scalar(raw_value)
            continue
        if ":" not in line:
            raise ValueError(f"{rel(path)}:{number}: expected key: value")

        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        current_key = key

        if not raw_value:
            if key == "supports":
                data[key] = {}
            else:
                data[key] = []
        else:
            data[key] = parse_scalar(raw_value)

    return data


def capability_paths() -> list[Path]:
    if not VENDORS_ROOT.exists():
        return []
    return sorted(VENDORS_ROOT.glob("*/capabilities.yaml"))


def validate_capability(path: Path, data: dict[str, Any], errors: list[str]) -> None:
    missing = sorted(REQUIRED_FIELDS - data.keys())
    if missing:
        errors.append(f"{rel(path)}: missing required fields: {', '.join(missing)}")

    vendor = data.get("vendor")
    if not isinstance(vendor, str) or not vendor:
        errors.append(f"{rel(path)}: vendor must be a non-empty string")
    elif vendor != path.parent.name:
        errors.append(
            f"{rel(path)}: vendor must match directory name {path.parent.name!r}"
        )

    last_reviewed = data.get("last_reviewed")
    if not isinstance(last_reviewed, str) or not DATE_RE.match(last_reviewed):
        errors.append(f"{rel(path)}: last_reviewed must use YYYY-MM-DD")

    confidence = data.get("confidence")
    if confidence not in CONFIDENCE_VALUES:
        errors.append(
            f"{rel(path)}: confidence must be one of "
            f"{', '.join(sorted(CONFIDENCE_VALUES))}"
        )

    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append(f"{rel(path)}: sources must be a non-empty list")
    elif any(not isinstance(source, str) or not URI_RE.match(source) for source in sources):
        errors.append(f"{rel(path)}: sources entries must be http(s) URLs")

    supports = data.get("supports")
    if not isinstance(supports, dict) or not supports:
        errors.append(f"{rel(path)}: supports must be a non-empty map")
    else:
        for key, value in sorted(supports.items()):
            if not isinstance(key, str) or not key:
                errors.append(f"{rel(path)}: supports keys must be non-empty strings")
            if isinstance(value, bool):
                continue
            if isinstance(value, str) and value in SUPPORT_VALUES:
                continue
            errors.append(
                f"{rel(path)}: supports.{key} must be boolean or one of "
                f"{', '.join(sorted(SUPPORT_VALUES))}"
            )

    preferred_outputs = data.get("preferred_outputs", [])
    if not isinstance(preferred_outputs, list):
        errors.append(f"{rel(path)}: preferred_outputs must be a list")
    elif any(not isinstance(output, str) or not output for output in preferred_outputs):
        errors.append(f"{rel(path)}: preferred_outputs entries must be non-empty strings")

    notes = data.get("notes", [])
    if not isinstance(notes, list):
        errors.append(f"{rel(path)}: notes must be a list")
    elif any(not isinstance(note, str) or not note for note in notes):
        errors.append(f"{rel(path)}: notes entries must be non-empty strings")

    rendering_keys = sorted(RENDERING_LOGIC_KEYS & data.keys())
    if rendering_keys:
        errors.append(
            f"{rel(path)}: vendor capability files must not define rendering logic "
            f"keys: {', '.join(rendering_keys)}"
        )


def main() -> int:
    errors: list[str] = []
    paths = capability_paths()
    if not paths:
        errors.append("vendors: no capabilities.yaml files found")

    for path in paths:
        try:
            data = parse_yaml_subset(path.read_text(encoding="utf-8"), path)
        except OSError as exc:
            errors.append(f"{rel(path)}: could not read file: {exc}")
            continue
        except ValueError as exc:
            errors.append(str(exc))
            continue
        validate_capability(path, data, errors)

    if errors:
        print("vendor validation failed", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"vendor validation passed ({len(paths)} vendors)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
