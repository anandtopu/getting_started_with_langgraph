# 00-01: Build the intake checklist

## Scenario

Larkspur receives a complete claim, a claim missing its loss date, and a duplicate.
The required fields, in order, are claim_id, claim_type, description, amount_cents, and loss_date.
Normalize leading/trailing whitespace in text. Missing means absent, None, or empty after normalization.
Zero cents is present. A duplicate marker takes precedence over the missing-information route.
Do not mutate the input. A checklist is a fixed workflow; it needs no language model or autonomous agent.

## Requirements

Implement `run(claim)` in your Python attempt. Return claim_id, status, missing, and trace.
The trace is exactly normalize_claim, check_required_fields, route_claim. Status is ready,
needs_information, or duplicate. A missing-field list uses the required-field order.
The starter is executable but intentionally routes a claim incorrectly.

## Acceptance criteria

All complete/missing/duplicate cases pass, zero cents is not missing, whitespace is normalized,
and the input is unchanged. Checks import your selected workspace file.

## Practice

Plain Python steps, state preservation, explicit branching, and when a fixed checklist is sufficient.
Run `uv run gym check 00-01`. Read an assertion as an expected behavior that your result must satisfy.
