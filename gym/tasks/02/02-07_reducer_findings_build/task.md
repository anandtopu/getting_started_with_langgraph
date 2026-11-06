# 02-07 — Build reducer findings: A merge must preserve evidence from earlier updates.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

A channel is one state field together with its update rule. The default rule overwrites. An Annotated reducer combines the old and new values. Associativity means grouping updates differently does not change the result, which matters when branches complete in batches.

## Your task

A merge must preserve evidence from earlier updates. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "first": {
      "id": "receipt",
      "severity": 1
    },
    "second": {
      "id": "receipt",
      "severity": 3
    }
  },
  {
    "first": {
      "id": "receipt",
      "severity": 1
    },
    "second": {
      "id": "estimate",
      "severity": 2
    }
  },
  {
    "first": {
      "id": "receipt",
      "severity": 4
    },
    "second": {
      "id": "receipt",
      "severity": 3
    }
  },
  {
    "first": {
      "id": "z",
      "severity": 1
    },
    "second": {
      "id": "a",
      "severity": 2
    }
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 02-07
uv run gym check 02-07
uv run gym hint 02-07
```

## Reading

[Module lesson](../../../../modules/02_state_and_reducers/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-state)
