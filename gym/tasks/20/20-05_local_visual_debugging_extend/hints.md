# Hints

## Hint 1

A process map and a dated case file can diagnose a wrong desk assignment even without a visual control room. Compare the first differing field with the task's required behavior.

## Hint 2

Report a discrepancy only when observed and reported routes differ. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: result.value["route"] != case["reported_route"]. Check every boundary input after the repair; a default-case pass alone is insufficient.
