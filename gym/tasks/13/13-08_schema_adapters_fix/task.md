# 13-08 — Fix schema adapters: Preserve the exact review threshold.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

When parent and child schemas differ, call the child inside an adapter node. Map the input fields explicitly, then return only the public finding. Private child fields should not become parent state just because a dictionary is convenient to copy.

## Your task

Preserve the exact review threshold. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "amount_cents": 600000
  },
  {
    "claim_id": "CLM-0001",
    "amount_cents": 500000
  },
  {
    "claim_id": "CLM-0200",
    "amount_cents": 10000
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 13-08
uv run gym check 13-08
uv run gym hint 13-08
```

## Reading

[Module lesson](../../../../modules/13_subgraphs/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)
