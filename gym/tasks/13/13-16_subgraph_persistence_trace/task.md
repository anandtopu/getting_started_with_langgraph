# 13-16 — Diagnose subgraph persistence from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A parent checkpointer propagates into its child. A child compiled with the default per-invocation behavior starts fresh for each invocation; checkpointer=True gives the child persistent state across calls. While paused, get_state(subgraphs=True) exposes the nested task snapshot. Streaming namespaces identify which graph emitted an update.

## Your task

Diagnose subgraph persistence from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "approved": false,
    "persistent_child": false
  },
  {
    "claim_id": "CLM-0001",
    "approved": true,
    "persistent_child": false
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Request nested snapshots when inspecting child state."
- "Reject a string masquerading as a human decision."
- "Include nested updates when streaming subgraphs."
- "Carry the actual human approval through the child boundary."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 13-16
uv run gym check 13-16
uv run gym hint 13-16
```

## Reading

[Module lesson](../../../../modules/13_subgraphs/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)
