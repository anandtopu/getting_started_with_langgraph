# 10-16 — Diagnose agent composition from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An adapter node converts a business question into private agent messages and returns only the public explanation. The parent retains claim identity and its own process status. Sharing every internal message is convenient but widens the context and privacy boundary unnecessarily.

## Your task

Diagnose agent composition from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "question": "What evidence is missing?"
  },
  {
    "claim_id": "CLM-0099",
    "question": "Which estimate is needed?"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Map the specialist answer into the parent explanation field."
- "Do not turn an explanation into payment approval."
- "Select the specialist answer rather than its input question."
- "Preserve the parent finalization step when refactoring the adapter."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 10-16
uv run gym check 10-16
uv run gym hint 10-16
```

## Reading

[Module lesson](../../../../modules/10_prebuilt_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/agents)
