# 00-11 — Extend environment: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

An environment is the interpreter and packages used by one command. A package installed for another interpreter is still missing here. An optional live provider must not block a deterministic checklist.

## Your task

Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "python": [
      3,
      12
    ],
    "packages": [
      "langgraph",
      "pytest"
    ],
    "data_present": true,
    "live": false,
    "provider_ready": false
  },
  {
    "python": [
      3,
      12
    ],
    "packages": [
      "langgraph",
      "pytest"
    ],
    "data_present": true,
    "live": true,
    "provider_ready": false
  },
  {
    "python": [
      3,
      12
    ],
    "packages": [
      "langgraph",
      "pytest"
    ],
    "data_present": false,
    "live": false,
    "provider_ready": false
  },
  {
    "python": [
      3,
      12
    ],
    "packages": [],
    "data_present": true,
    "live": false,
    "provider_ready": false
  },
  {
    "python": [
      3,
      10
    ],
    "packages": [
      "langgraph",
      "pytest"
    ],
    "data_present": true,
    "live": false,
    "provider_ready": false
  }
]
```

The new capability is checked in addition to the original cases. For run_batch, edit the Python orchestration interface (including in the TypeScript bonus); leave run(case) behavior intact. A batch is sequential and each case owns a new workflow invocation, not a shared durable thread.

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 00-11
uv run gym check 00-11
uv run gym hint 00-11
```

## Reading

[Module lesson](../../../../modules/00_setup/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/overview)
