---
name: brain-activate-project
description: Turn a requested area, topic, or note cluster into an active project; if no area is given, recommend knowledge-base areas that look ready to become projects.
---

# Brain Activate Project

Follow `AGENTS.md` first.

## Goal

Help the human decide what should become a tracked `30-projects/` context, then create or recommend the lightest useful project shape.

## Inputs to inspect

- User-provided area, path, topic, or domain if present.
- `20-knowledge/log.md`
- `.generated/indexes/open-questions.md`
- `.generated/unresolved.md`
- `.generated/indexes/recent-changes.md`
- `.generated/indexes/active-projects.md`
- Related notes in `20-knowledge/`, `10-notes/`, and `30-projects/`
- `.generated/graphify/GRAPH_REPORT.md` when relationship discovery helps.

## Output

If a target area is provided:

- Project-worthiness judgment.
- Suggested project name and location.
- Starting goal, desired outcome, next actions, open questions, risks, and source links.
- Minimal project scaffold recommendation, using `30-projects/_template/` when execution is requested.

If no target area is provided:

- 3-7 candidate areas that appear project-like.
- Why each candidate matters.
- What would make it active or not active.
- Recommended first project to activate.

## Judgment

- Prefer a project only when there is an outcome, next action, owner, or unresolved decision.
- Do not over-projectize reference material.
- Keep projects lightweight; a project context should reduce friction, not create administration.
- Preserve sources and uncertainty.
- Ask only when activation depends on current intent that the notes cannot reveal.

