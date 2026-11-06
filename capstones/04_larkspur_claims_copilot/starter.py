"""Run the flagship through its actual authenticated streaming API.

Run: uv run --extra apps python capstones/04_larkspur_claims_copilot/solution.py
Expected: one synthetic effect, customer approval forbidden, stale approval rejected.
LLM: local scripted fakes. Deploy the same v11 graph with compose.yaml.
"""

from common.app_demo import run_demo
from common.pretty import print_state


# YOUR CODE HERE: repair the acceptance contract below.
def run(case=None):
    case = {"approved": True, **(case or {})}
    return run_demo(approve=True, stale=True)


def main():
    print_state(run())


if __name__ == "__main__":
    main()
