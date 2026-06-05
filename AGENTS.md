# AGENTS.md

This repository is a personal Markdown knowledge base. The human captures and reviews; agents organize, link, compile, and maintain.

## Core rules

- Preserve `00-inbox/` capture material unless the human explicitly asks otherwise.
- `10-notes/` is editable organized material; clean or enrich it carefully when requested or clearly useful.
- `20-knowledge/` is the compiled durable knowledge layer maintained by agents and reviewed by humans; `30-projects/` holds active project contexts.
- Do not replace source material or organized notes with lossy summaries.
- Prefer updating existing canonical notes over creating duplicates.
- If unsure where something belongs, put it in `.generated/unresolved.md`.
- Keep folders shallow; use metadata and backlinks for navigation.
- The human reviews local diffs before committing.

## User config

- Check `brain.config.yml` in the repository root when present.
- Explicit instructions in the current chat override `brain.config.yml`.
- `brain.config.yml` overrides skill defaults for chat output preferences.
- Answer in the current chat language when it is clear; otherwise use `preferred_language`.
- Source-preservation rules still control the language of persisted notes and source-derived synthesis.

## Metadata guidelines

- In frontmatter, use Obsidian wikilinks for file references in metadata fields.
- Do not use filesystem traversal paths like `../../...` in metadata values.
- In `10-notes/` and `20-knowledge/`, include `origin: personal | external | mixed` and a short natural `origin_note`.
- `origin` means starting authorship: the human, an outside source, or both. A digest of someone else's work is `external`.
- `origin_note` should be brief and human-readable, e.g. `"My family record"`, `"Article notes"`, `"My interpretation of external research"`.

## Structure

Source priority runs top to bottom:

- `00-inbox/` — raw capture/source-of-record, organized by month (`YYYY-MM`)
- `10-notes/` — organized editable notes and source-derived material
- `20-knowledge/` — compiled durable knowledge
- `30-projects/` — active project contexts
- `.agents/skills/` — repo-local agent skills
- `_templates/` — note templates
- `.generated/` — generated indexes, reports, Graphify outputs; lower authority than notes
- `_archive/` — inactive material

## Persistence model

- Chat is for interaction, advice, prioritization, and calls to action.
- Persist durable facts, decisions, corrections, project state, open questions, stale claims, duplicate candidates, indexes, trackers, and meaningful logs.
- Do not persist routine coaching or session-style reports by default.
- When chat produces a durable consequence, update the right note, tracker, project page, or log instead of saving the chat response.

## Natural evolution

Agents may create plain, lowercase top-level folders under `10-notes/` or `20-knowledge/` when a repeated category becomes durable enough to reduce friction.

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
