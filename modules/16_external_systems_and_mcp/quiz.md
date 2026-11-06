# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_api_boundaries.py using one claim from its input cases.
2. Diagnose this broken behavior: Honor the bounded retry allowance after a lost acknowledgment. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_mcp_server.py using one claim from its input cases.
4. Diagnose this broken behavior: Pass the requested synthetic claim through schema validation. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_mcp_adapter.py using one claim from its input cases.
6. Diagnose this broken behavior: Send the selected claim identifier to the MCP service. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. async def creates a coroutine; await lets other work proceed while a request waits. An injected HTTP transport makes failures testable without a server. Retry only transient transport failures, bound attempts and timeouts, and reuse a stable idempotency key because a missing acknowledgment may follow a successful write.
2. Honor the bounded retry allowance after a lost acknowledgment. Compare the normal case with the boundary fixtures and identify the first differing update.
3. MCP describes tools with names and JSON schemas. The official SDK validates requests before calling the function. This local service exposes only synthetic triage reads and capability discovery; it has no payment or arbitrary filesystem operation. stdio is the protocol channel, so diagnostics belong on stderr.
4. Pass the requested synthetic claim through schema validation. Compare the normal case with the boundary fixtures and identify the first differing update.
5. MultiServerMCPClient loads tool definitions from a real local stdio subprocess. The adapter turns them into LangChain tools while an explicit client session owns their lifetime. The pinned adapter supports MCP SDK 1.x. The newer langchain.mcp successor is Beta and is documented separately instead of silently mixing incompatible APIs.
6. Send the selected claim identifier to the MCP service. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
