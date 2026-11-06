# Hints

## Hint 1

Watch the service desks work while retaining a final receipt, and close every open folder when stopping early. Compare the first differing field with the task's required behavior.

## Hint 2

Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: the original behavioral contract. Check every boundary input after the repair; a default-case pass alone is insufficient.
