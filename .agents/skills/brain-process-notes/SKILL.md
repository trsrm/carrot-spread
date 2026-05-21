---
name: brain-process-notes
description: Detect and process recent or uncommitted manual edits in 10-notes so durable changes are reconciled into 20-knowledge, indexes, logs, and maintenance reports without requiring manual status fields or inbox capture.
---

# Process Notes

## Overview

Use this skill when the human or agent has edited organized notes directly and wants agents to detect what changed, preserve source context, and update durable knowledge with low friction.

This complements `brain-process-inbox`: inbox handles new capture; this skill handles manual edits in `10-notes/`.

## Inputs

- Recently modified or uncommitted Markdown files under `10-notes/`.
- Deleted or renamed files under `10-notes/`.
- Optional user-provided scope such as "last 3 days", "people notes", or a specific path.

## Outputs

- Updated canonical notes in `20-knowledge/` or active project contexts in `30-projects/` when durable facts changed.
- Updated indexes where navigation changes.
- Updated `20-knowledge/log.md`.
- Updated `.generated/unresolved.md`, `.generated/duplicates.md`, or `.generated/stale-claims.md` when needed.
- A concise summary of detected note changes and resulting knowledge updates.

## Workflow

1. Detect candidates.
   - Run `python3 .agents/skills/brain-process-notes/scripts/list_note_changes.py`.
   - Use `--since-days N` when the user gives a time window.
   - Treat git working-tree changes as higher priority than mtime-only changes.
2. Classify each changed note:
   - durable fact addition
   - correction or deletion
   - preference or decision
   - provenance change or missing
   - source-only edit
   - formatting/noise
   - contradiction, stale claim, or unresolved ambiguity
3. Find related canonical pages.
   - Search `20-knowledge/` and `30-projects/`.
   - Prefer updating existing pages over creating new ones.
   - Treat `10-notes/` as editable organized material, not immutable raw capture.
   - Do not replace useful context with lossy summaries.
4. Reconcile changes.
   - Add new durable facts to canonical pages with source links.
   - Reflect corrections and removals only when supported by the changed note.
   - Do not silently merge contradictory claims; record ambiguity in `.generated/stale-claims.md` or `.generated/unresolved.md`.
   - If a note deletion removes source support, check whether canonical claims still have other sources before deleting knowledge.
5. Update navigation and logs.
   - Update relevant indexes only when navigation changed.
   - Append a concise entry to `20-knowledge/log.md`.
   - Update generated indexes if they already exist for the touched domain.
6. Report what happened.
   - List changed notes processed.
   - List canonical pages updated.
   - Call out skipped changes and why.

## Judgment

- The human should not need to add metadata, dates, tags, or agent prompts for this workflow.
- Use file modification time and git status as the implicit task queue.
- If the human changes a note in a way that changes authorship mix, update `origin` and `origin_note` along with the durable knowledge.
- If a change looks like a direct source correction, preserve the corrected organized note and update canonical knowledge.
- If a change looks like removed text, infer cautiously. Deleting text from `10-notes/` is not automatically proof that canonical knowledge is false.
- Keep the original language of the source note where possible.
- Use Obsidian wikilinks for note references in metadata.
- Do not copy high-sensitivity details into low-sensitivity summaries.

## Detection Script

Run:

```bash
python3 .agents/skills/brain-process-notes/scripts/list_note_changes.py --since-days 7
```

Useful options:

- `--since-days 3` narrows the mtime window.
- `--root 10-notes/people` limits detection to a subfolder.
- `--json` returns machine-readable output.

The script is a detector only. The agent still decides how to reconcile changes into canonical knowledge.
