# 15-13 — Build functional resume: Use a task boundary so completed evidence can be reused during replay.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Resuming a Functional API interrupt restarts the entrypoint from its beginning. Completed task results are retrieved from checkpoints, so the task body need not run again. Keep task ordering deterministic and validate the resume payload. External effects still require their own idempotency at the crash window.

## Your task

Use a task boundary so completed evidence can be reused during replay. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "approved": true
  },
  {
    "claim_id": "CLM-0001",
    "approved": false
  },
  {
    "claim_id": "CLM-0001",
    "approved": "yes"
  },
  {
    "claim_id": "CLM-0077",
    "approved": true
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 15-13
uv run gym check 15-13
uv run gym hint 15-13
```

## Reading

[Module lesson](../../../../modules/15_functional_api/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/functional-api)
