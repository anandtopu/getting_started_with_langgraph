# 00 — Setup and orientation

> After this module you can compare a plain claim checklist with an equivalent graph.

**Time:** 60 minutes · **Level:** Beginner · **LLM needed:** No live model · **Cost:** $0 with the included fakes.

**Larkspur Claims Copilot v00** · Practice takes additional time.

## Prerequisites

Complete [repository quick start](../../README.md). Read dictionary keys, functions, and Python type hints comfortably. Run uv sync from the repository root.

Optional installation requirements are listed in [the setup guide](../../docs/OPTIONAL_DEPENDENCIES.md). Use `uv run --no-sync` after installing extras so subsequent commands retain that environment.

## Learning objectives

- Implement and explain Plain Python versus stateful orchestration; workflow versus agent; LangGraph, LangChain, and LangSmith roles.
- Implement and explain uv and pip environments; portable script entry points; optional providers; safe configuration.
- Implement and explain Gym workflow; pytest assertions; progress and hints; deterministic acceptance criteria.

## The big idea

Compare a plain claim checklist with an equivalent graph. Predict the state before running code, then compare the observed result. A state is the data visible to a node; a node is one unit of work; an edge selects later work. A checkpoint is a saved state boundary, not a promise that an external effect happened exactly once.

## How it works

### Plain Python and a graph

Use plain Python for a small fixed calculation. A workflow follows control flow you choose; an agent can choose tools dynamically within your constraints. LangGraph supplies stateful execution, LangChain supplies model/tool components, and LangSmith supplies optional tracing and deployment. The first example runs the same checklist both ways and asserts identical decisions.

### Environment

An environment is the interpreter and packages used by one command. A package installed for another interpreter is still missing here. An optional live provider must not block a deterministic checklist.

Check the tools in this workshop, not the tools in another building.

### First Gym

An assertion compares an observed result with an explicit requirement. A failing starter is useful when it runs and shows a wrong business result. Hints guide a repair; viewing a solution is recorded separately from independent work.

Use a measuring tape before changing the shape of a part.

## Key APIs at a glance

| API / executable example | What it does | When to use it |
| --- | --- | --- |
| StateGraph — [01_plain_checklist.py](examples/01_plain_checklist.py) | Plain Python versus stateful orchestration; workflow versus agent; LangGraph, LangChain, and LangSmith roles | Compare a plain function and a fixed graph. |
| run(case) — [02_environment.py](examples/02_environment.py) | uv and pip environments; portable script entry points; optional providers; safe configuration | An environment is the interpreter and packages used by one command. |
| run(case) — [03_first_gym.py](examples/03_first_gym.py) | Gym workflow; pytest assertions; progress and hints; deterministic acceptance criteria | An assertion compares an observed result with an explicit requirement. |

## Walkthrough

Run commands from the repository root; the same commands work in PowerShell, macOS, and Linux. Open the source alongside the output. Find the state declaration, node functions, graph connections, and invocation. For a failure, start with the earliest changed field or scheduled node.

```text
uv run python modules/00_setup/examples/01_plain_checklist.py
```

```text
uv run python modules/00_setup/examples/02_environment.py
```

**Predict, then run:** for {"python": [3, 12], "packages": ["langgraph", "pytest"], "data_present": true, "live": false, "provider_ready": false}, write the resulting fields and any expected error. Then test the boundary cases in tests/environment.json.

<details>
<summary>Reveal the checked result</summary>

```json
{
  "value": {
    "ready": true,
    "errors": [],
    "mode": "offline"
  }
}
```

An environment is the interpreter and packages used by one command. A package installed for another interpreter is still missing here. An optional live provider must not block a deterministic checklist.

</details>

```text
uv run python modules/00_setup/examples/03_first_gym.py
```

**Predict, then run:** for {"claim_type": " Water ", "claim_id": "CLM-0001"}, write the resulting fields and any expected error. Then test the boundary cases in tests/first_gym.json.

<details>
<summary>Reveal the checked result</summary>

```json
{
  "value": {
    "claim_id": "CLM-0001",
    "label": "water"
  }
}
```

