# 12-10 — Trace orchestrator workers: Reject a plan that delegates the same section twice.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An orchestrator proposes a structured plan, then Send creates one worker invocation per section. Validate allowed section names, uniqueness, and size before fan-out. The reducer accumulates independent reports and a deferred assembler produces a canonical order rather than relying on worker completion timing.

## Your task

Reject a plan that delegates the same section twice. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 12-10
uv run gym check 12-10
uv run gym hint 12-10
```

## Reading

[Module lesson](../../../../modules/12_workflow_patterns/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
