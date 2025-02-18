import os
import logging
from telegram.ext import (
    Updater,
    CommandHandler,
)

from handlers import (
    start,
    help_command,
    today,
    summary,
    categories,
    get_transaction_handler,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    """Start the bot."""
    # Get token from environment variable
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        logger.error("No token found! Set TELEGRAM_BOT_TOKEN environment variable.")
        return

    # Create updater and dispatcher
    updater = Updater(token)
    dispatcher = updater.dispatcher

    # Add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("today", today))
    dispatcher.add_handler(CommandHandler("summary", summary))
    dispatcher.add_handler(CommandHandler("categories", categories))

    # Add transaction handlers
    dispatcher.add_handler(get_transaction_handler("debt"))
    dispatcher.add_handler(get_transaction_handler("credit"))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()