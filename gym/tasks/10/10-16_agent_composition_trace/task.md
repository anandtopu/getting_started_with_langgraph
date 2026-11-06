# 10-16 — Trace agent composition: Do not turn an explanation into payment approval.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An adapter node converts a business question into private agent messages and returns only the public explanation. The parent retains claim identity and its own process status. Sharing every internal message is convenient but widens the context and privacy boundary unnecessarily.

## Your task

Do not turn an explanation into payment approval. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 10-16
uv run gym check 10-16
uv run gym hint 10-16
```

## Reading

[Module lesson](../../../../modules/10_prebuilt_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/agents)
