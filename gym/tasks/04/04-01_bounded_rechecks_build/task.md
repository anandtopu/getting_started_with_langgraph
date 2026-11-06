# 04-01 — Build bounded rechecks: Received evidence must terminate the recheck loop.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

A loop is an edge back to earlier work. Business state must move toward an exit. recursion_limit is a runtime backstop measured in graph steps, not a replacement for a document-recheck budget.

## Your task

Received evidence must terminate the recheck loop. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "history": [
      false,
      false,
      true
    ],
    "budget": 3
  },
  {
    "history": [
      true
    ],
    "budget": 3
  },
  {
    "history": [
      false
    ],
    "budget": 2
  },
  {
    "history": [
      false,
      false,
      true
    ],
    "budget": 0
  },
  {
    "history": [
      false,
      false,
      false,
      false,
      false,
      false,
      false,
      false
    ],
    "budget": 8,
    "recursion_limit": 3
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 04-01
uv run gym check 04-01
uv run gym hint 04-01
```

## Reading

[Module lesson](../../../../modules/04_loops_parallel_map_reduce/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-control-flow)
