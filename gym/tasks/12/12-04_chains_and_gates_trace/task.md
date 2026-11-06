# 12-04 — Trace chains and gates: Stop the chain when the fact gate fails.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Prompt chaining fixes the order of model operations. A deterministic gate compares extracted facts with the authoritative policy before allowing a draft. The validated category can route work, but a model cannot override the gate. A blocked extraction should not consume a drafting call.

## Your task

Stop the chain when the fact gate fails. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 12-04
uv run gym check 12-04
uv run gym hint 12-04
```

## Reading

[Module lesson](../../../../modules/12_workflow_patterns/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