An assertion compares an observed result with an explicit requirement. A failing starter is useful when it runs and shows a wrong business result. Hints guide a repair; viewing a solution is recorded separately from independent work.

</details>

When build_graph needs no arguments, its generated Mermaid diagram is saved beside the example. A diagram records possible edges; a runtime stream records executed work. A single sequence advances one node per superstep. Parallel nodes see the same previous boundary, so they cannot read a sibling's unfinished update.

## When to use it, and when not to

Use these contracts when the claim needs the state or control-flow behavior described above. Keep pure arithmetic and validation in ordinary functions that can be tested independently. A graph, checkpoint, or extra agent adds operational choices; justify it with a concrete failure, pause, branch, or reuse requirement.

## Real-world use case

Compare a plain claim checklist with an equivalent graph. The executable milestone uses only fictional records and the shared v00 implementation. [Read the use case](use_case/claims_copilot.py).

```text
uv run python modules/00_setup/use_case/claims_copilot.py
```

Sample output from the synthetic default case:

```json
{
  "complete": {
    "claim_id": "CLM-0001",
    "status": "ready",
    "missing": [],
    "trace": [
      "normalize_claim",
      "check_required_fields",
      "route_claim"
    ]
  },
  "missing": {
    "claim_id": "CLM-0007",
    "status": "needs_information",
    "missing": [
      "loss_date"
    ],
    "trace": [
      "normalize_claim",
      "check_required_fields",
      "route_claim"
    ]
  }
}
```

A real team would connect this boundary to validated records and authenticated roles, then retain the same rejection, ownership, and recovery checks.

## Common bugs

| Symptom or broken contract | Cause and repair | Practice |
| --- | --- | --- |
| Observed `{"value": {"ready": false, "errors": ["Missing optional model integration"], "mode": "offline"}}`. Required and optional packages are different contracts. | Restore `errors = []` and check the boundary cases. | [00-07](../../gym/tasks/00/00-07_environment_build/task.md) |
| Observed `{"value": {"ready": false, "errors": ["Optional live provider is not configured"], "mode": "offline"}}`. A missing provider is a problem only when live mode was requested. | Restore `case["live"] and not case["provider_ready"]` and check the boundary cases. | [00-08](../../gym/tasks/00/00-08_environment_fix/task.md) |
| Observed `{"value": {"claim_id": "CLM-0001", "label": "water"}}`. Unknown claim categories need an explicit label. | Restore `else "unknown"` and check the boundary cases. | [00-13](../../gym/tasks/00/00-13_first_gym_build/task.md) |
| Observed `{"value": {"claim_id": "CLM-0001", "label": "unknown"}}`. Labels need case normalization before comparison. | Restore `value.strip().lower()` and check the boundary cases. | [00-14](../../gym/tasks/00/00-14_first_gym_fix/task.md) |

## Practice

