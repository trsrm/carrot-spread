---
name: process-inbox
description: Process new raw notes, documents, and thoughts from month folders under 00-inbox into the personal knowledge base.
---

# Process Inbox Skill

Follow `AGENTS.md` first. This skill only defines the task-specific inbox procedure.

## Goal

Convert raw captured material into durable, linked knowledge with minimal human effort.

## Inputs

- New or modified files under `00-inbox/YYYY-MM/`

## Outputs

- Preserved raw sources under `10-source/`
- Updated canonical notes in `20-knowledge/`, `30-projects/`, or `40-systems/`
- Updated indexes
- Updated log
- Updated unresolved/duplicate/stale-claim reports if needed

## Steps

1. Scan `00-inbox/YYYY-MM/` month folders.
2. Classify each item:
   - domain
   - type
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
4. Preserve raw material in `10-source/`.
   - Use short descriptive kebab-case filenames.
   - Do not add leading date prefixes to source filenames.
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
- Write extraction notes in the original language of the source material. If a source mixes languages, follow the dominant language and preserve key quoted terms as written.

## Metadata judgment

- Use `sensitivity: high` for health, family, finance, legal, identity, personal documents, private work/client context, or anything harmful if exposed.
- Use `sensitivity: medium` for personal preferences, non-public work methods, reusable prompts with business relevance, and private but low-risk research notes.
- Use `sensitivity: low` for public concepts, public tools, public articles, and general learning notes.
- Use `confidence: high` for direct, reliable evidence.
- Use `confidence: medium` for plausible interpretation.
- Use `confidence: low` for memory, hypotheses, rough notes, or AI inference.
- Do not copy high-sensitivity content into low-sensitivity summaries.
