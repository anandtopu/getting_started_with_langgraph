# B2-10 — Diagnose virtual filesystem from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

StateBackend stores a virtual filesystem in graph state instead of writing host files. Typed FilesystemPermission rules restrict writes to the claim directory, and checkpoints retain the resulting artifact. Tool success is checked separately from the final model sentence: a scripted acknowledgment cannot prove a denied write happened.

## Your task

Diagnose virtual filesystem from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

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

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Allow the explicitly scoped claim artifact path."
- "Deny writes outside the permitted virtual directory."
- "Persist the supplied investigation note without substitution."
- "Honor and validate the requested virtual artifact path."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B2-10
uv run gym check B2-10
uv run gym hint B2-10
```

## Reading

[Module lesson](../../../../modules/bonus/B2_deep_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/deepagents/backends)
