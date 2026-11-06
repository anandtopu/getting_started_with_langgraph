# 07-10 — Trace v2 stream parts: The state payload is inside data, not at the envelope root.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A v2 stream part has type, ns, and data fields. Updates contain a node's changed fields; values contain the visible whole state; custom events carry application progress. Interrupt metadata is separate from ordinary values and must survive UI serialization.

## Your task

The state payload is inside data, not at the envelope root. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "review": false
  },
  {
    "claim_id": "CLM-0001",
    "review": true
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 07-10
uv run gym check 07-10
uv run gym hint 07-10
```

## Reading

[Module lesson](../../../../modules/07_time_travel_and_streaming/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/streaming)
