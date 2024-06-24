from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Filters, dispatcher
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context):
    """Send a message when the command /start is issued."""
    print("ttttttttt")
    update.message.reply_text('Hi!')

def help_command(update: Update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update: Update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update: Update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def setup_dispatcher(dispatcher: dispatcher):
    """Add handlers to the dispatcher."""
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dispatcher.add_error_handler(error)
