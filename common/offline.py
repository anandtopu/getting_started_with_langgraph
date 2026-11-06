"""Execute a course script with network access disabled, after installation."""

import os
import runpy
import socket
import sys
from contextvars import ContextVar
from pathlib import Path
from types import FunctionType

_PAIR_CONTEXT = ContextVar("internal_socketpair", default=False)
_PAIR_INSTALLED = False


def install_socketpair_compatibility() -> None:
    """Allow Windows asyncio's own connected pair, without opening general networking.

    Windows implements socketpair in Python using loopback sockets. Clone only
    that standard-library function's globals so pytest's socket guard can still
    reject every normal socket constructor. No remote host can be supplied.
    """
    global _PAIR_INSTALLED
    if os.name != "nt" or _PAIR_INSTALLED:
        return
    if not isinstance(socket.socketpair, FunctionType):
        _PAIR_INSTALLED = True
        return
    original = socket.socket
    accept = original.accept
    safe_accept = FunctionType(
        accept.__code__, {**accept.__globals__, "socket": original}, argdefs=accept.__defaults__
    )

    class PairSocket(original):
        def accept(self):
            return safe_accept(self)

    pair = socket.socketpair
    safe_pair = FunctionType(
        pair.__code__, {**pair.__globals__, "socket": PairSocket}, argdefs=pair.__defaults__
    )

    def internal_pair(*args, **kwargs):
        token = _PAIR_CONTEXT.set(True)
        try:
            return safe_pair(*args, **kwargs)
        finally:
            _PAIR_CONTEXT.reset(token)

    socket.socketpair = internal_pair
    _PAIR_INSTALLED = True


def block_network(event: str, arguments: tuple) -> None:
    if (
        event in {"socket.connect", "socket.getaddrinfo", "socket.sendto"}
        and not _PAIR_CONTEXT.get()
    ):
        raise RuntimeError("Offline course execution attempted network access.")


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python -m common.offline SCRIPT [arguments]")
    path = Path(sys.argv[1]).resolve()
    os.environ["LARKSPUR_OFFLINE"] = "1"
    os.environ["LANGSMITH_TRACING"] = "false"
    os.environ["LANGCHAIN_TRACING_V2"] = "false"
    install_socketpair_compatibility()
    sys.addaudithook(block_network)
    sys.argv = [str(path), *sys.argv[2:]]
    runpy.run_path(str(path), run_name="__main__")


if __name__ == "__main__":
    main()
