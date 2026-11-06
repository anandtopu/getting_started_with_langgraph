# 19-03 — Predict test graph behavior across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

A pytest test is a function whose assertions express requirements. Parametrized tests run it over many inputs. Compare pure node rules and whole graphs against independently specified boundary outcomes; comparing two copies of the same implementation can preserve the same bug. Fake models make orchestration tests repeatable, not model accuracy measurable.

## Your task

Predict test graph behavior across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "amounts": [
      100000,
      100001,
      500001,
      true
    ]
  },
  {
    "amounts": [
      0,
      -1,
      500000
    ]
  },
  {
    "amounts": []
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 19-03
uv run gym check 19-03
uv run gym hint 19-03
```

## Reading

[Module lesson](../../../../modules/19_testing_and_evaluation/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/test)
