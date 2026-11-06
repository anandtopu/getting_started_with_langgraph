"""A local synthetic effect ledger with transactional, payload-bound idempotency."""

import json
import sqlite3
from pathlib import Path


class EffectLedger:
    def __init__(self, path: Path):
        self.path = path
        connection = self.connect()
        try:
            connection.execute(
                "CREATE TABLE IF NOT EXISTS effects (effect_key TEXT PRIMARY KEY, payload TEXT NOT NULL)"
            )
            connection.commit()
        finally:
            connection.close()

    def connect(self):
        return sqlite3.connect(self.path, timeout=10)

    def record(self, key: str, payload: dict) -> bool:
        if not key or not isinstance(key, str):
            raise ValueError("A stable effect key is required")
        encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        connection = self.connect()
        try:
            connection.execute("BEGIN IMMEDIATE")
            existing = connection.execute(
                "SELECT payload FROM effects WHERE effect_key = ?", (key,)
            ).fetchone()
            if existing is not None:
                if existing[0] != encoded:
                    raise ValueError("Idempotency key reused with a different payload")
                return False
            connection.execute("INSERT INTO effects VALUES (?, ?)", (key, encoded))
            connection.commit()
            return True
        finally:
            connection.close()

    def rows(self) -> list[dict]:
        connection = self.connect()
        try:
            return [
                {"key": row[0], "payload": json.loads(row[1])}
                for row in connection.execute(
                    "SELECT effect_key, payload FROM effects ORDER BY effect_key"
                )
            ]
        finally:
            connection.close()
