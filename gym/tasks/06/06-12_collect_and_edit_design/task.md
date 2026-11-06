# 06-12 — Design collect and edit and justify the boundary policies

Type: design. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

Parallel pauses can be answered with an interrupt-ID-to-response map. IDs identify requests; list order does not. Validate each edited value against its own schema and business limit before merging it into state.

## Your task

Design collect and edit and justify the boundary policies Implement the choices in run and complete design.md using the rubric.

## Inputs and acceptance

```json
[
  {
    "loss_date": "2026-01-01",
    "approved_cents": 125000
  },
  {
    "loss_date": "2026-01-01",
    "approved_cents": 0
  },
  {
    "loss_date": "2026-01-01",
    "approved_cents": 500001
  },
  {
    "loss_date": "invalid",
    "approved_cents": 125000
  },
  {
    "loss_date": "2026-01-01",
    "approved_cents": true
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 06-12
uv run gym check 06-12
uv run gym hint 06-12
```

## Reading

[Module lesson](../../../../modules/06_human_in_the_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/interrupts)
