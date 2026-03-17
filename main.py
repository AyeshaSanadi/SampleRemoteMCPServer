from fastmcp import FastMCP 

mcp = FastMCP(name="Simple Operation")

@mcp.tool
def add(n1: int, n2: int) -> int:
    return n1 + n2

if __name__ == "__main__":
    mcp.run(transport="http")

