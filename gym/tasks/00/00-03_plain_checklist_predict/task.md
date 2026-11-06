# 00-03: Predict three intake decisions

## Scenario

Larkspur receives a complete claim, a claim missing its loss date, and a duplicate.
The required fields, in order, are claim_id, claim_type, description, amount_cents, and loss_date.
Normalize leading/trailing whitespace in text. Missing means absent, None, or empty after normalization.
Zero cents is present. A duplicate marker takes precedence over the missing-information route.
Do not mutate the input. A checklist is a fixed workflow; it needs no language model or autonomous agent.

## Requirements

Edit the JSON answer, not Python. Before running anything, predict the three statuses, the three missing-field lists, and the shared trace for `common.gym_fixtures.checklist_cases()`.

## Acceptance criteria

The keys are statuses (three strings), missing (three arrays), and trace (the three node names). JSON key order does not matter; claim order does. The grader compares your answer with an actual deterministic checklist run.

## Practice

Prediction before execution, branching, and fixed-workflow control flow. Run `uv run gym check 00-03` after recording your prediction.
