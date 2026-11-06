# 11-15 — Predict semantic and privacy across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

An embedding maps text into numbers so the Store can rank similarity within a namespace. These transparent word vectors make the offline ranking reproducible. Store deletion does not delete old checkpoint contents: retention must handle both systems separately. Retrieval is evidence selection, never an authorization check.

## Your task

Predict semantic and privacy across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

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
  },
  {
    "query": "unrelated",
    "customer_id": "CUS-0040"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 11-15
uv run gym check 11-15
uv run gym hint 11-15
```

## Reading

[Module lesson](../../../../modules/11_memory/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/memory)
