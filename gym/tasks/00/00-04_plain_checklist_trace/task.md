# 00-04: Find the lost claim identifier

## Scenario

Larkspur receives a complete claim, a claim missing its loss date, and a duplicate.
The required fields, in order, are claim_id, claim_type, description, amount_cents, and loss_date.
Normalize leading/trailing whitespace in text. Missing means absent, None, or empty after normalization.
Zero cents is present. A duplicate marker takes precedence over the missing-information route.
Do not mutate the input. A checklist is a fixed workflow; it needs no language model or autonomous agent.

## Requirements

Inspect this observed trace:

```text
input: claim_id=CLM-0007, claim_type= Water , description= Burst pipe. , amount_cents=125000, loss_date=None
normalize_claim: description=Burst pipe., loss_date=None
check_required_fields: description=Burst pipe., loss_date=None, missing=[claim_id, claim_type, amount_cents, loss_date]
```

Return JSON keys first_bad_step, lost_field, and fix. For fix, use one of preserve_claim_id,
increase_budget, or request_new_claim. Find the first step that loses identity, not the step
that later notices it.

## Acceptance criteria

The first bad transition must match the supplied trace. Identify claim_id as the field and
select a repair that prevents information loss. The trace is reproduced by real Python steps.

## Practice

Tracing state changes, identity preservation, and diagnosis before adding orchestration.
