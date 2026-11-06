# Hints

## Hint 1

Inspect the waiting shelf before and after an approval rather than checking only the final receipt. Compare the first differing field with the task's required behavior.

## Hint 2

Capture the pre-resume pending state before it changes. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: "pending_before": list(before.next). Check every boundary input after the repair; a default-case pass alone is insufficient.
