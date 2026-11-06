# B4-16 — Diagnose typed approvals from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Per-call HumanInTheLoopMiddleware emits one approval request for each gated tool call. Its response_schema describes only permitted decisions; the runtime validates the answer before saving it. Resume by interrupt ID and keep tool editing disabled when the reviewer may approve or reject only. Typed approval validates shape, while real authorization still belongs to the application.

## Your task

Diagnose typed approvals from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

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
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Use per-call requests when resuming individual interrupt IDs."
- "Respect rejection instead of coercing every decision to approval."
- "Bind the proposal to its requested amount."
- "Record one effect for one approved tool execution."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B4-16
uv run gym check B4-16
uv run gym hint B4-16
```

## Reading

[Module lesson](../../../../modules/bonus/B4_whats_new/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/human-in-the-loop)
