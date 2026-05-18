---
name: brain-refresh-research
description: Refresh a requested research topic or note; if no topic is given, recommend stale or high-value research areas that should be refreshed.
---

# Brain Refresh Research

Follow `AGENTS.md` first.

## Goal

Identify research that may be stale, incomplete, contradictory, or decision-relevant, and produce a focused refresh plan or refreshed brief when asked.

## Inputs to inspect

- User-provided research topic, note, domain, or question if present.
- `.generated/stale-claims.md`
- `.generated/unresolved.md`
- `.generated/indexes/open-questions.md`
- `.generated/indexes/recent-changes.md`
- Relevant notes in `20-knowledge/`, `10-notes/`, and `30-projects/`
- `_templates/research-brief.md` when a persisted brief is requested.

## Output

If a target topic is provided:

- What likely needs refreshing.
- Current source-backed understanding.
- Uncertain or stale claims.
- Refresh questions and preferred source types.
- Decision-ready recommendation or research brief when sufficient evidence exists.

If no target topic is provided:

- Ranked list of research refresh candidates.
- Why each matters now.
- Suggested validation path.
- Best first refresh.

## Judgment

- Prefer authoritative and current sources for time-sensitive topics.
- For health, legal, finance, and safety topics, avoid acting as a professional adviser.
- Separate old source evidence from current guidance.
- Mark assumptions clearly.
- Keep the scope narrow enough to answer a real question.

