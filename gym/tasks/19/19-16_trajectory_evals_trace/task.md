# 19-16 — Trace trajectory evals: Check the policy arguments, not only tool names.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A trajectory is the sequence of tool requests, separate from the final answer. agentevals can compare strict order, unordered calls, subsets, or supersets. Exact argument matching catches the right tool used on the wrong policy. Choose the matching rule from the business requirement; parallel independent calls may legitimately change order.

## Your task

Check the policy arguments, not only tool names. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 19-16
uv run gym check 19-16
uv run gym hint 19-16
```

## Reading

[Module lesson](../../../../modules/19_testing_and_evaluation/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/test)
