#!/usr/bin/env python3
"""List recent and uncommitted note changes for knowledge reconciliation."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
from pathlib import Path


def run_git(args: list[str]) -> str:
    try:
        return subprocess.check_output(["git", *args], text=True, stderr=subprocess.DEVNULL)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def git_changes(roots: list[Path]) -> list[dict[str, str]]:
    args = ["status", "--porcelain=v1", "-z", "--", *[str(root) for root in roots]]
    raw = run_git(args)
    if not raw:
        return []

    parts = raw.split("\0")
    changes: list[dict[str, str]] = []
    i = 0
    while i < len(parts):
        entry = parts[i]
        i += 1
        if not entry:
            continue

        status = entry[:2]
        path = entry[3:]
        change: dict[str, str] = {"status": status, "path": path}

        if status.strip().startswith("R") or status.strip().startswith("C"):
            if i < len(parts) and parts[i]:
                change["new_path"] = parts[i]
                i += 1

        changes.append(change)
    return changes


def recent_markdown_files(roots: list[Path], since: dt.datetime) -> list[dict[str, str]]:
    recent: list[dict[str, str]] = []
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            if any(part.startswith(".") for part in path.parts):
                continue
            stat = path.stat()
            modified = dt.datetime.fromtimestamp(stat.st_mtime).astimezone()
            if modified >= since:
                recent.append(
                    {
                        "path": str(path),
                        "modified": modified.isoformat(timespec="seconds"),
                    }
                )
    return sorted(recent, key=lambda item: item["modified"], reverse=True)


def render_markdown(data: dict[str, object]) -> str:
    lines = [
        "# Note Change Candidates",
        "",
        f"- generated: {data['generated_at']}",
        f"- since: {data['since']}",
        f"- roots: {', '.join(data['roots'])}",
        "",
        "## Git changes",
    ]

    git_items = data["git_changes"]
    if git_items:
        for item in git_items:
            status = item["status"].strip() or "modified"
            if "new_path" in item:
                lines.append(f"- `{status}` `{item['path']}` -> `{item['new_path']}`")
            else:
                lines.append(f"- `{status}` `{item['path']}`")
    else:
        lines.append("- None detected.")

    lines.extend(["", "## Recently modified Markdown files"])
    recent_items = data["recent_markdown_files"]
    if recent_items:
        for item in recent_items:
            lines.append(f"- `{item['path']}` modified {item['modified']}")
    else:
        lines.append("- None detected.")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="List recent or uncommitted Markdown note changes.")
    parser.add_argument("--since-days", type=float, default=7, help="mtime window in days")
    parser.add_argument("--root", action="append", help="note root to scan; repeatable")
    parser.add_argument("--json", action="store_true", help="print JSON instead of Markdown")
    args = parser.parse_args()

    roots = [Path(root) for root in (args.root or ["10-notes"])]
    now = dt.datetime.now().astimezone()
    since = now - dt.timedelta(days=args.since_days)

    data: dict[str, object] = {
        "generated_at": now.isoformat(timespec="seconds"),
        "since": since.isoformat(timespec="seconds"),
        "roots": [str(root) for root in roots],
        "git_changes": git_changes(roots),
        "recent_markdown_files": recent_markdown_files(roots, since),
    }

    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(data), end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
