# 12-10 — Diagnose orchestrator workers from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An orchestrator proposes a structured plan, then Send creates one worker invocation per section. Validate allowed section names, uniqueness, and size before fan-out. The reducer accumulates independent reports and a deferred assembler produces a canonical order rather than relying on worker completion timing.

## Your task

Diagnose orchestrator workers from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "sections": [
      "coverage",
      "deductible",
      "exclusions"
    ]
  },
  {
    "sections": []
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Accumulate every worker result instead of overwriting sibling reports."
- "Reject a plan that delegates the same section twice."
- "Assemble reports by stable section identity."
- "Run every approved worker in the plan."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 12-10
uv run gym check 12-10
uv run gym hint 12-10
```

## Reading

[Module lesson](../../../../modules/12_workflow_patterns/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
