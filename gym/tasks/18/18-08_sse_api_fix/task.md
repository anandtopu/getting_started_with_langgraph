# 18-08 — Fix sse api: Carry a rejection through the authenticated workflow.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An SSE frame ends with a blank line and carries JSON on its data line. JSON escaping keeps embedded newlines inside one frame. The real FastAPI routes authenticate callers, check thread ownership, and bind resumed decisions to the current interrupt ID. Reconnect by reading a snapshot; this demo does not promise durable replay from Last-Event-ID.

## Your task

Carry a rejection through the authenticated workflow. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 18-08
uv run gym check 18-08
uv run gym hint 18-08
```

## Reading

[Module lesson](../../../../modules/18_streaming_user_interfaces/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/streaming)
