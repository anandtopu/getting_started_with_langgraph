# 03-05 — Extend conditional router: High-value claims require specialist review.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

A routing function chooses a label from current state. A path map connects that label to a real node. A total router has an outcome for every accepted input, including zero, missing evidence, unknown categories, and malformed amounts.

## Your task

Add a distinct jewelry-specialist path while preserving amount and missing-evidence guards. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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
  },
  {
    "claim_type": "jewelry",
    "amount_cents": 50000,
    "missing": []
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 03-05
uv run gym check 03-05
uv run gym hint 03-05
```

## Reading

[Module lesson](../../../../modules/03_branching_and_routing/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-control-flow)
