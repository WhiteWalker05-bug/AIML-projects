import json
from datetime import date
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("expense-manager")

FILE = Path(__file__).parent / "expenses.json"
CATEGORIES = ["food", "transportation", "utilities"]


def load():
    if FILE.exists():
        return json.loads(FILE.read_text())
    return []


def save(expenses):
    FILE.write_text(json.dumps(expenses, indent=2))


# ---------- TOOLS (actions Claude can perform) ----------
@mcp.tool()
def add_expense(amount: float, category: str, note: str = "") -> str:
    """Add an expense. Category must be: food, transportation, or utilities."""
    category = category.lower()
    if category not in CATEGORIES:
        return f"Category must be one of: {', '.join(CATEGORIES)}"

    expenses = load()
    expenses.append({
        "amount": amount,
        "category": category,
        "note": note,
        "date": date.today().isoformat(),
    })
    save(expenses)
    return f"Added {amount} to {category}."


@mcp.tool()
def list_expenses() -> list:
    """Show all expenses."""
    return load()


@mcp.tool()
def total_expenses() -> dict:
    """Show the total spent in each category, and overall."""
    totals = {c: 0 for c in CATEGORIES}
    for e in load():
        totals[e["category"]] += e["amount"]
    totals["overall"] = sum(totals.values())
    return totals


# ---------- RESOURCE (read-only data Claude can look at) ----------
@mcp.resource("expenses://categories")
def categories() -> str:
    """The allowed expense categories."""
    return "\n".join(CATEGORIES)


# ---------- PROMPT (a reusable template the user can pick) ----------
@mcp.prompt()
def review_my_spending() -> str:
    """Ask Claude to review my spending."""
    return (
        "Use the list_expenses and total_expenses tools to look at my expenses. "
        "Tell me which category I spend the most on, and give me 2 or 3 simple "
        "tips to spend less."
    )


if __name__ == "__main__":
    mcp.run()
