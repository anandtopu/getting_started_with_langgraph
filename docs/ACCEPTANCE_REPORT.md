# Phase 2 acceptance report

This is the foundation checkpoint, not the completed course release. The complete plan has 486 exercises. Six introductory exercises are implemented so the gym can be tested end to end; 480 remain for the module phases.

## Delivered foundation

- Locked Python environment and optional dependency groups.
- Shared settings, deterministic chat fakes, model factory, state printing, data access, and bounded offline execution.
- All nine gym commands, isolated grading, protected learner files, three hints, answer grading, Design self-review, progress recovery, concurrent updates, and seeded drills.
- Reproducible synthetic data: 500 claims, 60 submissions, 30 TXT/PDF document pairs, 20 emails, policy products, fraud rules, and golden evaluations.
- Validation scripts, contribution documents, MIT license, issue/PR templates, and CI configuration.

## Evidence and limits

The local environment is Windows with Python 3.12.13. Foundation tests and the six task starters/solutions have been exercised. The final command results are recorded below when validation completes. No live model inference, hosted deployment, payment, or email is performed.

The CI workflow covers Ubuntu and Windows on Python 3.11–3.14, macOS on 3.12, an optional-dependency job, and a separate public-link job. These are configured checks; remote CI has not run yet. The repository is not yet published.

The full-course release gates intentionally remain incomplete: modules, remaining gym tasks, notebooks, capstones, bonuses, and finishing guides arrive in later phases. Use the normal validation commands for this checkpoint; the validators' --release options enforce the future complete-course requirements.

## Next boundary

Phase 3 implements modules 00–07 and completes their 144 tasks. Continue only after the foundation checkpoint is accepted.
