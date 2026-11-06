# 19-10 — Diagnose test durable execution from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Durable tests assert the state before a pause, the pending node, and the resumed result. Snapshot only stable semantic fields, not random checkpoint IDs or timestamps. Reducer algebra can be checked over many generated inputs: associativity and idempotence protect parallel and replay behavior. The process-death test in module 17 covers a failure an in-memory mock cannot reproduce.

## Your task

Diagnose test durable execution from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

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
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Test rejection as well as approval on resume."
- "Capture the pre-resume pending state before it changes."
- "Include every update group when checking reducer behavior."
- "Read the completed snapshot after resumption."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 19-10
uv run gym check 19-10
uv run gym hint 19-10
```

## Reading

[Module lesson](../../../../modules/19_testing_and_evaluation/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/test)
