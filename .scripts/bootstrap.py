#!/usr/bin/env python3
"""Create missing knowledge-base scaffold directories and placeholders.

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
    "10-notes/articles",
    "10-notes/documents",
    "10-notes/conversations",
    "10-notes/meetings",
    "10-notes/emails",
    "10-notes/screenshots",
    "10-notes/medical",
    "10-notes/finance",
    "10-notes/work",
    "10-notes/family",
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
    ".agents/skills/brain-process-inbox",
    ".agents/skills/brain-process-notes",
    ".agents/skills/brain-maintain-knowledge",
    ".agents/skills/brain-weekly-review",
    ".agents/skills/brain-activate-project",
    ".agents/skills/brain-refresh-research",
    ".agents/skills/brain-professional-coach",
    ".agents/skills/brain-health-coach",
    ".agents/skills/brain-family-coach",
    ".agents/skills/brain-financial-coach",
    ".agents/skills/brain-decision-coach",
    ".agents/skills/brain-stuck-mode",
    ".agents/skills/brain-personal-coach",
    ".agents/skills/brain-risk-radar",
    ".agents/skills/brain-project-radar",
    "_templates",
    ".generated/indexes",
    ".generated/graphify",
    ".generated/reports",
    "_archive",
    ".scripts",
]

PLACEHOLDERS = [
    f"{CURRENT_INBOX_MONTH}/.gitkeep",
    "10-notes/articles/.gitkeep",
    "10-notes/documents/.gitkeep",
    "10-notes/conversations/.gitkeep",
    "10-notes/meetings/.gitkeep",
    "10-notes/emails/.gitkeep",
    "10-notes/screenshots/.gitkeep",
    "10-notes/medical/.gitkeep",
    "10-notes/finance/.gitkeep",
    "10-notes/work/.gitkeep",
    "10-notes/family/.gitkeep",
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
