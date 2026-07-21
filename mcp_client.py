import asyncio
import os
from mcp.client.sse import sse_client
from mcp.client.session import ClientSession

async def main():
    url = os.getenv("MCP_SERVER_URL", "http://localhost:7860/sse")
    print(f"Connecting to MCP Server at {url}...")
    
    try:
        async with sse_client(url) as streams:
            async with ClientSession(streams[0], streams[1]) as session:
                await session.initialize()
                tools = await session.list_tools()
                print(f"Available tools: {[t.name for t in tools.tools]}")
                print("Executing add_numbers(a=14, b=28)...")
                result = await session.call_tool("add_numbers", arguments={"a": 14, "b": 28})
                print(f"Result: {result.content[0].text}")
    except Exception as e:
        print(f"Connection failed: {e}\nMake sure the server is running!")

if __name__ == "__main__":
    asyncio.run(main())
