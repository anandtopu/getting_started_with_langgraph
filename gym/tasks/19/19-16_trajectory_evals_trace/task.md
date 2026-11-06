# 19-16 — Diagnose trajectory evals from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A trajectory is the sequence of tool requests, separate from the final answer. agentevals can compare strict order, unordered calls, subsets, or supersets. Exact argument matching catches the right tool used on the wrong policy. Choose the matching rule from the business requirement; parallel independent calls may legitimately change order.

## Your task

Diagnose trajectory evals from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

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
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Respect strict ordering when the evaluation contract requests it."
- "Check the policy arguments, not only tool names."
- "Evaluate the actual requested policy instead of replacing it with the reference."
- "Preserve the evaluator's boolean score in the report."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 19-16
uv run gym check 19-16
uv run gym hint 19-16
```

## Reading

[Module lesson](../../../../modules/19_testing_and_evaluation/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/test)
