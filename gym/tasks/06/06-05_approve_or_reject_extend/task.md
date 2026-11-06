# 06-05 — Extend approve or reject: Only a validated boolean authorizes this synthetic decision.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

interrupt pauses graph work and returns a request to the caller. A checkpointer and stable thread preserve that pause. Command(resume=...) supplies the response; the interrupted node restarts, so validate the response rather than trusting its shape.

## Your task

Validate adjuster identity from the trusted invocation configuration, independently of the response payload. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "amount_cents": 600000,
    "decision": {
      "approved": true
    }
  },
  {
    "amount_cents": 600000,
    "decision": {
      "approved": false
    }
  },
  {
    "amount_cents": 600000,
    "decision": {
      "approved": "yes"
    }
  },
  {
    "amount_cents": 1000000,
    "decision": {
      "approved": true
    }
  },
  {
    "amount_cents": 600000,
    "decision": {
      "approved": true,
      "adjuster_id": "ADJ-001"
    },
    "adjuster_id": "unknown"
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 06-05
uv run gym check 06-05
uv run gym hint 06-05
```

## Reading

[Module lesson](../../../../modules/06_human_in_the_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/interrupts)
