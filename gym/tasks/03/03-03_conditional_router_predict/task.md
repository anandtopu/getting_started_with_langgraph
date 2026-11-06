# 03-03 — Predict conditional router across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

A routing function chooses a label from current state. A path map connects that label to a real node. A total router has an outcome for every accepted input, including zero, missing evidence, unknown categories, and malformed amounts.

## Your task

Predict conditional router across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "claim_type": "water",
    "amount_cents": 100000,
    "missing": []
  },
  {
    "claim_type": "water",
    "amount_cents": 100001,
    "missing": []
  },
  {
    "claim_type": "water",
    "amount_cents": 500001,
    "missing": []
  },
  {
    "claim_type": "water",
    "amount_cents": 100000,
    "missing": [
      "loss_date"
    ]
  },
  {
    "claim_type": "water",
    "amount_cents": "100",
    "missing": []
  },
  {
    "claim_type": "jewelry",
    "amount_cents": 100000,
    "missing": []
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 03-03
uv run gym check 03-03
uv run gym hint 03-03
```

## Reading

[Module lesson](../../../../modules/03_branching_and_routing/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-control-flow)
