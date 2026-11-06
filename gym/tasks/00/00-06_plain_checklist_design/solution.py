"""One defensible design assignment; the explanation is part of the answer."""

from common.pretty import print_state


def run() -> dict[str, str]:
    return {
        "deductible_math": "python",
        "document_checklist": "workflow",
        "classify_description": "workflow",
        "open_policy_research": "agent",
        "approval_wait": "workflow",
        "quote_math": "python",
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
