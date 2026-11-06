# Hints

## Hint 1

Merge independent evidence envelopes without treating the last envelope as the whole case. Compare the first differing field with the task's required behavior.

## Hint 2

Severity must not decrease when a later finding is weaker. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: max(indexed.get(key, {}).get("severity", 0), finding["severity"]). Check every boundary input after the repair; a default-case pass alone is insufficient.
