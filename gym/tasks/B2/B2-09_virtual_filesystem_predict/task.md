# B2-09 — Predict virtual filesystem across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

StateBackend stores a virtual filesystem in graph state instead of writing host files. Typed FilesystemPermission rules restrict writes to the claim directory, and checkpoints retain the resulting artifact. Tool success is checked separately from the final model sentence: a scripted acknowledgment cannot prove a denied write happened.

## Your task

Predict virtual filesystem across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B2-09
uv run gym check B2-09
uv run gym hint B2-09
```

## Reading

[Module lesson](../../../../modules/bonus/B2_deep_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/deepagents/backends)
