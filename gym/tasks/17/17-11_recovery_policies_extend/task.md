# 17-11 — Extend recovery policies: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

RetryPolicy repeats selected transient failures; TimeoutPolicy bounds asynchronous attempts. After retries are exhausted, a NodeError-aware handler routes to manual review. RunControl requests a cooperative drain after the current superstep, preserving a resumable boundary rather than killing in-flight work. Recovery must not invent a successful external effect.

## Your task

Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

The new capability is checked in addition to the original cases. For run_batch, edit the Python orchestration interface (including in the TypeScript bonus); leave run(case) behavior intact. A batch is sequential and each case owns a new workflow invocation, not a shared durable thread.

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 17-11
uv run gym check 17-11
uv run gym hint 17-11
```

## Reading

[Module lesson](../../../../modules/17_durable_execution/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/fault-tolerance)
