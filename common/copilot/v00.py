"""Version 00: a deterministic plain-Python intake checklist."""

from common.claims import checklist
from common.data import load_submission


def run(claim: dict | None = None) -> dict:
    return checklist(load_submission(1) if claim is None else claim)
