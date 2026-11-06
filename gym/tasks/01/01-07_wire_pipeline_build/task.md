# 01-07 — Build wire pipeline: The acknowledgment must be reachable.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Edges declare which node can run next. START is the entry point and END marks termination. compile checks the graph and creates an executable object. Explicit v2 invoke returns GraphOutput; its value is the final state.

## Your task

The acknowledgment must be reachable. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "description": " Water leak ",
    "steps": []
  },
  {
    "claim_id": "CLM-0001",
    "description": " ",
    "steps": []
  },
  {
    "claim_id": "CLM-0098",
    "description": " theft ",
    "steps": []
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 01-07
uv run gym check 01-07
uv run gym hint 01-07
```

## Reading

[Module lesson](../../../../modules/01_your_first_graph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-control-flow)
