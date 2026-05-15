# AGENTS.md

This repository is a personal Markdown knowledge base used by humans and AI agents.

## Mission

Maintain a low-friction personal knowledge base that captures raw material, preserves sources, and compounds into durable, agent-maintained knowledge.

The human should mainly capture and review. Agents should organize, link, summarize, and maintain.

## Core rules

- Preserve raw source material.
- Never overwrite source notes with summaries.
- Prefer updating existing canonical notes over creating duplicates.
- If unsure where something belongs, put it in `.generated/unresolved.md`.
- Keep folders shallow.
- Use metadata and backlinks for navigation.
- The human reviews local diffs before committing.

## Metadata guidelines

- In frontmatter, use Obsidian wikilinks for file references in metadata fields.
- Do not use filesystem traversal paths in metadata values.

## Canonical structure

- `00-inbox/` — human capture zone organized by month folders (`YYYY-MM`)
- `10-notes/` — organized notes and preserved raw sources
- `20-knowledge/` — durable knowledge, maintained from notes and preserved raw sources
- `30-projects/` — active project contexts
- `40-systems/` — reusable prompts, workflows, checklists, and operating tools
- `.agents/skills/` — repo-local agent skills
- `_templates/` — note templates
- `.generated/` — generated indexes, reports, Graphify outputs
- `_archive/` — inactive material

## Natural evolution

The starting folders are not permanent taxonomy. Agents may create new top-level folders under `20-knowledge/`, `10-notes/`, or `40-systems/` when a category becomes durable and useful enough to reduce friction.

Use plain, lowercase folder names. Prefer reusing an existing folder until there is clear repeated need for a new one.

## Local skills

Detailed procedures live in repo-local skills under `.agents/skills/`.

- Use `process-inbox` for moving captured material from `00-inbox/YYYY-MM/` into organized notes/sources, knowledge, project, or system notes.
- Use `process-notes` for detecting recent or uncommitted manual edits in `10-notes/` and reconciling them into durable knowledge without requiring manual status fields.
- Use `maintain-knowledge` for reconciling, source-checking, updating, and linting durable knowledge pages.
- Use `deduplicate-notes` for duplicate or overlapping notes.
- Use `weekly-review` for periodic review of recent changes, open questions, and next actions.

## Source-of-truth hierarchy

1. Organized notes and preserved raw sources in `10-notes/`
2. Canonical notes in `20-knowledge/`, `30-projects/`, `40-systems/`
3. Generated indexes in `.generated/indexes/`
4. Graphify output in `.generated/graphify/`

## Graphify

This project has a Graphify knowledge graph at `.generated/graphify/`.

Default setup:

- Treat `.generated/graphify/` as the default Graphify output path for this repository.
- Before running any Graphify command, set `GRAPHIFY_OUT=.generated/graphify`, otherwise cache files will be generated in the root.
- Hotfix: when calling Graphify helpers that read or write manifests, pass `manifest_path=".generated/graphify/manifest.json"` explicitly; do not allow `graphify-out/manifest.json` in the repository root.

Rules:

- Read `.generated/graphify/GRAPH_REPORT.md` for god nodes and community structure before doing project-level analysis.
- Use Graphify query output only for navigation and relationship discovery. Prefer:
    - `graphify query "<question>"`
    - `graphify path "<A>" "<B>"`
    - `graphify explain "<concept>"`


## Agent scripts

- Prefer reusing existing `.scripts/` utilities before suggesting new automation.

## Style

- Be direct.
- Avoid filler.
- Prefer structured Markdown.
- Preserve nuance.
- Explicitly mark assumptions.
- Use decision-ready summaries.

## Safety

Do not invent missing facts.
Do not silently merge contradictory claims.
Do not delete raw files unless explicitly instructed.
Do not publish sensitive data.
Do not commit secrets.
