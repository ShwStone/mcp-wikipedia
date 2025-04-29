# mcp-wikipedia

MCP server to give client the ability to access Wikipedia pages

# Usage

First run:

```
cd <path of MCP servers>
git clone https://github.com/ShwStone/mcp-wikipedia.git
```

Then configure:

```json
{
  "mcpServers": {
    "wikipedia": {
      "command": "uv",
      "args": [
        "--directory",
        "<path of MCP servers>/mcp-wikipedia",
        "run",
        "python",
        "main.py"
      ]
    }
  }
}
```
