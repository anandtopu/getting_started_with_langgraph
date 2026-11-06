# B2-12 — Refactor virtual filesystem: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.

Type: refactor. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

StateBackend stores a virtual filesystem in graph state instead of writing host files. Typed FilesystemPermission rules restrict writes to the claim directory, and checkpoints retain the resulting artifact. Tool success is checked separately from the final model sentence: a scripted acknowledgment cannot prove a denied write happened.

## Your task

Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "path": "/claims/review.txt",
    "content": "Synthetic estimate requires review."
  },
  {
    "path": "/private/key.txt",
    "content": "Synthetic estimate requires review."
  },
  {
    "path": "/claims/second.txt",
    "content": "Another synthetic finding"
  }
]
```

The starter already satisfies the original behavior cases. It fails the separate structural requirement. Keep those original tests green while changing the design; a renamed function alone does not establish the required boundary.

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B2-12
uv run gym check B2-12
uv run gym hint B2-12
```

## Reading

[Module lesson](../../../../modules/bonus/B2_deep_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/deepagents/backends)
