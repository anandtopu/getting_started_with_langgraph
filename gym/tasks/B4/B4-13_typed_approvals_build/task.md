# B4-13 — Build typed approvals: Use per-call requests when resuming individual interrupt IDs.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Per-call HumanInTheLoopMiddleware emits one approval request for each gated tool call. Its response_schema describes only permitted decisions; the runtime validates the answer before saving it. Resume by interrupt ID and keep tool editing disabled when the reviewer may approve or reject only. Typed approval validates shape, while real authorization still belongs to the application.

## Your task

Use per-call requests when resuming individual interrupt IDs. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "decision": "approve",
    "amount_cents": 50000
  },
  {
    "decision": "reject",
    "amount_cents": 50000
  },
  {
    "decision": "edit",
    "amount_cents": 50000
  },
  {
    "decision": "approve",
    "amount_cents": 0
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B4-13
uv run gym check B4-13
uv run gym hint B4-13
```

## Reading

[Module lesson](../../../../modules/bonus/B4_whats_new/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/human-in-the-loop)
