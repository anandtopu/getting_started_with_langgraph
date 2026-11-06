# Hints for 00-02

## Hint 1

Run the missing-date case and inspect the condition that assigns its status.

## Hint 2

An empty missing list means complete, not incomplete. Duplicates still take precedence.

## Hint 3

Use duplicate if duplicate_of is present; otherwise needs_information if missing is nonempty; otherwise ready.
