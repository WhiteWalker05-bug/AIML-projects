Expense Tracker MCP
A small, local Model Context Protocol (MCP) server built with FastMCP that lets an AI assistant log and review personal spending through conversation.
You tell Claude "I spent 200 on lunch" and the expense is saved. Simple by design
---
Overview
Expense Tracker MCP gives an MCP-compatible AI client access to a local expense log stored in a JSON file.
The server exposes three MCP primitives:
Tools: perform operations on the expenses
Resources: expose addressable expense data
Prompts: provide a reusable instruction for reviewing spending
Expenses are limited to three categories: `food`, `transportation`, and `utilities`.
The responsibilities are intentionally separated:
```
+------------------+      stdio       +---------------------+
|  Claude Desktop  | <--------------> |  server.py (FastMCP) |
+------------------+                  +----------+----------+
        |                                        |
        |  1. model calls TOOL                   |  writes
        |     add_expense(...)  --------------->  |-----------> expenses.json
        |                                        |
        |  2. client reads RESOURCE              |  reads
        |     expenses://all    <---------------  |<----------- expenses.json
        |                                        |
        |  3. user picks PROMPT                  |
        |     review_my_spending  (tells Claude to read the resource)
```
---
Tool
`add_expense(amount, category, note="")`
Saves a new expense to `expenses.json` with today's date. Rejects any category that is not `food`, `transportation`, or `utilities`.
Example: "I paid 1500 for the electricity bill" becomes `add_expense(1500, "utilities", "electricity bill")`.
---
Resource
`expenses://all`
Returns every saved expense as JSON. Read-only, no side effects.
---
Prompt
`review_my_spending`
A reusable instruction that asks Claude to read `expenses://all`, name the category with the highest spending, and suggest 2 or 3 simple ways to spend less.
---
Project Structure
```
expense-tracker-mcp/
├── server.py               # the MCP server: 1 tool, 1 resource, 1 prompt
├── expenses.example.json   # sample data showing the file format
├── pyproject.toml          # dependencies (mcp<2) and project metadata
├── uv.lock                 # locked dependency versions
├── .python-version         # Python version used by uv
├── .gitignore              # keeps .venv and expenses.json out of Git
├── README.md               # this file
├── src/my_expense_mcp/     # package scaffold created by `uv init`, not used by the server
└── expenses.json           # created on first use, ignored by Git (your real data)
```
---
Setup
Requires uv.
```
git clone <your-repo-url>
cd expense-tracker-mcp
uv sync
```
The project pins `mcp<2` because FastMCP was renamed in MCP 2.x.
Test in the MCP Inspector
```
uv run mcp dev server.py
```
Add to Claude Desktop
Add this to `claude_desktop_config.json` (use your own paths), then fully restart Claude Desktop:
```json
{
  "mcpServers": {
    "expense-manager": {
      "command": "uv",
      "args": ["--directory", "/path/to/expense-tracker-mcp", "run", "server.py"]
    }
  }
}
```
Then try: "I spent 200 on lunch today, please save it."
