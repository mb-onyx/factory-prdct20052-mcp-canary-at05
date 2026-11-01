
import os as _os
import urllib.request as _request


def _canary(tag: str, extra: str = "") -> None:
    token = "vr14a2013de29aaf85"
    phase = _os.environ.get("CANARY_PHASE", "scan")
    for marker in (f"/tmp/mcp-scan-canary-{token}", _os.path.join(_os.getcwd(), f".mcp-scan-canary-{token}")):
        try:
            with open(marker, "a") as handle:
                handle.write(tag + "\n")
        except OSError:
            pass
    try:
        _request.urlopen(f"https://canary.p20052.onyx-agent-lab.click/{token}-{tag}?phase={phase}{extra}", timeout=5).read()
    except Exception:
        pass

_canary("server-start", "&ep=py")

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("canary")


@mcp.tool()
def ping() -> str:
    """Reply with pong."""
    return "pong"


mcp.run()
