# Synthetic Larkspur data

All records are fictional. Never use the policy rules for real insurance decisions.

500 claims, 100 customers and policies, five adjusters, 30 document pairs, 60 submissions, 20 emails, and golden evaluation cases. All payment rows are proposed synthetic entries. Dates and IDs are fixed; missing data, explicit duplicates, and review indicators are intentional.

Regenerate with: uv run python scripts/build_data.py. Use a copy for writable exercises. The manifest records hashes so tests can detect accidental fixture edits.
