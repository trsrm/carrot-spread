---
name: brain-risk-radar
description: Proactively scan for sensitive, stale, contradictory, high-impact, or unsafe-to-act-on notes across health, finance, family, legal/admin, and work contexts.
---

# Brain Risk Radar

Follow `AGENTS.md` first.

## Goal

Surface risks in the knowledge base that could lead to bad real-world decisions if left unexamined.

## Inputs to inspect

- `.generated/stale-claims.md`
- `.generated/unresolved.md`
- `.generated/indexes/open-questions.md`
- `20-knowledge/health/`
- `20-knowledge/finance/`
- `20-knowledge/family/`
- `20-knowledge/work/`
- Relevant recent log entries.

## Output

- Highest-risk items.
- Why each risk matters.
- What should not be acted on yet.
- Suggested validation source or person.
- One low-friction risk-reduction action.

## Judgment

- Prioritize impact and likelihood over completeness.
- Treat stale health, money, family, and work/client claims carefully.
- Keep risk language calm, concrete, and useful.
- Prefer "verify before acting" over alarm.

