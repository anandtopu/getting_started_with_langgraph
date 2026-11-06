# 11-16 — Diagnose semantic and privacy from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An embedding maps text into numbers so the Store can rank similarity within a namespace. These transparent word vectors make the offline ranking reproducible. Store deletion does not delete old checkpoint contents: retention must handle both systems separately. Retrieval is evidence selection, never an authorization check.

## Your task

Diagnose semantic and privacy from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "query": "water leak",
    "customer_id": "CUS-0001"
  },
  {
    "query": "theft",
    "customer_id": "CUS-0001"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Scope semantic search to the authenticated customer."
- "Delete checkpoint history separately from Store records."
- "Delete the requested memory while preserving unrelated evidence."
- "Rank the highest similarity first with a stable tie-breaker."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 11-16
uv run gym check 11-16
uv run gym hint 11-16
```

## Reading

[Module lesson](../../../../modules/11_memory/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/memory)
