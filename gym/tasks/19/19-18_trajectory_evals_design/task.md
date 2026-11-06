# 19-18 — Design trajectory evals and justify the boundary policies

Type: design. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

A trajectory is the sequence of tool requests, separate from the final answer. agentevals can compare strict order, unordered calls, subsets, or supersets. Exact argument matching catches the right tool used on the wrong policy. Choose the matching rule from the business requirement; parallel independent calls may legitimately change order.

## Your task

Design trajectory evals and justify the boundary policies Implement the choices in run and complete design.md using the rubric.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 19-18
uv run gym check 19-18
uv run gym hint 19-18
```

## Reading

[Module lesson](../../../../modules/19_testing_and_evaluation/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/test)
