# B2-11 — Extend virtual filesystem: Persist the supplied investigation note without substitution.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

StateBackend stores a virtual filesystem in graph state instead of writing host files. Typed FilesystemPermission rules restrict writes to the claim directory, and checkpoints retain the resulting artifact. Tool success is checked separately from the final model sentence: a scripted acknowledgment cannot prove a denied write happened.

## Your task

Persist the supplied investigation note without substitution. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B2-11
uv run gym check B2-11
uv run gym hint B2-11
```

## Reading

[Module lesson](../../../../modules/bonus/B2_deep_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/deepagents/backends)
