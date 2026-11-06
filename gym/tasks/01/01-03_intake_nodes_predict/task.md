# 01-03 — Predict intake nodes across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

State is the information available to a graph. TypedDict documents its keys. A node is a function that reads state and returns only the keys it changes; the graph merges those updates instead of replacing the whole state.

## Your task

Predict intake nodes across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "description": "  Pipe burst  ",
    "amount_cents": "125000"
  },
  {
    "claim_id": "CLM-0099",
    "description": "  Pipe burst  ",
    "amount_cents": "250"
  },
  {
    "claim_id": "CLM-0001",
    "description": " ",
    "amount_cents": "125000"
  },
  {
    "claim_id": "CLM-0001",
    "description": "  Pipe burst  ",
    "amount_cents": true
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 01-03
uv run gym check 01-03
uv run gym hint 01-03
```

## Reading

[Module lesson](../../../../modules/01_your_first_graph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api)
