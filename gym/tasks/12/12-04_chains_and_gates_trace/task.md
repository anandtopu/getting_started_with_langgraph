# 12-04 — Diagnose chains and gates from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Prompt chaining fixes the order of model operations. A deterministic gate compares extracted facts with the authoritative policy before allowing a draft. The validated category can route work, but a model cannot override the gate. A blocked extraction should not consume a drafting call.

## Your task

Diagnose chains and gates from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "category": "policy",
    "policy_deductible": 100000,
    "extracted_deductible": 100000
  },
  {
    "category": "documents",
    "policy_deductible": 100000,
    "extracted_deductible": 100000
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Reject contradictory extracted facts before drafting."
- "Stop the chain when the fact gate fails."
- "Validate the routing category against an explicit allowlist."
- "Keep the drafted deductible tied to the authoritative policy."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 12-04
uv run gym check 12-04
uv run gym hint 12-04
```

## Reading

[Module lesson](../../../../modules/12_workflow_patterns/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
