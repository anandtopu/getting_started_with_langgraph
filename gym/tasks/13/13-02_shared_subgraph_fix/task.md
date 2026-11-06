# 13-02 — Fix shared subgraph: Apply the high-value risk boundary inside the reusable child.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A compiled subgraph can be a parent node when their state keys agree. Its updates still meet the parent's reducers. This fraud checker is reused for claims and new policies; its idempotent flag reducer avoids duplicating shared evidence when the child returns accumulated state.

## Your task

Apply the high-value risk boundary inside the reusable child. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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
  },
  {
    "amount_cents": 600000,
    "documents": [],
    "workflow": "new_policy"
  },
  {
    "amount_cents": 600000,
    "documents": [],
    "workflow": "unknown"
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 13-02
uv run gym check 13-02
uv run gym hint 13-02
```

## Reading

[Module lesson](../../../../modules/13_subgraphs/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)
