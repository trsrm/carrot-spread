---
name: deduplicate-notes
description: Detect and resolve duplicate or overlapping notes while preserving source traceability.
---

# Deduplicate Notes Skill

Follow `AGENTS.md` first. This skill only defines the task-specific deduplication procedure.

## Goal

Reduce fragmentation without losing history.

## Steps

1. Search for duplicate titles, tags, concepts, and backlinks.
2. Compare overlapping notes.
3. Identify canonical target.
4. Merge durable content.
5. Preserve source references.
6. Add redirects or backlinks from old notes.
7. Move deprecated notes to `_archive/` only if safe.
8. Update `.generated/duplicates.md`.
9. Update indexes and log.

## Skill-specific judgment

- Archive or redirect deprecated notes only when the canonical target is clear.
- When overlap is partial, link notes instead of forcing a merge.
- When confidence or sensitivity differs, preserve that distinction in the merged note.
