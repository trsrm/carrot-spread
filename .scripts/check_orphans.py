#!/usr/bin/env python3
"""Identify Markdown pages with no inbound Markdown links."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / ".generated" / "orphan-pages.md"
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md)(?:#[^)]+)?\)")

SKIP_PREFIXES = (
    "00-inbox/",
    "10-source/",
    "_archive/",
    ".agents/",
    ".generated/",
    ".obsidian/",
    "_templates/",
    ".scripts/",
)


def relpath(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def should_check(path: Path) -> bool:
    rel = relpath(path)
    if path.name == "README.md" or rel == "AGENTS.md":
        return False
    return not rel.startswith(SKIP_PREFIXES)


def resolve_link(source: Path, target: str) -> str | None:
    if target.startswith(("http://", "https://", "mailto:")):
        return None
    clean = target.split("#", 1)[0]
    resolved = (source.parent / clean).resolve()
    try:
        return resolved.relative_to(ROOT).as_posix()
    except ValueError:
        return None


def main() -> int:
    pages = [path for path in sorted(ROOT.rglob("*.md")) if should_check(path)]
    inbound = {relpath(path): 0 for path in pages}

    for source in ROOT.rglob("*.md"):
        source_rel = relpath(source)
        if source_rel.startswith((".git/", ".obsidian/")):
            continue
        text = source.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            resolved = resolve_link(source, match.group(1))
            if resolved in inbound and resolved != source_rel:
                inbound[resolved] += 1

    rows = []
    today = date.today().isoformat()
    for rel, count in sorted(inbound.items()):
        if count == 0 and rel != "20-knowledge/index.md":
            rows.append(f"| {today} | [{rel}](../{rel}) | No inbound Markdown links found | Add from nearest index |")

    content = "# Orphan Pages\n\nPages with few or no backlinks.\n\n| Date | Page | Reason | Suggested link target |\n|---|---|---|---|\n" + "\n".join(rows)
    REPORT.write_text(content.rstrip() + "\n", encoding="utf-8")
    print(f"orphan_pages={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
