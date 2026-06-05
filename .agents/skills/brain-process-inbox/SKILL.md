---
name: brain-process-inbox
description: Process new raw notes, documents, and thoughts from month folders under 00-inbox into the personal knowledge base.
---

# Process Inbox Skill

Follow `AGENTS.md` first. This skill only defines the task-specific inbox procedure.

## Goal

Convert raw captured material into durable, linked knowledge with minimal human effort.

## Inputs

- New or modified files under `00-inbox/YYYY-MM/`

## Outputs

- Organized editable notes and source-derived material under `10-notes/`
- Updated canonical notes in `20-knowledge/` or active project contexts in `30-projects/`
- Updated person profiles in `20-knowledge/people/` when captures contain stable people facts, preferences, needs, communication patterns, relationship or other similar context
- Updated indexes
- Updated log
- Updated unresolved/duplicate/stale-claim reports if needed

## Steps

1. Scan `00-inbox/YYYY-MM/` month folders.
2. Classify each item:
   - domain
   - type
   - provenance
   - sensitivity
   - confidence
   - likely destination
3. Extract useful material from each item:
   - durable facts
   - source context
   - decisions or preferences
   - open questions
   - possible duplicate/overlap signals
   - stale, contradictory, or time-sensitive claims
   - proposed canonical note updates
   - affected people profiles and whether they need concise updates
4. Create or update organized material in `10-notes/` by preserving the captured content nearly as-is, except for meeting/call/recording/transcript captures.
   - Use short descriptive kebab-case filenames.
   - Do not add leading date prefixes to source filenames.
   - Preserve the human's wording, examples, and context as much as practical.
   - Light cleanup is allowed: structure, formatting, minor spelling fixes, broken Markdown, metadata, backlinks, and short agent notes that flag clear issues.
   - Do not rewrite captured content into LLM prose and do not replace it with a summary.
   - For meeting/call/recording/transcript captures, follow the meeting compression rules below instead of copying the full raw record into `10-notes/`.
   - Preserve capture/import dates in frontmatter, inbox processed markers, and the knowledge log.
5. Search existing canonical notes before creating new pages.
6. Update existing notes when possible.
7. Create new notes only when needed.
8. Add frontmatter.
9. Add backlinks.
10. Update `20-knowledge/index.md` when navigation changes.
11. Append a log entry to `20-knowledge/log.md`.
12. Update `.generated/indexes/`.
13. Add unresolved questions to `.generated/unresolved.md`.
14. Add possible duplicates to `.generated/duplicates.md`.
15. Add stale or contradictory claims to `.generated/stale-claims.md`.
16. Produce a concise summary of changes.

## Skill-specific judgment

- Keep the inbox easy for the human: do not require extra categorization before processing.
- Prefer updating existing knowledge/project/system notes over creating new pages.
- If destination is unclear after a reasonable search, add the item to `.generated/unresolved.md`.
- Write canonical notes in the original language of the source material. If a source mixes languages, follow the dominant language and preserve key quoted terms as written.

## Meeting compression judgment

- Leave full meeting/call/recording/transcript records in `00-inbox/YYYY-MM/`; do not copy them verbatim into `10-notes/`.
- Create one faithful compressed meeting note in `10-notes/` or the clearly implied project location.
- Preserve substantive facts, decisions, nuances, context, assumptions, risks, constraints, open questions, commitments, useful side topics, etc.
- Remove greetings, repetition, filler, false starts, meaningless self-corrections, over-explaining, etc.
- Let sections emerge from the meeting topics; do not force a fixed template.
- Consolidate scattered decisions and action items without losing context.
- Use light speaker/timestamp refs only when useful for verifying important nuance, decisions, ambiguity, or high-impact facts.
- Link to the raw inbox file with a quoted Obsidian wikilink; do not use traversal paths.
- Keep sensitivity at least as high as the raw source.

## Metadata judgment

- Use `origin: external` for digests or notes from someone else's article, book, course, lecture, video, recipe, official record, vendor page, professional guidance, or technical reference.
- Use `origin: personal` for the human's own memories, reflections, beliefs, preferences, original work, personal records, practices, planning, or decisions.
- Use `origin: mixed` when personal context or interpretation and external material both matter.
- Use `origin_note` for a short provenance explanation, such as "personal memory and preference", "digest of an external article", or "personal interpretation of external research".
- Use `sensitivity: high` for health, family, finance, legal, identity, personal documents, private work/client context, or anything harmful if exposed.
- Use `sensitivity: medium` for personal preferences, non-public work methods, reusable prompts with business relevance, and private but low-risk research notes.
- Use `sensitivity: low` for public concepts, public tools, public articles, and general learning notes.
- Use `confidence: high` for direct, reliable evidence.
- Use `confidence: medium` for plausible interpretation.
- Use `confidence: low` for memory, hypotheses, rough notes, or AI inference.
- Do not copy high-sensitivity content into low-sensitivity summaries.
- Write metadata file references as quoted Obsidian wikilinks.
