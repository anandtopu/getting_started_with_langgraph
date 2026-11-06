# 02-04 — Trace schema contracts: Use Pydantic field access or model_dump instead of losing validated values.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

TypedDict describes a dictionary for type checking; it does not validate values at runtime. Dataclasses give attribute access and defaults. Pydantic checks fields at the boundary. With explicit v2 output, preserve the schema's object type before extracting its fields.

## Your task

Use Pydantic field access or model_dump instead of losing validated values. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "kind": "pydantic",
    "amount_cents": 125000,
    "claim_id": "CLM-0001"
  },
  {
    "kind": "typed",
    "amount_cents": 125000,
    "claim_id": "CLM-0001"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 02-04
uv run gym check 02-04
uv run gym hint 02-04
```

## Reading

[Module lesson](../../../../modules/02_state_and_reducers/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-state)
