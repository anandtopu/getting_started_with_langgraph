# 00-15 — Predict first gym across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

An assertion compares an observed result with an explicit requirement. A failing starter is useful when it runs and shows a wrong business result. Hints guide a repair; viewing a solution is recorded separately from independent work.

## Your task

Predict first gym across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "claim_type": " Water ",
    "claim_id": "CLM-0001"
  },
  {
    "claim_type": "THEFT",
    "claim_id": "CLM-0001"
  },
  {
    "claim_type": null,
    "claim_id": "CLM-0001"
  },
  {
    "claim_type": "  storm  ",
    "claim_id": "CLM-0001"
  },
  {
    "claim_type": "unlisted",
    "claim_id": "CLM-0001"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 00-15
uv run gym check 00-15
uv run gym hint 00-15
```

## Reading

[Module lesson](../../../../modules/00_setup/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/test)
