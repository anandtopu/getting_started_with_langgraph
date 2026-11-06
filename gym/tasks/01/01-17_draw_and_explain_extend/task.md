# 01-17 — Extend draw and explain: Eligibility evidence must affect the validation result.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

A generated diagram shows the compiled edges rather than a hand-drawn guess. In a sequential graph each node runs in a later superstep, a batch of work that sees the previous batch's committed updates. Updates reveal which node actually ran.

## Your task

Add an eligibility node and verify both its diagram connection and runtime update. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "description": "Pipe burst"
  },
  {
    "claim_id": "CLM-0001",
    "description": ""
  },
  {
    "claim_id": "CLM-0042",
    "description": " stolen watch "
  },
  {
    "claim_id": "",
    "description": "Pipe burst"
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 01-17
uv run gym check 01-17
uv run gym hint 01-17
```

## Reading

[Module lesson](../../../../modules/01_your_first_graph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api)
