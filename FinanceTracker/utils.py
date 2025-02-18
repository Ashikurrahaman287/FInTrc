from typing import Union
from datetime import datetime

def validate_amount(amount_str: str) -> Union[float, str]:
    """Validate and convert amount string to float."""
    try:
        amount = float(amount_str)
        if amount <= 0:
            return "Amount must be greater than zero! ❌"
        return amount
    except ValueError:
        return "Please enter a valid number! ❌"

def format_amount(amount: float) -> str:
    """Format amount with currency symbol."""
    return f"${amount:.2f}"

def format_transaction(transaction) -> str:
    """Format transaction for display."""
    type_text = "Received" if transaction.type == "debt" else "Paid"
    return (
        f"{type_text} {format_amount(transaction.amount)} "
        f"({transaction.category})"
        f"{f' - {transaction.description}' if transaction.description else ''}"
    )

def format_today_summary(transactions) -> str:
    """Format today's transactions summary."""
    if not transactions:
        return "No transactions today! 📅"
    
    total_debt = sum(t.amount for t in transactions if t.type == 'debt')
    total_credit = sum(t.amount for t in transactions if t.type == 'credit')
    
    summary = f"📅 Today's Summary:\n"
    summary += f"Total Credit: {format_amount(total_credit)}\n"
    summary += f"Total Debt: {format_amount(total_debt)}\n\n"
    summary += "Transactions:\n"
    for t in transactions:
        summary += f"• {format_transaction(t)}\n"
    
    return summary

def format_summary(summary: dict) -> str:
    """Format overall summary."""
    return (
        f"💰 Summary:\n"
        f"Net Balance: {format_amount(summary['net_balance'])}\n"
        f"Total Debt: {format_amount(summary['total_debt'])}\n"
        f"Total Credit: {format_amount(summary['total_credit'])}"
    )

def format_categories(categories: dict) -> str:
    """Format category summary."""
    if not categories:
        return "No transactions in any category yet! 📊"
    
    result = "📊 Category Summary:\n"
    for category, amount in categories.items():
        result += f"• {category}: {format_amount(abs(amount))}\n"
    return result
