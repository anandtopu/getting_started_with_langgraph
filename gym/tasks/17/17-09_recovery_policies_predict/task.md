# 17-09 — Predict recovery policies across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

RetryPolicy repeats selected transient failures; TimeoutPolicy bounds asynchronous attempts. After retries are exhausted, a NodeError-aware handler routes to manual review. RunControl requests a cooperative drain after the current superstep, preserving a resumable boundary rather than killing in-flight work. Recovery must not invent a successful external effect.

## Your task

Predict recovery policies across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "failures": 1,
    "timeout": false,
    "drain": true
  },
  {
    "failures": 3,
    "timeout": false,
    "drain": true
  },
  {
    "failures": 1,
    "timeout": true,
    "drain": true
  },
  {
    "failures": 0,
    "timeout": false,
    "drain": false
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 17-09
uv run gym check 17-09
uv run gym hint 17-09
```

## Reading

[Module lesson](../../../../modules/17_durable_execution/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/fault-tolerance)
