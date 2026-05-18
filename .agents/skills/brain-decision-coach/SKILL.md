---
name: brain-decision-coach
description: Use the personal brain to prepare a decision packet for a requested decision, or identify likely blocking decisions when none is specified.
---

# Brain Decision Coach

Follow `AGENTS.md` first.

## Goal

Turn scattered notes into a clear decision frame that helps the human choose or identify what is blocking choice.

## Inputs to inspect

- User-provided decision, area, note, or domain if present.
- `.generated/indexes/open-questions.md`
- `.generated/unresolved.md`
- `.generated/stale-claims.md`
- `20-knowledge/log.md`
- Relevant notes and project contexts.

## Output

- Decision statement.
- Known facts.
- Assumptions and uncertainties.
- Options.
- Risks and tradeoffs.
- Recommended next step.
- One question that would most improve the decision.

## Judgment

- Do not force certainty when the sources are thin.
- Make the decision smaller if it is too broad.
- Prefer reversible next steps when confidence is low.
- Mark when professional advice or family discussion is needed.

