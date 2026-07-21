import os
from fastmcp import FastMCP

mcp = FastMCP("PublicMathServer")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Adds two integers together."""
    return a + b

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
