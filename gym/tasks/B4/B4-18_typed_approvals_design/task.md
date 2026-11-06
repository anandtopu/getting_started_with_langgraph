# B4-18 — Design typed approvals and justify the boundary policies

Type: design. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

Per-call HumanInTheLoopMiddleware emits one approval request for each gated tool call. Its response_schema describes only permitted decisions; the runtime validates the answer before saving it. Resume by interrupt ID and keep tool editing disabled when the reviewer may approve or reject only. Typed approval validates shape, while real authorization still belongs to the application.

## Your task

Design typed approvals and justify the boundary policies Implement the choices in run and complete design.md using the rubric.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B4-18
uv run gym check B4-18
uv run gym hint B4-18
```

## Reading

[Module lesson](../../../../modules/bonus/B4_whats_new/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/human-in-the-loop)
