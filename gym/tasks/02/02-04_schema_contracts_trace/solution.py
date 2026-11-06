"""Diagnose schema contracts from execution evidence. Run this file with Python. No live model or network."""

from dataclasses import asdict, dataclass
from typing import TypedDict

from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel, Field

from common.pretty import print_state

DEFAULT_CASE = {"kind": "pydantic", "amount_cents": 125000, "claim_id": "CLM-0001"}


class ClaimDict(TypedDict):
    claim_id: str
    amount_cents: int
    status: str


@dataclass
class ClaimData:
    claim_id: str = "unknown"
    amount_cents: int = 0
    status: str = "received"


class ClaimModel(BaseModel):
    claim_id: str = "unknown"
    amount_cents: int = Field(gt=0, strict=True)
    status: str = "received"


def as_mapping(state) -> dict:
    if isinstance(state, BaseModel):
        return dict()
    return asdict(state) if isinstance(state, ClaimData) else dict(state)


def validate_claim(state) -> dict:
    values = as_mapping(state)
    amount = values.get("amount_cents", 0)
    if type(amount) is not int or amount <= 0:
        raise ValueError("amount_cents must be a positive integer")
    return {"status": "validated"}


def build_graph(kind: str = "pydantic"):
    schema = {"typed": ClaimDict, "dataclass": ClaimData, "pydantic": ClaimModel}[kind]
    builder = StateGraph(schema)
    builder.add_node("validate_claim", validate_claim)
    builder.add_edge(START, "validate_claim")
    builder.add_edge("validate_claim", END)
    return builder.compile()


def scenario(case: dict | None = None) -> dict:
    values = dict(DEFAULT_CASE if case is None else case)
    kind = values.pop("kind", "pydantic")
    result = build_graph(kind).invoke(values, version="v2").value
    return {"output_type": type(result).__name__, "value": as_mapping(result)}


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"amount_cents": 125000, "claim_id": "CLM-0001", "kind": "pydantic"},
        {"amount_cents": 125000, "claim_id": "CLM-0001", "kind": "typed"},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "Use Pydantic field access or model_dump instead of losing validated values.",
    }


if __name__ == "__main__":
    main()
