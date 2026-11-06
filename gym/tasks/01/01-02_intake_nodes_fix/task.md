# 01-02 — Fix intake nodes: A graph node must return a mapping of state updates.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

State is the information available to a graph. TypedDict documents its keys. A node is a function that reads state and returns only the keys it changes; the graph merges those updates instead of replacing the whole state.

## Your task

A graph node must return a mapping of state updates. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "description": "  Pipe burst  ",
    "amount_cents": "125000"
  },
  {
    "claim_id": "CLM-0099",
    "description": "  Pipe burst  ",
    "amount_cents": "250"
  },
  {
    "claim_id": "CLM-0001",
    "description": " ",
    "amount_cents": "125000"
  },
  {
    "claim_id": "CLM-0001",
    "description": "  Pipe burst  ",
    "amount_cents": true
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 01-02
uv run gym check 01-02
uv run gym hint 01-02
```

## Reading

[Module lesson](../../../../modules/01_your_first_graph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api)
