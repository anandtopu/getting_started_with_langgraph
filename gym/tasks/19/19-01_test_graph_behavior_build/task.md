# 19-01 — Build test graph behavior: Specify the inclusive fast-track boundary in the test oracle.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

A pytest test is a function whose assertions express requirements. Parametrized tests run it over many inputs. Compare pure node rules and whole graphs against independently specified boundary outcomes; comparing two copies of the same implementation can preserve the same bug. Fake models make orchestration tests repeatable, not model accuracy measurable.

## Your task

Specify the inclusive fast-track boundary in the test oracle. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 19-01
uv run gym check 19-01
uv run gym hint 19-01
```

## Reading

[Module lesson](../../../../modules/19_testing_and_evaluation/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/test)
