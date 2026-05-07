#!/usr/bin/env python3
"""Create missing personal-brain scaffold directories and placeholders.

The script is intentionally conservative: it creates missing directories and
placeholder files only. It never overwrites existing content.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_INBOX_MONTH = f"00-inbox/{date.today():%Y-%m}"

DIRECTORIES = [
    CURRENT_INBOX_MONTH,
    "10-source/articles",
    "10-source/documents",
    "10-source/conversations",
    "10-source/meetings",
    "10-source/emails",
    "10-source/screenshots",
    "10-source/medical",
    "10-source/finance",
    "10-source/work",
    "10-source/family",
    "20-knowledge/life",
    "20-knowledge/work",
    "20-knowledge/health",
    "20-knowledge/finance",
    "20-knowledge/car",
    "20-knowledge/learning",
    "20-knowledge/people",
    "20-knowledge/ideas",
    "30-projects/_template",
    "40-systems/workflows",
    "40-systems/prompts",
    "40-systems/checklists",
    "40-systems/decision-frameworks",
    "40-systems/templates",
    ".agents/skills/process-inbox",
    ".agents/skills/maintain-knowledge",
    ".agents/skills/deduplicate-notes",
    ".agents/skills/weekly-review",
    "_templates",
    ".generated/indexes",
    ".generated/graphify",
    ".generated/reports",
    "_archive",
    ".scripts",
]

PLACEHOLDERS = [
    f"{CURRENT_INBOX_MONTH}/.gitkeep",
    "10-source/articles/.gitkeep",
    "10-source/documents/.gitkeep",
    "10-source/conversations/.gitkeep",
    "10-source/meetings/.gitkeep",
    "10-source/emails/.gitkeep",
    "10-source/screenshots/.gitkeep",
    "10-source/medical/.gitkeep",
    "10-source/finance/.gitkeep",
    "10-source/work/.gitkeep",
    "10-source/family/.gitkeep",
]


def main() -> int:
    created_dirs = 0
    created_files = 0

    for rel in DIRECTORIES:
        path = ROOT / rel
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created_dirs += 1

    for rel in PLACEHOLDERS:
        path = ROOT / rel
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
            created_files += 1

    print(f"created_dirs={created_dirs}")
    print(f"created_files={created_files}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
