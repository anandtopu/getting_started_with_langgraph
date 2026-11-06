# Hints

## Hint 1

Merge independent evidence envelopes without treating the last envelope as the whole case. Compare the first differing field with the task's required behavior.

## Hint 2

Return new evidence only; the reducer already has previous values. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: "log": ["receipt"]. Check every boundary input after the repair; a default-case pass alone is insufficient.
