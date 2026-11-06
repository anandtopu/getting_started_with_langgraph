# 13-09 — Predict schema adapters across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

When parent and child schemas differ, call the child inside an adapter node. Map the input fields explicitly, then return only the public finding. Private child fields should not become parent state just because a dictionary is convenient to copy.

## Your task

Predict schema adapters across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "amount_cents": 600000
  },
  {
    "claim_id": "CLM-0001",
    "amount_cents": 500000
  },
  {
    "claim_id": "CLM-0200",
    "amount_cents": 10000
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 13-09
uv run gym check 13-09
uv run gym hint 13-09
```

## Reading

[Module lesson](../../../../modules/13_subgraphs/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)
