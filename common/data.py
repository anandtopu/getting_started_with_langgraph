"""Repository-relative, read-only access to the committed synthetic dataset."""

import json
import re
import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def data_path(relative: str, base: Path = DATA) -> Path:
    """Reject traversal and symlinks escaping the selected dataset."""
    path = (base / relative).resolve()
    if not path.is_relative_to(base.resolve()):
        raise ValueError("A dataset path must stay inside data/.")
    if not path.is_file():
        raise FileNotFoundError(f"Missing synthetic fixture: {relative}. Run scripts/check_env.py.")
    return path


def load_submission(number: int, base: Path = DATA) -> dict[str, Any]:
    if not 1 <= number <= 60:
        raise ValueError("Submission numbers are 1 through 60.")
    return json.loads(
        data_path(f"claim_submissions/claim_{number:03d}.json", base).read_text("utf-8")
    )


def load_jsonl(relative: str, base: Path = DATA) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in data_path(relative, base).read_text("utf-8").splitlines()
        if line.strip()
    ]


def load_fraud_rules(base: Path = DATA) -> dict[str, Any]:
    return yaml.safe_load(data_path("fraud_rules.yaml", base).read_text("utf-8"))


@contextmanager
def claims_connection(path: Path = DATA / "claims.db") -> Iterator[sqlite3.Connection]:
    """Open in read-only mode and close explicitly, including on Windows."""
    connection = sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
    finally:
        connection.close()


def lookup_claim(claim_id: str, path: Path = DATA / "claims.db") -> dict[str, Any] | None:
    if not re.fullmatch(r"CLM-\d{4}", claim_id):
        raise ValueError("Expected a synthetic claim ID such as CLM-0001.")
    with claims_connection(path) as connection:
        row = connection.execute("SELECT * FROM claims WHERE claim_id = ?", (claim_id,)).fetchone()
    return dict(row) if row else None
