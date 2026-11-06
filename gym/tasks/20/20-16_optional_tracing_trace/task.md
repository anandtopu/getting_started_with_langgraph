# 20-16 — Diagnose optional tracing from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

LangSmith tracing is optional and independent of checkpoint persistence. A local trace can show an old route, locate the checkpoint before routing, fork with corrected data, and retain the original history. This example explicitly disables remote tracing. Enable hosted tracing only for sanitized data and an account you intend to use.

## Your task

Diagnose optional tracing from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "corrected_cents": 50000
  },
  {
    "corrected_cents": 600000
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Apply the corrected amount to the fork before resuming routing."
- "Fork at the intended pre-routing boundary."
- "Keep the original route distinct from the corrected branch."
- "Verify that branching retains and extends checkpoint history."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 20-16
uv run gym check 20-16
uv run gym hint 20-16
```

## Reading

[Module lesson](../../../../modules/20_observability_and_debugging/README.md) · [Official guide](https://docs.langchain.com/langsmith/observability)
