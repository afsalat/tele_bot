from flask import request
from telegram import Update, Bot
from telegram.ext import Dispatcher
from config import Config
from handlers import setup_dispatcher
from app.api import api_bp


def init_bot():
    print(Config.TOKEN)
    bot = Bot(token=Config.TOKEN)
    dispatcher = Dispatcher(bot, None, use_context=True)
    setup_dispatcher(dispatcher)
    return bot, dispatcher

bot, dispatcher = init_bot()

api_bp.route('/webhook', methods=['POST'])
def webhook():
    """Set up the webhook to receive updates from Telegram."""
    print(request.json)
    if request.method == "POST":
        update = Update.de_json(request.get_json(), bot)
        dispatcher.process_update(update)
    return 'ok'
