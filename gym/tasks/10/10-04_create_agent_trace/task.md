# 10-04 — Trace create agent: Reject unknown policy IDs, not the known fixture.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

create_agent builds a standard model/tool loop on LangGraph. Start there for ordinary tool use; use a custom StateGraph when the business process requires explicit gates or branches. The compiled agent still accepts state, can be inspected as a graph, and emits normal messages.

## Your task

Reject unknown policy IDs, not the known fixture. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "policy_id": "POL-0001"
  },
  {
    "policy_id": "MISSING"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 10-04
uv run gym check 10-04
uv run gym hint 10-04
```

## Reading

[Module lesson](../../../../modules/10_prebuilt_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/agents)