- [00-01 — build, easy](../../gym/tasks/00/00-01_plain_checklist_build/task.md): Build a three-step checklist that reads a synthetic claim without needing a model.
- [00-02 — fix, medium](../../gym/tasks/00/00-02_plain_checklist_fix/task.md): Fix a checklist whose missing-data branch silently approves an incomplete claim.
- [00-03 — predict, easy](../../gym/tasks/00/00-03_plain_checklist_predict/task.md): Predict the checklist results for complete, incomplete, and duplicate submissions.
- [00-04 — trace, medium](../../gym/tasks/00/00-04_plain_checklist_trace/task.md): Trace which checklist step dropped the claim identifier.
- [00-05 — extend, hard](../../gym/tasks/00/00-05_plain_checklist_extend/task.md): Extend the checklist to return an explicit reason for every intake decision.
- [00-06 — design, hard](../../gym/tasks/00/00-06_plain_checklist_design/task.md): Choose the smallest sufficient implementation for six Larkspur requests.
- [00-07 — build, easy](../../gym/tasks/00/00-07_environment_build/task.md): Build environment: Required and optional packages are different contracts.
- [00-08 — fix, medium](../../gym/tasks/00/00-08_environment_fix/task.md): Fix environment: A missing provider is a problem only when live mode was requested.
- [00-09 — predict, easy](../../gym/tasks/00/00-09_environment_predict/task.md): Predict environment across the declared cases
- [00-10 — trace, medium](../../gym/tasks/00/00-10_environment_trace/task.md): Trace environment: A missing provider is a problem only when live mode was requested.
- [00-11 — extend, hard](../../gym/tasks/00/00-11_environment_extend/task.md): Extend environment: A setup report must identify missing committed fixtures.
- [00-12 — refactor, hard](../../gym/tasks/00/00-12_environment_refactor/task.md): Refactor environment: Use the supplied interpreter version; do not assume the recommended version is installed.
- [00-13 — build, easy](../../gym/tasks/00/00-13_first_gym_build/task.md): Build first gym: Unknown claim categories need an explicit label.
- [00-14 — fix, medium](../../gym/tasks/00/00-14_first_gym_fix/task.md): Fix first gym: Labels need case normalization before comparison.
- [00-15 — predict, easy](../../gym/tasks/00/00-15_first_gym_predict/task.md): Predict first gym across the declared cases
- [00-16 — trace, medium](../../gym/tasks/00/00-16_first_gym_trace/task.md): Trace first gym: Labels need case normalization before comparison.
- [00-17 — extend, hard](../../gym/tasks/00/00-17_first_gym_extend/task.md): Extend first gym: Leading and trailing spaces are not claim categories.
- [00-18 — design, hard](../../gym/tasks/00/00-18_first_gym_design/task.md): Design first gym and justify the boundary policies

Start with tasks 01, 02, 09, 10, 17, and 18 in this module. Finish the other tasks for full practice. Hints are progressive; solution exposure is recorded. Predict and Trace tasks use answer JSON, not a code starter.

## Quiz

Predict first; explain in your own words.

1. Explain the contract in 02_environment.py using one claim from its input cases.
2. Diagnose this broken behavior: A missing provider is a problem only when live mode was requested. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 03_first_gym.py using one claim from its input cases.
4. Diagnose this broken behavior: Labels need case normalization before comparison. Which observation distinguishes the repair from a default-case-only fix?
5. When is plain Python sufficient for intake?
6. What is the difference between a workflow and an agent?

<details>
<summary>Answers</summary>

1. An environment is the interpreter and packages used by one command. A package installed for another interpreter is still missing here. An optional live provider must not block a deterministic checklist.
2. A missing provider is a problem only when live mode was requested. Compare the normal case with the boundary fixtures and identify the first differing update.
3. An assertion compares an observed result with an explicit requirement. A failing starter is useful when it runs and shows a wrong business result. Hints guide a repair; viewing a solution is recorded separately from independent work.
4. Labels need case normalization before comparison. Compare the normal case with the boundary fixtures and identify the first differing update.
5. Use a plain function for a small fixed calculation without orchestration needs.
6. A workflow follows chosen control flow; an agent selects actions dynamically within explicit limits.

</details>

## Cost and safety

The default commands cost $0: deterministic Python and, in model lessons, scripted local fakes. They consume no hosted tokens and make no real payments or emails. Optional live experiments use the provider configured in .env; a short one-to-four-call exercise is usually cents, but verify your provider's current token prices and set a budget. Ollama can run locally without a hosted bill. Temporary checkpoint files are isolated from the committed dataset. Keep real customer details and credentials out of graph state.

## Key takeaways

- State visibility and update rules determine what a node can safely assume.
- Check normal, missing, boundary, and failure cases before trusting a workflow.
- Separate observed execution from diagrams, predictions, and durable history.
- Model output is evidence to validate, never an authorization grant.
- A saved checkpoint and an external effect have separate durability boundaries.

## Go deeper

- [plain checklist official guide](https://docs.langchain.com/oss/python/langgraph/overview)
- [environment official guide](https://docs.langchain.com/oss/python/langgraph/overview)
- [first gym official guide](https://docs.langchain.com/oss/python/langgraph/test)

## Next:

Continue to [module 01: Your first graph](../../modules/01_your_first_graph/README.md).
