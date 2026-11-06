# Hints

## Hint 1

A spending envelope limits the planned work, while an authorized signature is still required for the actual payment. Compare the first differing field with the task's required behavior.

## Hint 2

Enforce the separate planned-call budget. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: case["planned_calls"] > case["call_budget"]. Check every boundary input after the repair; a default-case pass alone is insufficient.
