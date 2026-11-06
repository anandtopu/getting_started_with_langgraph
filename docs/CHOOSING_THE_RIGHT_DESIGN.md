# Choose the smallest design that meets the requirement

These are conceptual decision diagrams. Start with an observable requirement: a pause, recovery after failure, dynamic tool selection, or separately testable ownership. A graph is not a requirement by itself.

```mermaid
flowchart TD
    A[New business process] --> B{Small fixed calculation?}
    B -->|Yes| P[Plain Python]
    B -->|No| C{Control flow known beforehand?}
    C -->|Yes| W[Fixed workflow]
    C -->|No| D{Standard model and tool loop sufficient?}
    D -->|Yes| E[create_agent]
    D -->|No| F{Different context or permission boundaries?}
    F -->|No| G[Custom agent graph]
    F -->|Yes| H[Scoped agents under a bounded supervisor]
```

A payout formula belongs in a pure function. Gathering documents, waiting for an estimate, and asking an adjuster are workflow steps. Policy Q&A can use an agent to choose a read-only retrieval tool. An agent that must follow a precise approval protocol may need explicit graph nodes around its tool loop. Multiple agents are useful when specialists need different tools or private context; they add calls, latency, and coordination failures.

```mermaid
flowchart TD
    A[Need durable orchestration] --> B{Is named state and branching the main model?}
    B -->|Yes| G[Graph API]
    B -->|No| C{Does ordinary function control flow read more clearly?}
    C -->|Yes| F[Functional API entrypoint and tasks]
    C -->|No| G
```

Both APIs use durable execution. Graph nodes make state transitions and possible routes visible. Functional tasks preserve results across re-entry while normal Python expresses orchestration. Neither API makes arbitrary external effects automatically safe to repeat. Test the failure boundary, not just the syntax.

```mermaid
flowchart TD
    A[Growing workflow] --> B{Reusable responsibility or private state boundary?}
    B -->|Yes| S[Subgraph with an explicit input-output contract]
    B -->|No| C{Separate team owns and tests this component?}
    C -->|Yes| S
    C -->|No| K[Keep one graph and small node functions]
```

Use a shared-schema subgraph only for genuinely shared fields. Use an adapter when private messages or internal bookkeeping must stay private. Decide whether the child inherits the parent's checkpoint lifecycle or owns independent threads before adding persistence.

For every design, write five answers: who can start it; who can resume it; what is saved; what might repeat; and how you detect a duplicate effect. Compare your answers with the [capstone rubric](../capstones/05_design_your_own/rubric.md) and [official workflows and agents guide](https://docs.langchain.com/oss/python/langgraph/workflows-agents).
