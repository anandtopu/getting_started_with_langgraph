# 19-04 — Diagnose test graph behavior from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A pytest test is a function whose assertions express requirements. Parametrized tests run it over many inputs. Compare pure node rules and whole graphs against independently specified boundary outcomes; comparing two copies of the same implementation can preserve the same bug. Fake models make orchestration tests repeatable, not model accuracy measurable.

## Your task

Diagnose test graph behavior from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "amounts": [
      100000,
      100001,
      500001,
      true
    ]
  },
  {
    "amounts": [
      0,
      -1,
      500000
    ]
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Specify the inclusive fast-track boundary in the test oracle."
- "Include boolean cents in invalid-input coverage."
- "Keep exactly 500000 cents in the standard route."
- "Require both implementations to match the independent expected route."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 19-04
uv run gym check 19-04
uv run gym hint 19-04
```

## Reading

[Module lesson](../../../../modules/19_testing_and_evaluation/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/test)
