# B2-10 — Trace virtual filesystem: Deny writes outside the permitted virtual directory.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

StateBackend stores a virtual filesystem in graph state instead of writing host files. Typed FilesystemPermission rules restrict writes to the claim directory, and checkpoints retain the resulting artifact. Tool success is checked separately from the final model sentence: a scripted acknowledgment cannot prove a denied write happened.

## Your task

Deny writes outside the permitted virtual directory. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B2-10
uv run gym check B2-10
uv run gym hint B2-10
```

## Reading

[Module lesson](../../../../modules/bonus/B2_deep_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/deepagents/backends)
