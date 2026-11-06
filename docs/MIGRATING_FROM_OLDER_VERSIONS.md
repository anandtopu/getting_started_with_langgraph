# Migrating from older versions

The course uses the verified versions in [VERIFICATION_NOTES.md](VERIFICATION_NOTES.md). This document is the only place where historical spellings are included for comparison. It also holds the registry used by the repository scanner.

| Historical spelling or pattern | Current course path | Status |
| --- | --- | --- |
| `langgraph.prebuilt.create_react_agent` | `langchain.agents.create_agent` | Deprecated by the LangGraph v1 migration guide |
| `MessageGraph` | `StateGraph` with `MessagesState` or a messages channel | Deprecated |
| raising `NodeInterrupt` | call `interrupt()` and resume with `Command` | Superseded and deprecated; use dynamic interrupts |
| `interrupt_before` / `interrupt_after` for business approval | Dynamic interrupts in a node | These static breakpoint parameters remain debugging tools, not a human-review design |
| `config_schema` for application context | `context_schema` and runtime context | Superseded runtime-context configuration |
| `MemorySaver` | `InMemorySaver` | Older compatibility alias; do not falsely claim every alias itself emits a warning |
| `LLMChain`, `AgentExecutor`, `initialize_agent` | Runnables, current agent construction, or an explicit graph | Legacy LangChain teaching patterns, excluded from the main course |

The [official v1 migration guide](https://docs.langchain.com/oss/python/migrate/langgraph-v1) confirms the graph and agent changes. [Current tools](https://docs.langchain.com/oss/python/langchain/tools) describe trusted runtime context.

## Output access

Use explicit v2 on Python graph invocation and streaming. Read `result.value` and `result.interrupts`; do not read v2 GraphOutput as a dictionary. A stream part has type, namespace, and data fields. Old default-mode streams use different tuple/dictionary shapes. See the [streaming guide](https://docs.langchain.com/oss/python/langgraph/streaming).

## A runnable static debugging comparison

Static breakpoints are useful for inspecting a graph before or after a named node. This example is deliberately confined to the migration document. Save the entire block in an ignored workspace file and run it with Python:

```python
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from typing import TypedDict


class State(TypedDict):
    claim_id: str
    status: str


def validate_claim(state: State) -> dict[str, str]:
    return {"status": "validated"}


def main() -> None:
    builder = StateGraph(State)
    builder.add_node("validate_claim", validate_claim)
    builder.add_edge(START, "validate_claim")
    builder.add_edge("validate_claim", END)
    graph = builder.compile(
        checkpointer=InMemorySaver(),
        interrupt_before=["validate_claim"],
    )
    config = {"configurable": {"thread_id": "debug-example"}}
    graph.invoke({"claim_id": "CLM-0001", "status": "received"}, config, version="v2")
    print(graph.get_state(config).next)
    print(graph.invoke(None, config, version="v2").value)


if __name__ == "__main__":
    main()
```

Expected: the next node is validate_claim, then the resumed value has status validated. A real approval needs a meaningful payload and a validated decision; it belongs in a dynamic interrupt rather than this breakpoint.

## MCP compatibility

The requested standalone adapter currently requires MCP SDK 1.x. The integrated LangChain successor is Beta. Do not combine incompatible SDK major versions merely because both are latest on their own. The exact selected versions and evidence are in the verification notes.

## Scanner registry

The scan reads these values from this document, so its own code does not need to embed prohibited names.

<!-- legacy-scan-registry -->
```json
[
  "create_react_agent",
  "MessageGraph",
  "NodeInterrupt",
  "interrupt_before",
  "interrupt_after",
  "config_schema",
  "MemorySaver",
  "LLMChain",
  "AgentExecutor",
  "initialize_agent"
]
```
