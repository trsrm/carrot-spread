# AGENTS.md

This repository is a personal Markdown knowledge base. The human captures and reviews; agents organize, link, compile, and maintain.

## Core rules

- Preserve `00-inbox/` capture material unless the human explicitly asks otherwise.
- `10-notes/` is editable organized material; clean or enrich it carefully when requested or clearly useful.
- `20-knowledge/`, `30-projects/`, and `40-systems/` are compiled durable layers maintained by agents and reviewed by humans.
- Do not replace source material or organized notes with lossy summaries.
- Prefer updating existing canonical notes over creating duplicates.
- If unsure where something belongs, put it in `.generated/unresolved.md`.
- Keep folders shallow; use metadata and backlinks for navigation.
- The human reviews local diffs before committing.

## Metadata guidelines

- In frontmatter, use Obsidian wikilinks for file references in metadata fields.
- Do not use filesystem traversal paths like `../../...` in metadata values.

## Structure

Source priority runs top to bottom:

- `00-inbox/` — raw capture/source-of-record, organized by month (`YYYY-MM`)
- `10-notes/` — organized editable notes and source-derived material
- `20-knowledge/` — compiled durable knowledge
- `30-projects/` — active project contexts
- `40-systems/` — reusable prompts, workflows, checklists, tools
- `.agents/skills/` — repo-local agent skills
- `_templates/` — note templates
- `.generated/` — generated indexes, reports, Graphify outputs; lower authority than notes
- `_archive/` — inactive material

## Natural evolution

Agents may create plain, lowercase top-level folders under `10-notes/`, `20-knowledge/`, or `40-systems/` when a repeated category becomes durable enough to reduce friction.

## Local skills

- Use `brain-process-inbox` for moving captured material from `00-inbox/YYYY-MM/` into organized notes/sources, knowledge, project, or system notes.
- Use `brain-process-notes` for detecting recent or uncommitted manual edits in `10-notes/` and reconciling them into durable knowledge without requiring manual status fields.
- Use `brain-maintain-knowledge` for reconciling, source-checking, updating, deduplicating, linting durable knowledge pages, and conservatively surfacing cleanup or archive candidates.
- Use `brain-weekly-review` for periodic review of recent changes, open questions, and next actions.

## Graphify

- Treat `.generated/graphify/` as the default Graphify output path.
- Before running any Graphify command, set `GRAPHIFY_OUT=.generated/graphify`, otherwise cache files will be generated in the root.
- Hotfix: when calling Graphify helpers that read or write manifests, pass `manifest_path=".generated/graphify/manifest.json"` explicitly; do not allow `graphify-out/manifest.json` in the repository root.
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

- Do not invent missing facts.
- Do not silently merge contradictory claims.
- Do not delete raw files unless explicitly instructed.
- Do not publish sensitive data.
- Do not commit secrets.
