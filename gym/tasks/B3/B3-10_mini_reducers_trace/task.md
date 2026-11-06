# B3-10 — Trace mini reducers: Retain the overwrite-conflict case in the real runtime comparison.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An overwrite channel accepts one update per superstep; multiple writers need a reducer. This comparison runs the same policy and estimate findings in the mini runner and real LangGraph, normalizing their different exception classes to one conflict observation. Canonical output order is separate from the algebra used to merge writes.

## Your task

Retain the overwrite-conflict case in the real runtime comparison. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "use_reducer": true
  },
  {
    "use_reducer": false
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B3-10
uv run gym check B3-10
uv run gym hint B3-10
```

## Reading

[Module lesson](../../../../modules/bonus/B3_mini_langgraph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api)
