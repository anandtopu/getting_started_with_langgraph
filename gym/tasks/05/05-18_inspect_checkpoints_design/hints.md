# Hints

## Hint 1

Correct an audit ledger by adding a new entry with a parent reference instead of erasing an old entry. Compare the first differing field with the task's required behavior.

## Hint 2

The corrected checkpoint must contain the replacement evidence. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: case["corrected_amount"]. Check every boundary input after the repair; a default-case pass alone is insufficient.
