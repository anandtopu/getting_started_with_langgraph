# 18-04 — Diagnose async streams from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

ainvoke awaits one result; astream yields intermediate parts. Pass RunnableConfig into async model calls for explicit context propagation. The seven v2 modes expose different views, so count types rather than assuming one common payload. Cancellation must await cleanup; a browser disconnect is not proof that an external effect was rolled back.

## Your task

Diagnose async streams from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "text": "Your estimate is ready.",
    "cancel": true
  },
  {
    "text": "Documents ready.",
    "cancel": false
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Accumulate chunks instead of replacing the previous text."
- "Request the intended seven stream projections."
- "Cancel and await the pending async graph when requested."
- "Record cleanup after the waiting node receives cancellation."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 18-04
uv run gym check 18-04
uv run gym hint 18-04
```

## Reading

[Module lesson](../../../../modules/18_streaming_user_interfaces/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/streaming)
