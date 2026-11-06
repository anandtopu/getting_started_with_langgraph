# Hints

## Hint 1

Merge independent evidence envelopes without treating the last envelope as the whole case. Compare the first differing field with the task's required behavior.

## Hint 2

A merge must preserve evidence from earlier updates. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: indexed = {item["id"]: dict(item) for item in left}. Check every boundary input after the repair; a default-case pass alone is insufficient.
