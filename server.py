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


# ---------- TOOL: an action the model decides to call ----------
@mcp.tool()
def add_expense(amount: float, category: str, note: str = "") -> str:
    """Save a new expense to expenses.json.

    Use this when the user mentions spending money. Category must be one of:
    food, transportation, utilities. Today's date is added automatically.
    """
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
    FILE.write_text(json.dumps(expenses, indent=2))
    return f"Added {amount} to {category}."


# ---------- RESOURCE: read-only data at a URI ----------
@mcp.resource("expenses://all")
def all_expenses() -> str:
    """All saved expenses as JSON. Read-only, no side effects."""
    return json.dumps(load(), indent=2)


# ---------- PROMPT: a template the user picks on purpose ----------
@mcp.prompt()
def review_my_spending() -> str:
    """Ask Claude to review my spending and suggest ways to save."""
    return (
        "Read the expenses://all resource. Tell me which category "
        "(food, transportation, or utilities) I spend the most on, "
        "and give me 2 or 3 simple tips to spend less."
    )


if __name__ == "__main__":
    mcp.run()