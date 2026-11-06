# 18-09 — Predict sse api across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

An SSE frame ends with a blank line and carries JSON on its data line. JSON escaping keeps embedded newlines inside one frame. The real FastAPI routes authenticate callers, check thread ownership, and bind resumed decisions to the current interrupt ID. Reconnect by reading a snapshot; this demo does not promise durable replay from Last-Event-ID.

## Your task

Predict sse api across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

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
  },
  {
    "approved": true,
    "stale": true,
    "note": "Quote: \"estimate\"\nready"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 18-09
uv run gym check 18-09
uv run gym hint 18-09
```

## Reading

[Module lesson](../../../../modules/18_streaming_user_interfaces/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/streaming)
