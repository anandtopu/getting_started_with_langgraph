# 03-07 — Build command routes: Suspicious evidence must affect the selected destination.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Command combines state updates with a routing instruction. Its destination annotation helps describe possible edges. A static edge still runs even when a Command chooses another node, so use one routing mechanism at a decision point.

## Your task

Suspicious evidence must affect the selected destination. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "suspicious": true
  },
  {
    "claim_id": "CLM-0001",
    "suspicious": false
  },
  {
    "claim_id": "CLM-0031",
    "suspicious": true
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 03-07
uv run gym check 03-07
uv run gym hint 03-07
```

## Reading

[Module lesson](../../../../modules/03_branching_and_routing/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-send-command)
