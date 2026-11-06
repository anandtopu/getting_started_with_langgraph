"""Read-only synthetic claims MCP service. Run with python -m common.mcp_server."""

from common.data import lookup_claim


def create_server():
    from mcp.server.fastmcp import FastMCP

    server = FastMCP("Larkspur synthetic claims")

    @server.tool()
    def read_claim(claim_id: str) -> dict:
        """Read a synthetic claim's public triage fields; no write or payment capability."""
        claim = lookup_claim(claim_id)
        if claim is None:
            raise ValueError("Unknown synthetic claim")
        return {key: claim[key] for key in ("claim_id", "claim_type", "amount_cents", "route")}

    @server.tool()
    def list_capabilities() -> list[str]:
        """Describe this deliberately read-only demonstration service."""
        return ["read_claim", "list_capabilities"]

    return server


def main() -> None:
    # stdio carries protocol messages only. Framework diagnostics use stderr.
    create_server().run(transport="stdio")


if __name__ == "__main__":
    main()
