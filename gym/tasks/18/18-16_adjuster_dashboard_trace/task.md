# 18-16 — Diagnose adjuster dashboard from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

The dashboard is a projection of server events: append progress and text, replace pending approvals when a new snapshot arrives. Streamlit session state remembers the selected thread between UI reruns. Client-side controls improve usability, while the API independently rejects stale or unauthorized decisions. Beta v3 typed projections are explored in B4; this UI uses stable v2-derived SSE.

## Your task

Diagnose adjuster dashboard from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "chunks": [
      "Estimate ",
      "received."
    ],
    "submitted_id": "old-approval"
  },
  {
    "chunks": [
      "Estimate ",
      "received."
    ],
    "submitted_id": "current-approval"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Render every received text chunk in order."
- "Replace the stale approval identity with the current snapshot."
- "Enable submission only for a currently pending interrupt."
- "Attribute displayed progress to the node that emitted it."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 18-16
uv run gym check 18-16
uv run gym hint 18-16
```

## Reading

[Module lesson](../../../../modules/18_streaming_user_interfaces/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/event-streaming)
