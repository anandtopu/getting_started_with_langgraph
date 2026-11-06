# Phase 2 acceptance report

This is the foundation checkpoint, not the completed course release. The complete plan has 486 exercises. Six introductory exercises are implemented so the gym can be tested end to end; 480 remain for the module phases.

## Delivered foundation

- Locked Python environment and optional dependency groups.
- Shared settings, deterministic chat fakes, model factory, state printing, data access, and bounded offline execution.
- All nine gym commands, isolated grading, protected learner files, three hints, answer grading, Design self-review, progress recovery, concurrent updates, and seeded drills.
- Reproducible synthetic data: 500 claims, 60 submissions, 30 TXT/PDF document pairs, 20 emails, policy products, fraud rules, and golden evaluations.
- Validation scripts, contribution documents, MIT license, issue/PR templates, and CI configuration.

## Evidence and limits

Measured November 5, 2026 (America/Chicago), on Windows with Python 3.12.13 and uv 0.12.18. No live model inference, hosted deployment, payment, or email was performed.

| Check | Observed result |
| --- | --- |
| Base install: uv sync --locked | Passed; default environment restored after optional checks |
| Final base suite: uv run pytest | **64 passed**, 27.08 seconds, no warnings |
| Ruff lint and format checks | Passed; 99 Python files formatted |
| Gym validator | All six released exercises passed; code starters fail for their intended behavior, solutions pass, answer oracles agree, and three hints exist |
| Offline examples | Both shipped examples passed with network access blocked |
| Installed API probes | Passed for explicit v2 output/streaming, node parameters, and structured fake output |
| Catalog coverage and legacy scan | Passed for the phase's declared scope |
| Internal and public links | Final check: 249 links, zero problems |
| Contribution hooks | Lint, format, legacy scan, and local links passed in the inspection clone; notebook stripping had no files yet |
| All Python extras and maintenance tools | Installed successfully; dependency consistency passed for 224 installed packages |
| All-extras suite | 60 tests passed before the final progress/DNS additions; final base suite contains 64 tests |
| Optional providers | All four adapters initialized with synthetic keys and connections blocked; no inference |
| Synthetic data | Hashes, foreign keys, read-only access, repeated generation, integer money boundaries, and logical SQLite rows passed |
| PDF inspection | Representative estimate, receipt, and police summary rendered and visually checked |
| Fresh clone | Cached offline installation, environment check, first graph, intended starter failure, and repaired first task passed in **14.57 seconds** |
| Fresh-clone data suite | All 14 data tests passed, including regeneration and committed hashes |
| Complete-course release validator | Correctly failed: 480 tasks remain, plus incomplete later-module distributions |

The quick-start measurement is an automated guided repair with a warm dependency cache, from local code commit 43e8298. It does not measure download speed or a novice's learning time. Reproduce it with uv run python scripts/check_quickstart.py --offline-install after committing changes. The script keeps an ignored inspection clone and its timing report under tmp/.

The generated text files use explicit LF endings, and Git preserves those endings. This prevents fixture hashes from changing between Windows and Unix checkouts. Database byte integrity is checked against the committed manifest; regeneration across SQLite builds additionally compares logical rows.

The CI workflow covers Ubuntu and Windows on Python 3.11–3.14, macOS on 3.12, an optional-dependency job, and a separate public-link job. These are configured checks; remote CI has not run yet. The repository is not yet published.

The full-course release gates intentionally remain incomplete: modules, remaining gym tasks, notebooks, capstones, bonuses, and finishing guides arrive in later phases. Use the normal validation commands for this checkpoint; the validators' --release options enforce the future complete-course requirements.

## Full-course definition of done

- [x] Default dependency environment installs; the available offline tests pass without keys.
- [x] Ruff lint/format, foundation examples, installed API probes, and legacy-pattern checks pass.
- [x] The nine gym commands have functional tests, including failed learners, stale results, assisted study, reset backups, drills, concurrency, corruption, and timeouts.
- [x] Synthetic data and shared fake models are implemented and checked.
- [ ] Remote CI has not run. The OS/Python matrix is configured, not yet observed.
- [ ] Complete-course task count and per-module distribution await 480 additional exercises.
- [ ] Tier 1 modules, remaining tiers, notebooks, quizzes, and capstones are not yet implemented.
- [ ] Future paths listed in the feature map remain planned until their modules are released.
- [ ] The under-ten-minute novice quick-start requirement still needs an actual learner trial.
- [ ] Optional live inference, Ollama service/model access, Docker/Postgres, deployment, TypeScript, and public publication remain later checks.

The executable files delivered in this phase are complete and checked. Deliberately incorrect starters are exercises; planned future files are not represented by placeholder implementations.

## Next boundary

Phase 3 implements modules 00–07 and completes their 144 tasks. Continue only after the foundation checkpoint is accepted.
