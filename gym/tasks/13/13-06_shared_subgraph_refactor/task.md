# 13-06 — Refactor shared subgraph: Extract parallel fraud checks into a reusable subgraph; keep both workflow outputs and rejection cases unchanged.

Type: refactor. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

A compiled subgraph can be a parent node when their state keys agree. Its updates still meet the parent's reducers. This fraud checker is reused for claims and new policies; its idempotent flag reducer avoids duplicating shared evidence when the child returns accumulated state.

## Your task

Extract parallel fraud checks into a reusable subgraph; keep both workflow outputs and rejection cases unchanged. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

The starter already satisfies the original behavior cases. It fails the separate structural requirement. Keep those original tests green while changing the design; a renamed function alone does not establish the required boundary.

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 13-06
uv run gym check 13-06
uv run gym hint 13-06
```

## Reading

[Module lesson](../../../../modules/13_subgraphs/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)
