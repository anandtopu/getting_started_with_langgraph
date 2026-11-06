# 04-09 — Predict fan out fan in across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Send creates one worker invocation per item with its own input. Parallel workers need a reducer when they write the same channel. defer waits for pending work, which matters when one branch takes more steps than another.

## Your task

Predict fan out fan in across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "documents": [
      {
        "id": "DOC-001",
        "kind": "estimate"
      },
      {
        "id": "DOC-021",
        "kind": "police"
      }
    ]
  },
  {
    "documents": []
  },
  {
    "documents": [
      {
        "id": "DOC-Z",
        "kind": "estimate"
      }
    ]
  },
  {
    "documents": [
      {
        "id": "DOC-Z",
        "kind": "police"
      },
      {
        "id": "DOC-A",
        "kind": "receipt"
      },
      {
        "id": "DOC-B",
        "kind": "police"
      }
    ]
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 04-09
uv run gym check 04-09
uv run gym hint 04-09
```

## Reading

[Module lesson](../../../../modules/04_loops_parallel_map_reduce/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-send-command)
