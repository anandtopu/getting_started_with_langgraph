# 00-06: Choose a sufficient design

## Scenario

Larkspur is deciding how much orchestration each new request needs. Choose a small design and explain the decision.

## Requirements

Implement `run()` returning six scenario IDs mapped to a choice: python, workflow, or agent.
The scenarios are deductible_math, document_checklist, classify_description, open_policy_research,
approval_wait, and quote_math. Write your reasoning in the companion design file.

A workflow follows a defined sequence. An agent chooses tools/steps in response to a goal.
Plain Python is enough for a direct calculation. LangGraph supplies stateful orchestration;
LangChain's create_agent supplies an agent built on that runtime; LangSmith is optional diagnostics
and deployment, not the computation engine.

## Acceptance criteria

Mechanical checks require six known scenario IDs and allowed choices. The rubric scores whether
your decisions are justified, appropriately small, auditable, and clear. More than one design may
be defensible. After completing the rubric, declare it with `gym check 00-06 --self-reviewed`.

## Practice

Choosing complexity deliberately; distinguishing workflow, agent, runtime, and observability.
