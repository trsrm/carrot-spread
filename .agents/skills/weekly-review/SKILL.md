---
name: weekly-review
description: Review recent changes, unresolved questions, active projects, stale notes, and suggested next actions.
---

# Weekly Review Skill

Follow `AGENTS.md` first. This skill only defines the task-specific weekly review procedure.

## Goal

Keep the personal brain useful and current.

## Inputs

- `20-knowledge/log.md`
- `.generated/indexes/recent-changes.md`
- `.generated/unresolved.md`
- `.generated/stale-claims.md`
- `.generated/duplicates.md`
- `.generated/indexes/active-projects.md`

## Output

Create or update:

```text
.generated/reports/weekly-review-YYYY-MM-DD.md
```

## Review sections

- New knowledge added
- Active projects
- Open questions
- Stale claims
- Duplicates
- Orphan pages
- Suggested next actions
- Suggested archives

## Skill-specific judgment

- Do not create busywork.
- Prioritize high-leverage cleanup.
- Separate suggestions from actions taken.

## Implementation note

- Run `python3 .scripts/check_orphans.py` during weekly review and use `.generated/orphan-pages.md` in the Orphan pages section if available.
