# 18-15 — Predict adjuster dashboard across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

The dashboard is a projection of server events: append progress and text, replace pending approvals when a new snapshot arrives. Streamlit session state remembers the selected thread between UI reruns. Client-side controls improve usability, while the API independently rejects stale or unauthorized decisions. Beta v3 typed projections are explored in B4; this UI uses stable v2-derived SSE.

## Your task

Predict adjuster dashboard across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

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
  },
  {
    "chunks": [],
    "submitted_id": "old-approval"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 18-15
uv run gym check 18-15
uv run gym hint 18-15
```

## Reading

[Module lesson](../../../../modules/18_streaming_user_interfaces/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/event-streaming)
