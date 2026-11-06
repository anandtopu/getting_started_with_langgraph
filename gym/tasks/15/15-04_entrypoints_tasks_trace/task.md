# 15-04 — Trace entrypoints tasks: Match the Graph API fast-track boundary.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An entrypoint accepts one serializable input and uses ordinary Python branches. A task call schedules durable work and returns a future; result() obtains its value. This supports familiar control flow without removing the need for validated inputs and deterministic replay order.

## Your task

Match the Graph API fast-track boundary. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "description": "  Pipe burst  ",
    "amount_cents": 125000
  },
  {
    "claim_id": "CLM-0001",
    "description": "  Pipe burst  ",
    "amount_cents": 100000
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 15-04
uv run gym check 15-04
uv run gym hint 15-04
```

## Reading

[Module lesson](../../../../modules/15_functional_api/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/functional-api)
