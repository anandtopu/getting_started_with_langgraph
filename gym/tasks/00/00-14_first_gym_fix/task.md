# 00-14 — Fix first gym: Labels need case normalization before comparison.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An assertion compares an observed result with an explicit requirement. A failing starter is useful when it runs and shows a wrong business result. Hints guide a repair; viewing a solution is recorded separately from independent work.

## Your task

Labels need case normalization before comparison. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "claim_type": " Water ",
    "claim_id": "CLM-0001"
  },
  {
    "claim_type": "THEFT",
    "claim_id": "CLM-0001"
  },
  {
    "claim_type": null,
    "claim_id": "CLM-0001"
  },
  {
    "claim_type": "  storm  ",
    "claim_id": "CLM-0001"
  },
  {
    "claim_type": "unlisted",
    "claim_id": "CLM-0001"
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 00-14
uv run gym check 00-14
uv run gym hint 00-14
```

## Reading

[Module lesson](../../../../modules/00_setup/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/test)
