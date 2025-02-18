from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    CallbackContext,
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    Filters,
)
from constants import *
from storage import storage, Transaction
from utils import (
    validate_amount,
    format_today_summary,
    format_summary,
    format_categories,
)

def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
    update.message.reply_text(WELCOME_MESSAGE)

def help_command(update: Update, context: CallbackContext) -> None:
    """Handle the /help command."""
    update.message.reply_text(HELP_MESSAGE)

def today(update: Update, context: CallbackContext) -> None:
    """Handle the /today command."""
    user_id = update.message.from_user.id
    transactions = storage.get_today_transactions(user_id)
    update.message.reply_text(format_today_summary(transactions))

def summary(update: Update, context: CallbackContext) -> None:
    """Handle the /summary command."""
    user_id = update.message.from_user.id
    summary = storage.get_user_summary(user_id)
    update.message.reply_text(format_summary(summary))

def categories(update: Update, context: CallbackContext) -> None:
    """Handle the /categories command."""
    user_id = update.message.from_user.id
    categories = storage.get_category_summary(user_id)
    update.message.reply_text(format_categories(categories))

def start_transaction(update: Update, context: CallbackContext, transaction_type: str) -> int:
    """Start the transaction conversation."""
    context.user_data['transaction_type'] = transaction_type
    update.message.reply_text(
        f"Enter amount {MONEY_EMOJI}:",
        reply_markup=ReplyKeyboardRemove()
    )
    return AMOUNT

def amount_received(update: Update, context: CallbackContext) -> int:
    """Handle amount input."""
    amount_str = update.message.text
    amount_result = validate_amount(amount_str)

    if isinstance(amount_result, str):
        update.message.reply_text(amount_result)
        return AMOUNT

    context.user_data['amount'] = amount_result
    reply_markup = ReplyKeyboardMarkup(
        [[cat] for cat in DEFAULT_CATEGORIES],
        one_time_keyboard=True
    )
    update.message.reply_text(
        f"Select or enter category {CATEGORY_EMOJI}:",
        reply_markup=reply_markup
    )
    return CATEGORY

def category_received(update: Update, context: CallbackContext) -> int:
    """Handle category input."""
    context.user_data['category'] = update.message.text
    update.message.reply_text(
        f"Add description (optional) {NOTE_EMOJI} or send /skip:",
        reply_markup=ReplyKeyboardRemove()
    )
    return DESCRIPTION

def skip_description(update: Update, context: CallbackContext) -> int:
    """Handle skipping description."""
    return description_received(update, context)

def description_received(update: Update, context: CallbackContext) -> int:
    """Handle description input and save transaction."""
    user_data = context.user_data
    description = "" if update.message.text == "/skip" else update.message.text

    transaction = Transaction(
        user_id=update.message.from_user.id,
        amount=user_data['amount'],
        category=user_data['category'],
        description=description,
        transaction_type=user_data['transaction_type']
    )

    storage.add_transaction(transaction)

    update.message.reply_text(
        f"Transaction saved! {CHECK_EMOJI}",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    """Cancel the conversation."""
    update.message.reply_text(
        f"Transaction cancelled {ERROR_EMOJI}",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

def get_transaction_handler(transaction_type: str) -> ConversationHandler:
    """Create conversation handler for transactions."""
    return ConversationHandler(
        entry_points=[
            CommandHandler(
                transaction_type,
                lambda update, context: start_transaction(update, context, transaction_type)
            )
        ],
        states={
            AMOUNT: [MessageHandler(Filters.text & ~Filters.command, amount_received)],
            CATEGORY: [MessageHandler(Filters.text & ~Filters.command, category_received)],
            DESCRIPTION: [
                MessageHandler(Filters.text & ~Filters.command, description_received),
                CommandHandler("skip", skip_description)
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )