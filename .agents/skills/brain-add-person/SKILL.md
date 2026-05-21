---
name: brain-add-person
description: Create or update people profiles in the personal brain. Use when the human asks to add a person, create a profile for someone, capture person preferences, relationship context, communication needs, important dates, or practical details worth remembering.
---

# Brain Add Person

## Overview

Create useful, current person profiles while preserving source detail when it matters.

## Workflow

1. Read `brain.config.yml`, `20-knowledge/people/index.md`, `_templates/person.md`, and any existing matching profile.
2. Decide whether the request is for a new profile or an update.
3. Compare the supplied context with the current `_templates/person.md` sections and prompts.
4. Ask one organized set of profile questions in chat before editing files.
5. After the human answers, create or update `20-knowledge/people/person-slug.md` using `_templates/person.md`.
6. Put stable, reusable facts in the profile.
7. Put detailed raw memory, sensitive background, contradictions, or source-heavy material in a separate source note under `10-notes/people/`, then link it from `source`.
8. Create or update `10-notes/people/person-slug-interaction-log.md` only when dated interaction history matters.
9. Update `20-knowledge/people/index.md` and append a concise entry to `20-knowledge/log.md`.

## Asking Questions

Use the current `_templates/person.md` and available context to shape the questions.

Ask about profile areas that are missing, unclear, contradictory, or likely useful for the requested person. Add context-specific questions when existing notes, the user's wording, or the relationship type suggests them. It is fine to ask a fuller list at once; the human decides what to answer or skip.

## Judgment

- Keep profiles concise and current-state oriented.
- Ask first, write after the human answers.
- Do not copy empty or `TBD` fields.
- Do not require every possible field; let the human skip anything.
- Mark assumptions, contradictions, and uncertainty explicitly.
- Use `sensitivity: high` for family, children, health-adjacent, finance, conflict, identity, or private relationship context.
- Use `confidence: low` for memory, rough impressions, or uncertain claims.
- Preserve raw/source material when it carries meaning; do not replace it with a lossy summary.
