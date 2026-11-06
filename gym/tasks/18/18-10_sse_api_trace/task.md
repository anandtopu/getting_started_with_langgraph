# 18-10 — Diagnose sse api from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An SSE frame ends with a blank line and carries JSON on its data line. JSON escaping keeps embedded newlines inside one frame. The real FastAPI routes authenticate callers, check thread ownership, and bind resumed decisions to the current interrupt ID. Reconnect by reading a snapshot; this demo does not promise durable replay from Last-Event-ID.

## Your task

Diagnose sse api from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "approved": true,
    "stale": true,
    "note": "Estimate\nreceived"
  },
  {
    "approved": false,
    "stale": true,
    "note": "Estimate\nreceived"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Preserve the exact event payload through SSE encoding."
- "Carry a rejection through the authenticated workflow."
- "Emit each progress event once, not twice."
- "Compare the payload field after decoding, not its event category."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 18-10
uv run gym check 18-10
uv run gym hint 18-10
```

## Reading

[Module lesson](../../../../modules/18_streaming_user_interfaces/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/streaming)
