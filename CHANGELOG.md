# Changelog

## v0.5 (2026-05-21)

- Added provenance metadata guidance for `origin: personal | external | mixed` and `origin_note` across `10-notes/` and `20-knowledge/`.
- Updated note and knowledge templates to include provenance fields, including clearer source-note origin prompts.
- Added the new `brain-add-person` skill for creating or updating people profiles while preserving detailed source notes and interaction logs.
- Refreshed person-profile handling and removed the separate `person-intake` template in favor of the richer canonical person template.

## v0.4 (2026-05-19)

- Added domain placement auditing to `brain-maintain-knowledge` so maintenance checks path, frontmatter domain, source-folder category, title, tags, and index ownership as independent signals.
- Added root `brain.config.yml` support for user-level chat preferences such as `preferred_language`.
- Merged the old `40-systems/` layer back into the main knowledge structure so durable system notes live under `10-notes/` or `20-knowledge/` instead of a separate top-level folder.
- Updated core processing skills to target `20-knowledge/` and `30-projects/`, with people-profile handling in `brain-process-inbox`.
- Changed `brain-weekly-review` to return the review in chat by default and persist follow-up changes only when they create durable state.
- Refined `brain-maintain-knowledge` restructuring guidance for crowded, misplaced, overlapping, or unclear notes and folders.

## v0.3 (2026-05-18)

- Introduced the namespaced `brain-*` skill framework, replacing the earlier generic skill names with clearer personal-brain workflows.
- Added major new guidance skills for project activation, personal coaching, health, finance, family, professional work, decisions, stuck-mode support, research refreshes, risk radar, and project radar.
- Clarified the framework model: `00-inbox/` is raw source-of-record capture, `10-notes/` is editable organized/source-derived material, and durable compiled knowledge lives in `20-knowledge/`, `30-projects/`, and `40-systems/`.
- Updated framework scripts for the `10-notes/` layout, generated indexes, orphan checks, and localized open-question detection.
- Expanded people support with interaction-log conventions, a richer canonical person template, and a new person-intake questionnaire.
- Refreshed README, AGENTS instructions, bootstrap scaffolding, and template indexes to document the new framework.

## v0.2 (2026-05-15)

- Migrated preserved-source guidance to `10-notes/` for organized notes and preserved raw sources.
- Added the `process-notes` skill for reconciling manual edits in `10-notes/` into durable knowledge.
- Updated agent instructions, inbox guidance, and checklist metadata to use the latest Obsidian wikilink conventions.
- Documented the Graphify manifest hotfix in `AGENTS.md`.
