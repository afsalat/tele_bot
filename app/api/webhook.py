from flask import request
from telegram import Update, Bot
from telegram.ext import Dispatcher
from config import Config
from app.handler.handlers import setup_dispatcher
from app.api import api_bp

print("runnning this page")

def init_bot():
    print(Config.TOKEN)
    bot = Bot(token=Config.TOKEN)
    dispatcher = Dispatcher(bot, None, use_context=True)
    setup_dispatcher(dispatcher)
    return bot, dispatcher

bot, dispatcher = init_bot()

@api_bp.route('/webhook', methods=['POST'])
def webhook():
    print("inside")
    """Set up the webhook to receive updates from Telegram."""
    print(request.json)
    if request.method == "POST":
        update = Update.de_json(request.get_json(), bot)
        print(update,'update')
        dispatcher.process_update(update)
    return 'ok'

@api_bp.route('/webhookz', methods=['GET'])
def webhookz():
    # print("inside webhooklog")
   
    file_name = 'example.txt'
    with open(file_name, 'w') as file:
        # Write some content to the file
        file.write('Hello, this is a sample text file.\n')

    print(f'File "{file_name}" created and written successfully.')

    
    return 'done'
