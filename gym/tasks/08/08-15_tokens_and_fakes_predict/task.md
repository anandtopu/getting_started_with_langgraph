# 08-15 — Predict tokens and fakes across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

The messages stream emits a chunk and metadata inside each v2 part's data field. Assemble content in order and inspect langgraph_node to attribute it. A fake should agree between invoke and stream, including a structured JSON response; it tests orchestration, not model quality.

## Your task

Predict tokens and fakes across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "text": "Larkspur received your synthetic claim.",
    "structured": false
  },
  {
    "text": "Estimate received.",
    "structured": false
  },
  {
    "text": "{\"claim_type\":\"water\",\"amount_cents\":50,\"confidence\":0.9}",
    "structured": true
  },
  {
    "text": "invalid",
    "structured": true
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 08-15
uv run gym check 08-15
uv run gym hint 08-15
```

## Reading

[Module lesson](../../../../modules/08_llms_inside_nodes/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/streaming)
