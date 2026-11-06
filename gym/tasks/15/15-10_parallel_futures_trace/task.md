# 15-10 — Trace parallel futures: Preserve every parallel graph result.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Create all task futures before resolving them to allow concurrent work. Collect results in a canonical order so scheduling differences do not change the business answer. The equivalent Send graph lets you compare the same finding function across the Graph and Functional APIs, including an empty document list.

## Your task

Preserve every parallel graph result. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 15-10
uv run gym check 15-10
uv run gym hint 15-10
```

## Reading

[Module lesson](../../../../modules/15_functional_api/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/functional-api)
