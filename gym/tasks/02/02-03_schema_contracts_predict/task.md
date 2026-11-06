# 02-03 — Predict schema contracts across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

TypedDict describes a dictionary for type checking; it does not validate values at runtime. Dataclasses give attribute access and defaults. Pydantic checks fields at the boundary. With explicit v2 output, preserve the schema's object type before extracting its fields.

## Your task

Predict schema contracts across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

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
  },
  {
    "kind": "dataclass",
    "amount_cents": 125000,
    "claim_id": "CLM-0001"
  },
  {
    "kind": "pydantic",
    "amount_cents": -1,
    "claim_id": "CLM-0001"
  },
  {
    "kind": "pydantic",
    "amount_cents": true,
    "claim_id": "CLM-0001"
  },
  {
    "kind": "typed",
    "amount_cents": 0,
    "claim_id": "CLM-0001"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 02-03
uv run gym check 02-03
uv run gym hint 02-03
```

## Reading

[Module lesson](../../../../modules/02_state_and_reducers/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-state)
