---
name: maintain-knowledge
description: Maintain durable knowledge pages using raw sources, canonical notes, indexes, logs, and backlinks.
---

# Maintain Knowledge Skill

Follow `AGENTS.md` first. This skill only defines task-specific knowledge maintenance procedures.

## Mental model

This repo follows a source-preserving knowledge maintenance pattern:

- Raw sources are preserved in `10-source/`.
- Durable knowledge is maintained in `20-knowledge/`.
- The schema is defined in root instructions and focused skills.
- Human effort should focus on capture, review, and direction.

## Operations

### Ingest

- Read new source material.
- Preserve raw files.
- Extract durable knowledge.
- Update existing pages before creating new ones.
- Add source references.
- Update `20-knowledge/index.md`.
- Append to `20-knowledge/log.md`.

### Query

- Start from `20-knowledge/index.md`.
- Read canonical pages.
- Check raw sources for sensitive or important claims.
- If the answer creates reusable knowledge, save it back only if instructed.

### Lint

Look for:

- stale claims
- contradictions
- duplicate pages
- orphan pages
- missing backlinks
- missing source references
- unresolved questions

## Skill-specific judgment

- Keep knowledge pages readable by humans.
- Keep durable pages current-state oriented.
- Use logs and generated reports to surface maintenance needs, not as canonical truth.
- Prefer direct raw sources over summaries.
- Mark assumptions explicitly.
- Preserve uncertainty and source context when claims conflict.
- Keep the original language and tone of the source material when possible.
