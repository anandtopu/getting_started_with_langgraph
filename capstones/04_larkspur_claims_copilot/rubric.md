# Self-review rubric

Score each criterion 0 (missing), 1 (happy path only), or 2 (demonstrated including failure). Passing means at least 8/10, with 2 on authorization and recovery.

- Correctness: all independent acceptance cases pass, with one learner-added boundary case.
- Authorization: trusted identity is separate from user/model text; rejection cannot produce an effect.
- Recovery: show the saved state or replay boundary and explain effect deduplication.
- Design: justify workflow versus agent and identify the smallest useful component boundaries.
- Operations: document dependencies, execution commands, costs, failure diagnostics, and a safe shutdown.

Record evidence and one remaining limitation for every score. Do not award design points solely because tests pass.
