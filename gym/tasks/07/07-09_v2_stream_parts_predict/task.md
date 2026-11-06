# 07-09 — Predict v2 stream parts across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

A v2 stream part has type, ns, and data fields. Updates contain a node's changed fields; values contain the visible whole state; custom events carry application progress. Interrupt metadata is separate from ordinary values and must survive UI serialization.

## Your task

Predict v2 stream parts across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "review": false
  },
  {
    "claim_id": "CLM-0001",
    "review": true
  },
  {
    "claim_id": "CLM-0040",
    "review": false
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 07-09
uv run gym check 07-09
uv run gym hint 07-09
```

## Reading

[Module lesson](../../../../modules/07_time_travel_and_streaming/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/streaming)
