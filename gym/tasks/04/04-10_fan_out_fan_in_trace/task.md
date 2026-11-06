# 04-10 — Diagnose fan out fan in from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Send creates one worker invocation per item with its own input. Parallel workers need a reducer when they write the same channel. defer waits for pending work, which matters when one branch takes more steps than another.

## Your task

Diagnose fan out fan in from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "documents": [
      {
        "id": "DOC-001",
        "kind": "estimate"
      },
      {
        "id": "DOC-021",
        "kind": "police"
      }
    ]
  },
  {
    "documents": []
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Each worker must contribute its own document evidence."
- "Parallel writes to an overwrite channel conflict."
- "The deeper police branch must finish before summary."
- "Do not treat arrival order as the public result order."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 04-10
uv run gym check 04-10
uv run gym hint 04-10
```

## Reading

[Module lesson](../../../../modules/04_loops_parallel_map_reduce/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-send-command)
