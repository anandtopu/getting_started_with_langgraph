# Hints

## Hint 1

The thread ID is the claim-folder number; reuse another customer's number and you open the wrong folder. Compare the first differing field with the task's required behavior.

## Hint 2

Claim identity must participate in the thread mapping. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: "claim:" + claim_id. Check every boundary input after the repair; a default-case pass alone is insufficient.
