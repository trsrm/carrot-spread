#!/usr/bin/env python3
"""Rebuild simple generated Markdown indexes.

The script reads frontmatter and headings, then writes only files under
`.generated/indexes/`.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX_DIR = ROOT / ".generated" / "indexes"
DOMAINS = ["life", "work", "health", "family", "finance", "car", "learning", "ai", "general"]
SKIP_NAMES = {"AGENTS.md", "README.md"}
SKIP_PREFIXES = (
    ".agents/",
    ".git/",
    ".generated/",
    ".obsidian/",
    ".scripts/",
    "00-inbox/",
    "30-projects/_template/",
    "_archive/",
    "_templates/",
)


@dataclass(frozen=True)
class Note:
    path: Path
    rel: str
    title: str
    fields: dict[str, str]
    mtime: float


def relpath(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    try:
        _, block, _ = text.split("---", 2)
    except ValueError:
        return {}
    fields: dict[str, str] = {}
    for raw_line in block.splitlines():
        if not raw_line.strip() or raw_line.startswith(" ") or raw_line.startswith("-"):
            continue
        if ":" in raw_line:
            key, value = raw_line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def load_notes() -> list[Note]:
    notes: list[Note] = []
    for path in sorted(ROOT.rglob("*.md")):
        rel = relpath(path)
        if path.name in SKIP_NAMES or any(rel.startswith(prefix) for prefix in SKIP_PREFIXES):
            continue
        text = path.read_text(encoding="utf-8")
        notes.append(
            Note(
                path=path,
                rel=rel,
                title=first_heading(text, path.stem.replace("-", " ").title()),
                fields=parse_frontmatter(text),
                mtime=path.stat().st_mtime,
            )
        )
    return notes


def link(note: Note) -> str:
    return f"[{note.title}](../../{note.rel})"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_project_indexes(notes: list[Note]) -> None:
    project_candidates = [
        note
        for note in notes
        if note.rel.startswith("30-projects/")
        and not note.rel.startswith("30-projects/_template/")
        and note.path.name in {"index.md", "00-context.md"}
    ]
    by_project_dir: dict[Path, list[Note]] = {}
    for note in project_candidates:
        by_project_dir.setdefault(note.path.parent, []).append(note)
    project_notes = []
    for project_dir in sorted(by_project_dir):
        candidates = by_project_dir[project_dir]
        project_notes.append(next((note for note in candidates if note.path.name == "index.md"), candidates[0]))

    def row(note: Note) -> str:
        status = note.fields.get("status", "")
        domain = note.fields.get("domain", "")
        updated = note.fields.get("updated", "")
        return f"| {link(note)} | {status} | {domain} | {updated} | [{note.rel}](../../{note.rel}) |"

    header = "# Active Projects\n\n| Project | Status | Domain | Updated | Links |\n|---|---|---|---:|---|\n"
    active_rows = [row(note) for note in project_notes if note.fields.get("status") == "active"]
    write(INDEX_DIR / "active-projects.md", header + "\n".join(active_rows))

    header = "# All Projects\n\n| Project | Status | Domain | Updated | Links |\n|---|---|---|---:|---|\n"
    write(INDEX_DIR / "all-projects.md", header + "\n".join(row(note) for note in project_notes))


def write_decisions(notes: list[Note]) -> None:
    decisions = [note for note in notes if note.fields.get("type") == "decision"]
    rows = []
    for note in decisions:
        rows.append(
            f"| {note.fields.get('created', '')} | {note.title} | [{note.rel}](../../{note.rel}) | {note.fields.get('status', '')} | [{note.rel}](../../{note.rel}) |"
        )
    content = "# Decisions\n\n| Date | Decision | Location | Status | Links |\n|---|---|---|---|---|\n" + "\n".join(rows)
    write(INDEX_DIR / "decisions.md", content)


def write_open_questions(notes: list[Note]) -> None:
    question_notes = [note for note in notes if note.fields.get("type") == "question"]
    rows = []
    for note in question_notes:
        rows.append(f"| {note.fields.get('created', '')} | {note.title} | [{note.rel}](../../{note.rel}) |  | {note.fields.get('status', '')} |")
    for note in notes:
        text = note.path.read_text(encoding="utf-8")
        in_section = False
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.lower() in {"## open questions", "## відкриті питання"}:
                in_section = True
                continue
            if in_section and stripped.startswith("## "):
                break
            if in_section and stripped.startswith("- "):
                question = stripped[2:].strip()
                if question.lower().rstrip(".") in {"none", "немає"}:
                    continue
                if question:
                    rows.append(f"| {note.fields.get('updated', '')} | {question} | [{note.rel}](../../{note.rel}) |  | open |")
    content = "# Open Questions\n\n| Date | Question | Location | Owner | Status |\n|---|---|---|---|---|\n" + "\n".join(rows)
    write(INDEX_DIR / "open-questions.md", content)


def write_recent_changes(notes: list[Note]) -> None:
    recent = sorted(notes, key=lambda note: note.mtime, reverse=True)[:25]
    rows = []
    for note in recent:
        date = datetime.fromtimestamp(note.mtime).date().isoformat()
        rows.append(f"| {date} | {note.fields.get('type', '')} | {note.title} | [{note.rel}](../../{note.rel}) |")
    content = "# Recent Changes\n\n| Date | Type | Title | Files |\n|---|---|---|---|\n" + "\n".join(rows)
    write(INDEX_DIR / "recent-changes.md", content)


def write_domain_indexes(notes: list[Note]) -> None:
    for domain in DOMAINS:
        domain_notes = [note for note in notes if note.fields.get("domain") == domain and not note.rel.startswith("_templates/")]
        rows = []
        for note in domain_notes:
            rows.append(f"| {link(note)} | {note.fields.get('status', '')} | {note.fields.get('updated', '')} | {note.fields.get('sensitivity', '')} |")
        title = domain.replace("-", " ").title()
        content = f"# {title} Index\n\n| Note | Status | Updated | Sensitivity |\n|---|---|---:|---|\n" + "\n".join(rows)
        write(INDEX_DIR / f"{domain}.md", content)


def main() -> int:
    notes = load_notes()
    write_project_indexes(notes)
    write_decisions(notes)
    write_open_questions(notes)
    write_recent_changes(notes)
    write_domain_indexes(notes)
    print(f"indexed_notes={len(notes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
