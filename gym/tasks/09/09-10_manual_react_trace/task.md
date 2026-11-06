# 09-10 — Diagnose manual react from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A manual agent loop alternates a model node and ToolNode. tools_condition checks the newest AI message: tool calls continue the loop, a final answer ends it. A recursion budget catches nontermination, but does not authorize tool effects or guarantee a useful answer.

## Your task

Diagnose manual react from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "policy_id": "POL-0001",
    "recursion_limit": 12
  },
  {
    "policy_id": "MISSING",
    "recursion_limit": 12
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Return tool evidence to the model before ending."
- "Let the agent observe a policy lookup failure."
- "Respect the caller's execution budget."
- "Preserve the requested policy when constructing tool arguments."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 09-10
uv run gym check 09-10
uv run gym hint 09-10
```

## Reading

[Module lesson](../../../../modules/09_tools_and_agent_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
