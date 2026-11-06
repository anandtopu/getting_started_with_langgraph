# 19-17 — Extend trajectory evals: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

A trajectory is the sequence of tool requests, separate from the final answer. agentevals can compare strict order, unordered calls, subsets, or supersets. Exact argument matching catches the right tool used on the wrong policy. Choose the matching rule from the business requirement; parallel independent calls may legitimately change order.

## Your task

Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "tools": [
      "lookup_policy",
      "check_coverage"
    ],
    "mode": "strict",
    "policy_id": "POL-0001"
  },
  {
    "tools": [
      "check_coverage",
      "lookup_policy"
    ],
    "mode": "strict",
    "policy_id": "POL-0001"
  },
  {
    "tools": [
      "check_coverage",
      "lookup_policy"
    ],
    "mode": "unordered",
    "policy_id": "POL-0001"
  },
  {
    "tools": [
      "lookup_policy",
      "check_coverage"
    ],
    "mode": "strict",
    "policy_id": "POL-0002"
  }
]
```

The new capability is checked in addition to the original cases. For run_batch, edit the Python orchestration interface (including in the TypeScript bonus); leave run(case) behavior intact. A batch is sequential and each case owns a new workflow invocation, not a shared durable thread.

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 19-17
uv run gym check 19-17
uv run gym hint 19-17
```

## Reading

[Module lesson](../../../../modules/19_testing_and_evaluation/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/test)
