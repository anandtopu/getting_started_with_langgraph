"""Local deterministic evaluation with a process exit suitable for CI."""

from common.claims import route_claim
from common.data import load_jsonl


def evaluate_routes(rows: list[dict]) -> dict:
    failures = []
    for index, row in enumerate(rows):
        actual = route_claim(row["input"])
        if actual != row["expected_route"]:
            failures.append({"case": index, "expected": row["expected_route"], "actual": actual})
    return {
        "cases": len(rows),
        "correct": len(rows) - len(failures),
        "accuracy": (len(rows) - len(failures)) / len(rows) if rows else 0.0,
        "failures": failures,
    }


def evaluate_file(path: str) -> dict:
    return evaluate_routes(load_jsonl(path))
