# 20-11 — Extend structured logs: Retain the caller's thread correlation identifier.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

Structured logs are small machine-readable records correlated by thread and run. An allowlist excludes raw prompts, contact details, and credentials rather than hoping a redactor recognizes every secret. Random run identifiers belong in operational logs but should be normalized out of teaching snapshots.

## Your task

Retain the caller's thread correlation identifier. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "thread_id": "claim-thread",
    "run_id": "review-1",
    "description": "Synthetic contact: 555-0100",
    "api_key": "synthetic-secret"
  },
  {
    "thread_id": "second-claim",
    "run_id": "review-2",
    "description": "Synthetic contact: 555-0100",
    "api_key": "synthetic-secret"
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 20-11
uv run gym check 20-11
uv run gym hint 20-11
```

## Reading

[Module lesson](../../../../modules/20_observability_and_debugging/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/pregel)
