# 03-09 — Predict command routes across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Command combines state updates with a routing instruction. Its destination annotation helps describe possible edges. A static edge still runs even when a Command chooses another node, so use one routing mechanism at a decision point.

## Your task

Predict command routes across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "suspicious": true
  },
  {
    "claim_id": "CLM-0001",
    "suspicious": false
  },
  {
    "claim_id": "CLM-0031",
    "suspicious": true
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 03-09
uv run gym check 03-09
uv run gym hint 03-09
```

## Reading

[Module lesson](../../../../modules/03_branching_and_routing/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-send-command)
