# 13-17 — Extend subgraph persistence: Include nested updates when streaming subgraphs.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

A parent checkpointer propagates into its child. A child compiled with the default per-invocation behavior starts fresh for each invocation; checkpointer=True gives the child persistent state across calls. While paused, get_state(subgraphs=True) exposes the nested task snapshot. Streaming namespaces identify which graph emitted an update.

## Your task

Include nested updates when streaming subgraphs. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "approved": false,
    "persistent_child": false
  },
  {
    "claim_id": "CLM-0001",
    "approved": true,
    "persistent_child": false
  },
  {
    "claim_id": "CLM-0001",
    "approved": false,
    "persistent_child": true
  },
  {
    "claim_id": "CLM-0001",
    "approved": "yes",
    "persistent_child": false
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 13-17
uv run gym check 13-17
uv run gym hint 13-17
```

## Reading

[Module lesson](../../../../modules/13_subgraphs/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)
