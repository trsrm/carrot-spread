#!/usr/bin/env python3
"""Validate required YAML frontmatter fields in canonical Markdown notes."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FIELDS = [
    "id",
    "type",
    "domain",
    "status",
    "source",
    "confidence",
    "sensitivity",
    "created",
    "updated",
    "tags",
    "related",
]

PROVENANCE_REQUIRED_FIELDS = [
    "origin",
    "origin_note",
]

PROVENANCE_REQUIRED_PREFIXES = (
    "10-notes/",
    "20-knowledge/",
)

CANONICAL_PREFIXES = (
    "10-notes/",
    "20-knowledge/",
    "30-projects/",
)

SKIP_NAMES = {"README.md"}
SKIP_PREFIXES = (
    "00-inbox/",
    "30-projects/_template/",
    "_archive/",
    ".generated/",
    "_templates/",
    ".scripts/",
)


def relpath(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def should_check(path: Path) -> bool:
    rel = relpath(path)
    if path.name in SKIP_NAMES:
        return False
    if any(rel.startswith(prefix) for prefix in SKIP_PREFIXES):
        return False
    return any(rel.startswith(prefix) for prefix in CANONICAL_PREFIXES)


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    try:
        _, block, _ = text.split("---", 2)
    except ValueError:
        return None
    fields: dict[str, str] = {}
    for raw_line in block.splitlines():
        if not raw_line.strip() or raw_line.startswith(" ") or raw_line.startswith("-"):
            continue
        if ":" in raw_line:
            key, value = raw_line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def main() -> int:
    failures: list[str] = []
    checked = 0

    for path in sorted(ROOT.rglob("*.md")):
        if not should_check(path):
            continue
        checked += 1
        rel = relpath(path)
        fields = parse_frontmatter(path.read_text(encoding="utf-8"))
        if fields is None:
            failures.append(f"{rel}: missing frontmatter")
            continue
        required_fields = list(REQUIRED_FIELDS)
        if any(rel.startswith(prefix) for prefix in PROVENANCE_REQUIRED_PREFIXES):
            required_fields.extend(PROVENANCE_REQUIRED_FIELDS)
        missing = [field for field in required_fields if field not in fields]
        if missing:
            failures.append(f"{rel}: missing fields: {', '.join(missing)}")

    print(f"checked={checked}")
    if failures:
        print("frontmatter_errors:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("frontmatter_ok=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
