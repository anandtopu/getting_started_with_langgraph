# B1-10 — Diagnose typescript durable from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

JavaScript Send fans out document work, SqliteSaver retains the approval pause, and Command resumes it. The saver connection is explicitly closed. JavaScript uses camelCase options such as streamMode and returns its documented update shape; this lesson intentionally does not copy Python invocation parameters.

## Your task

Diagnose typescript durable from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "documents": [
      "estimate",
      "receipt"
    ],
    "approved": false
  },
  {
    "documents": [],
    "approved": true
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Review every document before the approval step."
- "Accept explicit boolean decisions and reject strings at the interrupt boundary."
- "Preserve a rejected approval through JavaScript resume."
- "Combine all parallel findings rather than retaining only the last write."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B1-10
uv run gym check B1-10
uv run gym hint B1-10
```

## Reading

[Module lesson](../../../../modules/bonus/B1_langgraph_js/README.md) · [Official guide](https://docs.langchain.com/oss/javascript/langgraph/interrupts)
