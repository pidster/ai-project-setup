#!/usr/bin/env python3
"""Generate or validate vendor install manifests."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
VENDORS_ROOT = REPO_ROOT / "vendors"
DIST_ROOT = REPO_ROOT / "dist"
RENDERER = "core/skills/tools/install_manifest.py"
DELIVERABLE_ORDER = ("marketplace", "plugin", "repo_files")
DELIVERABLE_DIRS = {
    "marketplace": "marketplace",
    "plugin": "plugin",
    "repo_files": "repo-files",
}
WRITE_ACTIONS = {"copy_file", "copy_tree", "merge_structured_file"}
NON_EXECUTED_ACTIONS = {"external_package", "manual_step"}
ACTION_TYPES = WRITE_ACTIONS | NON_EXECUTED_ACTIONS


@dataclass(frozen=True)
class Action:
    action_type: str
    fields: dict[str, Any]


@dataclass(frozen=True)
class Distribution:
    distribution_type: str
    artifact: str
    installable_by_cli: bool
    rationale: str
    actions: list[Action]


@dataclass(frozen=True)
class Manifest:
    vendor: str
    display_name: str
    last_reviewed: str
    confidence: str
    plugin_model: str
    distribution: Distribution
    sources: list[str]


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

        data[key] = [] if not raw_value else parse_scalar(raw_value)

    return data


def quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def is_relative_safe(path: str) -> bool:
    candidate = Path(path)
    if not path or candidate.is_absolute():
        return False
    if any(part in {"", ".", ".."} for part in candidate.parts):
        return False
    return True


def vendor_names() -> list[str]:
    return sorted(path.parent.name for path in VENDORS_ROOT.glob("*/plugin-model.yaml"))


def read_plugin_model(vendor: str) -> dict[str, Any]:
    path = VENDORS_ROOT / vendor / "plugin-model.yaml"
    return parse_yaml_subset(path.read_text(encoding="utf-8"), path)


def vendor_supports_deliverable(plugin_model: dict[str, Any], deliverable_type: str) -> bool:
    if deliverable_type == "marketplace":
        return bool(plugin_model.get("marketplace_surfaces", []))
    if deliverable_type == "plugin":
        return plugin_model.get("plugin_model") in {"package_manifest", "module_plugin"} and bool(
            plugin_model.get("plugin_config_surfaces", [])
        )
    if deliverable_type == "repo_files":
        return bool(plugin_model.get("direct_config_surfaces", []))
    raise ValueError(f"unknown deliverable type: {deliverable_type}")


def artifact_root(vendor: str, deliverable_type: str) -> Path:
    return DIST_ROOT / vendor / DELIVERABLE_DIRS[deliverable_type]


def artifact_exists(vendor: str, deliverable_type: str) -> bool:
    root = artifact_root(vendor, deliverable_type)
    if not root.exists():
        return False
    return any(path.is_file() and path.name != ".gitkeep" for path in root.rglob("*"))


def generated_repo_files(vendor: str) -> list[Path]:
    root = artifact_root(vendor, "repo_files")
    files: list[Path] = []
    if not root.exists():
        return files
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.name != ".gitkeep":
            files.append(path)
    return files


def repo_file_actions(vendor: str) -> list[Action]:
    actions: list[Action] = []
    vendor_root = artifact_root(vendor, "repo_files")
    for source in generated_repo_files(vendor):
        target = str(source.relative_to(vendor_root))
        actions.append(
            Action(
                action_type="copy_file",
                fields={
                    "source": rel(source),
                    "target": target,
                    "on_conflict": "fail",
                },
            )
        )
    return actions


def plugin_package_root(vendor: str) -> Path:
    root = artifact_root(vendor, "plugin")
    children = [path for path in sorted(root.iterdir()) if path.is_dir()] if root.exists() else []
    if len(children) == 1:
        return children[0]
    return root


def manual_actions(vendor: str, deliverable_type: str) -> list[Action]:
    root = artifact_root(vendor, deliverable_type)
    if vendor == "claude" and deliverable_type == "plugin":
        package_root = plugin_package_root(vendor)
        return [
            Action(
                action_type="manual_step",
                fields={
                    "summary": "Load or publish the generated Claude Code plugin package.",
                    "instructions": (
                        f"Use {rel(package_root)} with Claude Code plugin development "
                        "or marketplace tooling, such as claude --plugin-dir, then "
                        "enable the plugin in Claude Code."
                    ),
                },
            )
        ]
    return [
        Action(
            action_type="manual_step",
            fields={
                "summary": f"Install the generated {deliverable_type} artifact using vendor tooling.",
                "instructions": (
                    f"Review {rel(root)} and use the vendor's documented plugin, "
                    "module, or marketplace installation flow."
                ),
            },
        )
    ]


def selection_rationale(vendor: str, plugin_model: dict[str, Any], selected: str) -> str:
    unavailable: list[str] = []
    for deliverable_type in DELIVERABLE_ORDER:
        if deliverable_type == selected:
            break
        if not vendor_supports_deliverable(plugin_model, deliverable_type):
            unavailable.append(f"{deliverable_type} is not a verified vendor surface")
        elif not artifact_exists(vendor, deliverable_type):
            unavailable.append(f"{deliverable_type} artifact is not generated")
    if unavailable:
        return f"Selected {selected}; higher-priority surfaces skipped because " + "; ".join(unavailable) + "."
    return f"Selected {selected} as the best generated deliverable for this vendor."


def select_distribution(vendor: str, plugin_model: dict[str, Any]) -> Distribution:
    for deliverable_type in DELIVERABLE_ORDER:
        if vendor_supports_deliverable(plugin_model, deliverable_type) and artifact_exists(vendor, deliverable_type):
            if deliverable_type == "repo_files":
                return Distribution(
                    distribution_type=deliverable_type,
                    artifact=rel(artifact_root(vendor, deliverable_type)),
                    installable_by_cli=True,
                    rationale=selection_rationale(vendor, plugin_model, deliverable_type),
                    actions=repo_file_actions(vendor),
                )
            root = plugin_package_root(vendor) if deliverable_type == "plugin" else artifact_root(vendor, deliverable_type)
            return Distribution(
                distribution_type=deliverable_type,
                artifact=rel(root),
                installable_by_cli=False,
                rationale=selection_rationale(vendor, plugin_model, deliverable_type),
                actions=manual_actions(vendor, deliverable_type),
            )
    return Distribution(
        distribution_type="none",
        artifact="none",
        installable_by_cli=False,
        rationale="No supported generated distribution artifact exists for this vendor.",
        actions=[],
    )


def build_manifest(vendor: str) -> Manifest:
    plugin_model = read_plugin_model(vendor)
    return Manifest(
        vendor=vendor,
        display_name=str(plugin_model.get("display_name", vendor)),
        last_reviewed=str(plugin_model.get("last_reviewed", "")),
        confidence=str(plugin_model.get("confidence", "")),
        plugin_model=str(plugin_model.get("plugin_model", "")),
        distribution=select_distribution(vendor, plugin_model),
        sources=[str(source) for source in plugin_model.get("sources", [])],
    )


def render_action(action: Action) -> list[str]:
    lines = [f"  - type: {action.action_type}"]
    for key, value in action.fields.items():
        lines.append(f"    {key}: {quote(str(value))}")
    return lines


def render_manifest(manifest: Manifest) -> str:
    distribution = manifest.distribution
    lines = [
        f"# Generated by {RENDERER}. Do not edit directly.",
        f"vendor: {manifest.vendor}",
        f"display_name: {quote(manifest.display_name)}",
        f"generated_by: {RENDERER}",
        "source_files:",
        f"  capabilities: vendors/{manifest.vendor}/capabilities.yaml",
        f"  plugin_model: vendors/{manifest.vendor}/plugin-model.yaml",
        "review:",
        f"  last_reviewed: {manifest.last_reviewed}",
        f"  confidence: {manifest.confidence}",
        "plugin_model:",
        f"  category: {manifest.plugin_model}",
        "distribution:",
        f"  type: {distribution.distribution_type}",
        f"  artifact: {quote(distribution.artifact)}",
        f"  installable_by_cli: {bool_text(distribution.installable_by_cli)}",
        f"  rationale: {quote(distribution.rationale)}",
        "actions:",
    ]
    if distribution.actions:
        for action in distribution.actions:
            lines.extend(render_action(action))
    else:
        lines.append("  - none")
    lines.append("sources:")
    for source in manifest.sources:
        lines.append(f"  - {source}")
    return "\n".join(lines).rstrip() + "\n"


def manifest_path(vendor: str) -> Path:
    return DIST_ROOT / vendor / "install-manifest.yaml"


def validate_action(vendor: str, action: Action, errors: list[str]) -> None:
    if action.action_type not in ACTION_TYPES:
        errors.append(f"{vendor}: unknown action type {action.action_type}")
        return

    if action.action_type in WRITE_ACTIONS:
        source = action.fields.get("source")
        target = action.fields.get("target")
        if not isinstance(source, str) or not (REPO_ROOT / source).exists():
            errors.append(f"{vendor}: action source missing: {source}")
        if not isinstance(target, str) or not is_relative_safe(target):
            errors.append(f"{vendor}: unsafe action target: {target}")
        if action.fields.get("on_conflict") != "fail":
            errors.append(f"{vendor}: write actions must default on_conflict to fail")
    elif action.action_type == "manual_step":
        for field in ("summary", "instructions"):
            value = action.fields.get(field)
            if not isinstance(value, str) or not value:
                errors.append(f"{vendor}: manual_step missing {field}")
    elif action.action_type == "external_package":
        for field in ("surface", "package", "version", "manual"):
            value = action.fields.get(field)
            if not isinstance(value, str) or not value:
                errors.append(f"{vendor}: external_package missing {field}")


def generated_artifact_dirs(vendor: str) -> list[str]:
    return [
        deliverable_type
        for deliverable_type in DELIVERABLE_ORDER
        if artifact_exists(vendor, deliverable_type)
    ]


def validate_manifest(manifest: Manifest, errors: list[str]) -> None:
    if not (VENDORS_ROOT / manifest.vendor / "capabilities.yaml").exists():
        errors.append(f"{manifest.vendor}: missing capability source")
    if not (VENDORS_ROOT / manifest.vendor / "plugin-model.yaml").exists():
        errors.append(f"{manifest.vendor}: missing plugin model source")

    plugin_model = read_plugin_model(manifest.vendor)
    selected = select_distribution(manifest.vendor, plugin_model)
    if manifest.distribution != selected:
        errors.append(f"{manifest.vendor}: selected distribution does not match generated artifacts")

    if manifest.distribution.distribution_type != "none":
        if not vendor_supports_deliverable(plugin_model, manifest.distribution.distribution_type):
            errors.append(f"{manifest.vendor}: selected distribution is not vendor-supported")
        if not artifact_exists(manifest.vendor, manifest.distribution.distribution_type):
            errors.append(f"{manifest.vendor}: selected distribution artifact is missing")
    if manifest.distribution.installable_by_cli and not manifest.distribution.actions:
        errors.append(f"{manifest.vendor}: installable distribution has no actions")
    if manifest.distribution.distribution_type != "repo_files" and manifest.distribution.installable_by_cli:
        errors.append(f"{manifest.vendor}: non-repo distribution must not be CLI-installable yet")

    for action in manifest.distribution.actions:
        validate_action(manifest.vendor, action, errors)


def validate_vendor_dist_layout(vendor: str, errors: list[str]) -> None:
    root = DIST_ROOT / vendor
    if not root.exists():
        errors.append(f"{vendor}: missing dist directory")
        return

    allowed_dirs = set(DELIVERABLE_DIRS.values())
    for path in sorted(root.iterdir()):
        if path.name == "install-manifest.yaml":
            continue
        if path.is_dir() and path.name in allowed_dirs:
            continue
        errors.append(
            f"{rel(path)}: vendor dist entries must be install-manifest.yaml "
            "or the single selected artifact directory"
        )

    artifacts = generated_artifact_dirs(vendor)
    if len(artifacts) != 1:
        errors.append(f"{vendor}: expected exactly one generated distribution artifact, found {artifacts}")


def validate_all(manifests: list[Manifest]) -> list[str]:
    errors: list[str] = []
    vendors = set(vendor_names())
    manifest_vendors = {manifest.vendor for manifest in manifests}
    for vendor in sorted(vendors - manifest_vendors):
        errors.append(f"{vendor}: missing generated install manifest model")
    for manifest in manifests:
        validate_vendor_dist_layout(manifest.vendor, errors)
        validate_manifest(manifest, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="check install manifest freshness")
    args = parser.parse_args()

    manifests = [build_manifest(vendor) for vendor in vendor_names()]
    errors = validate_all(manifests)
    if errors:
        print("install manifest validation failed", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    rendered = {manifest_path(manifest.vendor): render_manifest(manifest) for manifest in manifests}

    if args.check:
        stale: list[str] = []
        for path, expected in sorted(rendered.items()):
            if not path.exists():
                stale.append(f"{rel(path)}: missing install manifest")
                continue
            if path.read_text(encoding="utf-8") != expected:
                stale.append(f"{rel(path)}: install manifest is stale")
        if stale:
            for error in stale:
                print(error, file=sys.stderr)
            return 1
        print("install manifests are up to date")
        return 0

    for path, content in sorted(rendered.items()):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
