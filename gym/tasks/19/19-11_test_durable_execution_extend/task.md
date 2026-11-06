# 19-11 — Extend test durable execution: Include every update group when checking reducer behavior.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

Durable tests assert the state before a pause, the pending node, and the resumed result. Snapshot only stable semantic fields, not random checkpoint IDs or timestamps. Reducer algebra can be checked over many generated inputs: associativity and idempotence protect parallel and replay behavior. The process-death test in module 17 covers a failure an in-memory mock cannot reproduce.

## Your task

Include every update group when checking reducer behavior. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "approved": false,
    "groups": [
      [
        "receipt"
      ],
      [
        "estimate",
        "receipt"
      ],
      [
        "policy"
      ]
    ]
  },
  {
    "approved": true,
    "groups": [
      [
        "receipt"
      ],
      [
        "estimate",
        "receipt"
      ],
      [
        "policy"
      ]
    ]
  },
  {
    "approved": false,
    "groups": [
      [],
      [
        "receipt"
      ],
      [
        "receipt"
      ]
    ]
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 19-11
uv run gym check 19-11
uv run gym hint 19-11
```

## Reading

[Module lesson](../../../../modules/19_testing_and_evaluation/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/test)
