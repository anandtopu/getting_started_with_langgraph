"""Streamlit adjuster dashboard: streamlit run apps/dashboard.py."""

import hashlib
import os
import uuid

import httpx
import streamlit as st

from common.sse import decode_events, update_dashboard


def main():
    st.set_page_config(page_title="Larkspur claims", page_icon="📋")
    st.title("Larkspur Claims Copilot")
    st.caption("Synthetic training claims. Every recorded payment is a local demonstration.")
    base_url = os.environ.get("LARKSPUR_API_URL", "http://127.0.0.1:8000")
    token = st.sidebar.text_input("Adjuster access token", type="password")
    if "next_thread_id" in st.session_state:
        st.session_state["thread_input"] = st.session_state.pop("next_thread_id")
    elif "thread_input" not in st.session_state:
        st.session_state["thread_input"] = st.session_state.get("thread_id", "")
    thread_id = st.sidebar.text_input("Claim thread", key="thread_input")
    submission = st.sidebar.number_input("Synthetic submission", min_value=1, max_value=60, value=1)
    # A session can switch claims or credentials; never reuse another view's streamed text.
    scope = hashlib.sha256((base_url + "\0" + token + "\0" + thread_id).encode()).hexdigest()
    if st.session_state.get("view_scope") != scope:
        st.session_state.pop("view", None)
        st.session_state["view_scope"] = scope
    if not token:
        st.info("Enter your local adjuster token to open a claim.")
        return
    client = httpx.Client(
        base_url=base_url, headers={"Authorization": "Bearer " + token}, timeout=120
    )
    display = st.empty()

    def render(state):
        with display.container():
            st.write(" → ".join(state.get("progress", [])))
            if state.get("text"):
                st.write(state["text"])
            if state.get("error"):
                st.error(state["error"])

    def stream(path, payload=None):
        state = {"progress": [], "text": "", "pending": []}
        with client.stream("POST", path, json=payload) as response:
            response.raise_for_status()
            frame = ""
            for line in response.iter_lines():
                frame += line + "\n"
                if not line:
                    for event in decode_events(frame):
                        state = update_dashboard(state, event)
                        render(state)
                    frame = ""
        st.session_state["view"] = state
        st.session_state["view_scope"] = hashlib.sha256(
            (base_url + "\0" + token + "\0" + thread_id).encode()
        ).hexdigest()

    try:
        if st.sidebar.button("Open new claim"):
            thread_id = "claim-" + uuid.uuid4().hex
            response = client.post(
                "/threads", json={"thread_id": thread_id, "submission": int(submission)}
            )
            response.raise_for_status()
            st.session_state["thread_id"] = thread_id
            st.session_state["next_thread_id"] = thread_id
            stream(f"/threads/{thread_id}/run")
            st.rerun()
        if not thread_id:
            return
        response = client.get(f"/threads/{thread_id}")
        response.raise_for_status()
        snapshot = response.json()
        st.session_state["thread_id"] = thread_id
        render(st.session_state.get("view", {}))
        if snapshot["summary"]:
            st.success(snapshot["summary"]["status"])
            st.write(snapshot["summary"]["letter"])
        for pending in snapshot["interrupts"]:
            request = pending["request"]
            st.write(request)
            if request.get("kind") == "estimate_wait":
                document_id = st.text_input("Estimate document ID", value="DOC-ESTIMATE")
                received_on = st.date_input(
                    "Receipt date", value=__import__("datetime").date(2026, 1, 4)
                )
                if st.button("Attach estimate", key=pending["id"]):
                    stream(
                        f"/threads/{thread_id}/resume",
                        {
                            "interrupt_id": pending["id"],
                            "document_id": document_id,
                            "received_on": received_on.isoformat(),
                        },
                    )
                    st.rerun()
            else:
                confirmed = st.checkbox(
                    "I checked the policy coverage", key="coverage-" + pending["id"]
                )
                approve, reject = st.columns(2)
                if approve.button(
                    "Approve",
                    key="yes-" + pending["id"],
                    disabled=request.get("kind") == "payment_approval" and not confirmed,
                ):
                    stream(
                        f"/threads/{thread_id}/resume",
                        {
                            "interrupt_id": pending["id"],
                            "approved": True,
                            "coverage_confirmed": confirmed,
                        },
                    )
                    st.rerun()
                if reject.button("Reject", key="no-" + pending["id"]):
                    stream(
                        f"/threads/{thread_id}/resume",
                        {"interrupt_id": pending["id"], "approved": False},
                    )
                    st.rerun()
        if (
            not snapshot["interrupts"]
            and not snapshot["summary"]
            and st.button("Continue interrupted run")
        ):
            stream(f"/threads/{thread_id}/run")
            st.rerun()
    except httpx.HTTPStatusError as error:
        st.error(
            f"The API returned {error.response.status_code}. Refresh the thread and check your access."
        )
    except httpx.RequestError:
        st.error("The local claims API is unavailable. Start it using the deployment guide.")
    finally:
        client.close()


if __name__ == "__main__":
    main()
