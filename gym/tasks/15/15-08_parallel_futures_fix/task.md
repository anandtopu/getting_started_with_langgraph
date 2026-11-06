# 15-08 — Fix parallel futures: Preserve every parallel graph result.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Create all task futures before resolving them to allow concurrent work. Collect results in a canonical order so scheduling differences do not change the business answer. The equivalent Send graph lets you compare the same finding function across the Graph and Functional APIs, including an empty document list.

## Your task

Preserve every parallel graph result. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 15-08
uv run gym check 15-08
uv run gym hint 15-08
```

## Reading

[Module lesson](../../../../modules/15_functional_api/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/functional-api)
