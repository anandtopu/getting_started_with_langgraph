# 06-03 — Predict approve or reject across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

interrupt pauses graph work and returns a request to the caller. A checkpointer and stable thread preserve that pause. Command(resume=...) supplies the response; the interrupted node restarts, so validate the response rather than trusting its shape.

## Your task

Predict approve or reject across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

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
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 06-03
uv run gym check 06-03
uv run gym hint 06-03
```

## Reading

[Module lesson](../../../../modules/06_human_in_the_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/interrupts)
