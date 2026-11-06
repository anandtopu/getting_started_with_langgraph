# 12-16 — Diagnose evaluator optimizer from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

The evaluator names concrete factual and tone defects; the optimizer receives that feedback before another draft. Stop on success or a strict attempt budget. A deterministic substring check is deliberately limited: it teaches loop control and must not be mistaken for a production factuality evaluator.

## Your task

Diagnose evaluator optimizer from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "drafts": [
      "Your deductible is 90000 cents.",
      "Thank you. Your deductible is 100000 cents."
    ],
    "budget": 3
  },
  {
    "drafts": [
      "Your deductible is 90000 cents.",
      "Thank you. Your deductible is 100000 cents."
    ],
    "budget": 1
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Stop unsuccessful revision at the configured budget."
- "Require the authoritative deductible fact."
- "Keep the respectful-tone criterion separate from the factual criterion."
- "Stop immediately once both criteria pass."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 12-16
uv run gym check 12-16
uv run gym hint 12-16
```

## Reading

[Module lesson](../../../../modules/12_workflow_patterns/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
