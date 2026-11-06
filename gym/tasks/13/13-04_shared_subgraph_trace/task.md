# 13-04 — Trace shared subgraph: Apply the high-value risk boundary inside the reusable child.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A compiled subgraph can be a parent node when their state keys agree. Its updates still meet the parent's reducers. This fraud checker is reused for claims and new policies; its idempotent flag reducer avoids duplicating shared evidence when the child returns accumulated state.

## Your task

Apply the high-value risk boundary inside the reusable child. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "amount_cents": 600000,
    "documents": [],
    "workflow": "claim"
  },
  {
    "amount_cents": 100000,
    "documents": [
      "estimate"
    ],
    "workflow": "claim"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 13-04
uv run gym check 13-04
uv run gym hint 13-04
```

## Reading

[Module lesson](../../../../modules/13_subgraphs/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)
