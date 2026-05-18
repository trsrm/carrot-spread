<img src="https://i.ibb.co/LXx5DPjq/photo-2026-05-07-23-54-29.jpg" alt="Carrot Spread Logo" width="200">

# Carrot Spread

This repository is a Markdown-first personal knowledge base for human and AI collaboration.

## Operating model

- Human captures raw thoughts and documents in month folders under `00-inbox/`.
- Agents preserve organized notes and sources in `10-notes/`.
- Agents maintain durable knowledge in `20-knowledge/`.
- Active projects live in `30-projects/`.
- Reusable workflows and prompts live in `40-systems/`.
- Repo-local agent skills live in `.agents/skills/`.
- Generated indexes and graphs live in `.generated/`.

## Agent skills

`AGENTS.md` is the repo constitution. It defines global safety, source-of-truth, and structure rules.

Use `.agents/skills/` for task-specific procedures:

- `brain-process-inbox` — process new captured material from `00-inbox/YYYY-MM/`.
- `brain-process-notes` — reconcile recent or uncommitted edits in `10-notes/`.
- `brain-maintain-knowledge` — update, reconcile, source-check, deduplicate, lint durable knowledge pages, and conservatively surface cleanup or archive candidates.
- `brain-weekly-review` — review recent changes, open questions, and next actions.

Guidance skills use two roles:

- Coach skills help act on a known domain, situation, or decision.
- Radar skills proactively detect hidden cross-domain issues.

Current guidance skills:

- `brain-personal-coach` — broad personal guidance, weekly priorities, proactive personal scans, patterns, and next actions.
- `brain-health-coach`, `brain-financial-coach`, `brain-family-coach`, `brain-professional-coach`, and `brain-decision-coach` — domain-specific guidance.
- `brain-risk-radar` — stale, sensitive, contradictory, high-impact, or unsafe-to-act-on claims across domains.
- `brain-project-radar` — notes that imply active projects but are not tracked in `30-projects`.

Skills should contain procedures that an agent can run. General notes, prompts, and evaluation material belong in `40-systems/` or domain folders, not in skills.

## Daily workflow

1. Add raw notes/documents to the current `00-inbox/YYYY-MM/` folder.
2. Ask Codex or another agent to process the inbox.
3. Review the diff and commit.
