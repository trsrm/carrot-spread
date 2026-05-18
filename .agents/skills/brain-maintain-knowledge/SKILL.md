---
name: brain-maintain-knowledge
description: Maintain durable knowledge pages using raw sources, organized notes, canonical notes, indexes, logs, backlinks, deduplication, and conservative cleanup radar.
---

# Maintain Knowledge Skill

Follow `AGENTS.md` first. This skill only defines task-specific knowledge maintenance procedures.

## Mental model

This repo follows a source-preserving knowledge maintenance pattern:

- Raw capture/source-of-record material lives in `00-inbox/` and is not rewritten during normal processing.
- Organized editable notes and source-derived material live in `10-notes/`.
- Compiled durable knowledge is maintained in `20-knowledge/`.
- The schema is defined in root instructions and focused skills.
- Human effort should focus on capture, review, and direction.

## Default pass

When invoked without a specific target, run all maintenance operations in a conservative sequence:

1. Read the main navigation and maintenance surfaces:
   - `20-knowledge/index.md`
   - recent entries in `20-knowledge/log.md`
   - `.generated/README.md`
   - `.generated/unresolved.md`, `.generated/stale-claims.md`, `.generated/duplicates.md`, and `.generated/orphan-pages.md` if present
   - `.generated/graphify/GRAPH_REPORT.md` if present
2. Run `Source Check` for sensitive, important, stale, or high-impact claims surfaced by indexes, logs, generated reports, or Graphify.
3. Run `Lint` across the maintained knowledge surfaces.
4. Run `Navigation Repair`, applying small local fixes only when the fix is clear and source-preserving.
5. Run `Deduplication`, resolving duplicate or overlapping notes while preserving source traceability.
6. Run `Restructure Options`, returning advisory before/after options in chat.
7. Run `Archive Review`, returning archive candidates and rationale in chat.
8. Run `Cleanup Radar`, returning ranked cleanup candidates in chat.
9. Ask the human only when a decision affects broad folder moves, non-trivial duplicate merges, source interpretation, or archival of raw/source material.

Default output:

- Changes made
- Issues found but not changed
- Source checks
- Duplicate findings
- Restructure options
- Archive candidates
- Cleanup radar
- Follow-up decisions needed

## Operations

### Source Check

- Start from canonical pages, then verify sensitive or important claims against `10-notes/` and, when needed, original `00-inbox/` captures.
- Prefer direct organized/source material over lossy summaries when claims affect decisions.
- Mark unsupported, stale, or contradictory claims for maintenance.
- Do not save new reusable knowledge unless explicitly instructed.

### Lint

Look for:

- stale claims
- contradictions
- duplicate pages
- orphan pages
- missing backlinks
- missing source references
- unresolved questions
- plain path file references

### Navigation Repair

- Fix broken or stale links, missing backlinks, index gaps, and plain filesystem path references.
- Convert metadata file references to quoted Obsidian wikilinks.
- Use generated artifacts such as orphan reports as hints, not canonical truth.
- Update navigation only when it improves findability.

### Restructure Options

- Advisory only by default.
- Propose folder or page restructuring when repeated friction, crowding, misplaced notes, or unclear canonical ownership appears.
- Return before/after structure, rationale, affected notes, and risks in chat.
- Do not move files or rewrite links unless explicitly asked.

### Archive Review

- Identify stale, superseded, inactive, or one-off material that may belong in `_archive/`.
- Return archive candidates and rationale in chat instead of creating a generated report.
- Never recommend archiving `00-inbox/` source-of-record material unless the human explicitly asks.
- Prefer "candidate" language unless canonical replacement, source preservation, and link impact are clear.

### Cleanup Radar

- Advisory only by default.
- Return cleanup candidates in chat instead of creating a generated report.
- Do not move, delete, archive, rewrite, or generate files unless explicitly asked.
- Use these ranked buckets:
  - Archive candidates
  - Low-signal or low-value content
  - Duplicate or overlapping content
  - Stale generated artifacts
  - Do-not-touch or preserve items
  - Follow-up decisions needed
- Mark uncertainty and weak evidence clearly.
- Prefer a small number of high-confidence recommendations over a broad sweep.

### Deduplication

- Treat duplicate or overlapping pages as a normal maintenance concern.
- Detect duplicate titles, overlapping concepts, repeated source summaries, and competing canonical pages.
- Compare overlapping notes before merging.
- Identify the canonical target.
- Merge durable content into the canonical note.
- Preserve source references.
- Add redirects or backlinks from old notes.
- Move deprecated notes to `_archive/` only when the canonical target is clear, source preservation is verified, and link impact is understood.
- Update `.generated/duplicates.md`.
- Update relevant indexes and `20-knowledge/log.md`.
- Preserve source traceability and confidence or sensitivity distinctions.
- When overlap is partial, link notes instead of forcing a merge.

## Skill-specific judgment

- Keep knowledge pages readable by humans.
- Keep durable pages current-state oriented.
- Use logs and generated reports to surface maintenance needs, not as canonical truth.
- Prefer direct organized/source material over lossy summaries.
- Mark assumptions explicitly.
- Preserve uncertainty and source context when claims conflict.
- Keep the original language and tone of the source material when possible.
- Write metadata file references as quoted Obsidian wikilinks.
