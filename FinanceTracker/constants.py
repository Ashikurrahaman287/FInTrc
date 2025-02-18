# Bot messages and emoji constants
WELCOME_MESSAGE = """
Welcome to FinTrackBot! 💰
Track your debts, credits, and expenses effortlessly.
Use /help to see available commands.
"""

HELP_MESSAGE = """
Available commands:
/start - Start the bot
/debt - Log money owed to you
/credit - Log money you owe
/today - View today's transactions
/summary - View your balance summary
/categories - View spending by category
/help - Show this help message

Use the commands to start tracking your finances! 📊
"""

# Emoji constants
MONEY_EMOJI = "💸"
CATEGORY_EMOJI = "🏷️"
NOTE_EMOJI = "📝"
CHECK_EMOJI = "✅"
ERROR_EMOJI = "❌"

# States for conversation handling
AMOUNT = 0
CATEGORY = 1
DESCRIPTION = 2

# Default categories
DEFAULT_CATEGORIES = [
    "Food",
    "Transport",
    "Bills",
    "Entertainment",
    "Friend",
    "Business",
    "Other"
]