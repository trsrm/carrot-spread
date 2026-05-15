![Carrot Spread Logo](https://i.ibb.co/1tr6Ynyp/photo-2026-05-07-23-54-29.jpg)

# Carrot Spread

Markdown-first personal knowledge base for human and AI collaboration. Think of it as a personal brain-dump, but with structure and agents to help you organize, synthesize, and act on your knowledge.

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

- `process-inbox` — process new captured material from `00-inbox/YYYY-MM/`.
- `process-notes` — reconcile recent or uncommitted manual edits in `10-notes/`.
- `maintain-knowledge` — update, reconcile, and source-check durable knowledge pages.
- `deduplicate-notes` — resolve duplicate or overlapping notes.
- `weekly-review` — review recent changes, open questions, and next actions.

Skills should contain procedures that an agent can run. General notes, prompts, and evaluation material belong in `40-systems/` or domain folders, not in skills.

## Daily workflow

1. Add raw notes/documents to the current `00-inbox/YYYY-MM/` folder.
2. Ask Codex or another agent to process the inbox.
3. Review the diff and commit.
