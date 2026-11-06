"""Run the committed synthetic routing evaluation and fail below the acceptance threshold."""

import argparse

from common.evaluation import evaluate_file
from common.pretty import print_state


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", default="eval/routing.jsonl")
    parser.add_argument("--minimum", type=float, default=1.0)
    args = parser.parse_args()
    if not 0 <= args.minimum <= 1:
        parser.error("minimum must be between zero and one")
    result = evaluate_file(args.dataset)
    print_state(result)
    return int(result["accuracy"] < args.minimum or not result["cases"])


if __name__ == "__main__":
    raise SystemExit(main())
