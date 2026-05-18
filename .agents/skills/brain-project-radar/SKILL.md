---
name: brain-project-radar
description: Proactively scan the personal brain for notes that imply active projects but are not tracked in 30-projects.
---

# Brain Project Radar

Follow `AGENTS.md` first.

## Goal

Find initiatives hiding inside notes and recommend which ones deserve project tracking.

## Inputs to inspect

- `.generated/indexes/active-projects.md`
- `.generated/indexes/open-questions.md`
- `.generated/unresolved.md`
- `.generated/indexes/recent-changes.md`
- `20-knowledge/log.md`
- `20-knowledge/life/`, `20-knowledge/health/`, `20-knowledge/work/`, `20-knowledge/family/`, `20-knowledge/finance/`
- `.generated/graphify/GRAPH_REPORT.md` when useful.

## Output

- Candidate project areas.
- Evidence that each is active or blocked.
- Recommended project title and minimal outcome.
- First next action.
- Which candidates should remain reference notes.

## Judgment

- A project needs a desired outcome and next action.
- Do not create project overhead for passive reference material.
- Prefer a small number of strong candidates.
- If asked to activate one, defer to `brain-activate-project`.

