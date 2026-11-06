# 06-10 — Trace collect and edit: Each interrupt must receive the response for its own request kind.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Parallel pauses can be answered with an interrupt-ID-to-response map. IDs identify requests; list order does not. Validate each edited value against its own schema and business limit before merging it into state.

## Your task

Each interrupt must receive the response for its own request kind. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 06-10
uv run gym check 06-10
uv run gym hint 06-10
```

## Reading

[Module lesson](../../../../modules/06_human_in_the_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/interrupts)
