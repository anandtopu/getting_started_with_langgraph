# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_create_agent.py using one claim from its input cases.
2. Diagnose this broken behavior: Reject unknown policy IDs, not the known fixture. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_middleware.py using one claim from its input cases.
4. Diagnose this broken behavior: Enforce the independent tool budget. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_agent_composition.py using one claim from its input cases.
6. Diagnose this broken behavior: Do not turn an explanation into payment approval. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. create_agent builds a standard model/tool loop on LangGraph. Start there for ordinary tool use; use a custom StateGraph when the business process requires explicit gates or branches. The compiled agent still accepts state, can be inspected as a graph, and emits normal messages.
2. Reject unknown policy IDs, not the known fixture. Compare the normal case with the boundary fixtures and identify the first differing update.
3. Middleware hooks surround agent operations. before_model can update declared middleware state; wrap_model_call controls the handler; after_model observes the result. Model and tool budgets are separate: limiting one does not automatically limit the other. Hook order belongs in an explicit test.
4. Enforce the independent tool budget. Compare the normal case with the boundary fixtures and identify the first differing update.
5. An adapter node converts a business question into private agent messages and returns only the public explanation. The parent retains claim identity and its own process status. Sharing every internal message is convenient but widens the context and privacy boundary unnecessarily.
6. Do not turn an explanation into payment approval. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
