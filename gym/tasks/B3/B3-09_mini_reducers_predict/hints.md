# Hints

## Hint 1

Two people cannot independently replace the same page without an agreed rule for combining their edits. Compare the first differing field with the task's required behavior.

## Hint 2

Install the mini-runner reducer when parallel accumulation is required. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: {"findings": operator.add} if case["use_reducer"] else {}. Check every boundary input after the repair; a default-case pass alone is insufficient.
