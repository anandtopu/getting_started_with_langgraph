# 03-10 — Diagnose command routes from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Command combines state updates with a routing instruction. Its destination annotation helps describe possible edges. A static edge still runs even when a Command chooses another node, so use one routing mechanism at a decision point.

## Your task

Diagnose command routes from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "suspicious": true
  },
  {
    "claim_id": "CLM-0001",
    "suspicious": false
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Suspicious evidence must affect the selected destination."
- "A competing static edge schedules an extra acknowledgment."
- "The recorded reason must explain the actual decision."
- "Equivalent control flow must not duplicate work."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 03-10
uv run gym check 03-10
uv run gym hint 03-10
```

## Reading

[Module lesson](../../../../modules/03_branching_and_routing/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-send-command)
