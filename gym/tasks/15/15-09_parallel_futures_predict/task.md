# 15-09 — Predict parallel futures across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Create all task futures before resolving them to allow concurrent work. Collect results in a canonical order so scheduling differences do not change the business answer. The equivalent Send graph lets you compare the same finding function across the Graph and Functional APIs, including an empty document list.

## Your task

Predict parallel futures across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "documents": [
      "estimate",
      "receipt",
      "police_report"
    ]
  },
  {
    "documents": []
  },
  {
    "documents": [
      "receipt",
      "estimate"
    ]
  },
  {
    "documents": [
      "police_report"
    ]
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 15-09
uv run gym check 15-09
uv run gym hint 15-09
```

## Reading

[Module lesson](../../../../modules/15_functional_api/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/functional-api)
