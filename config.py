from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    WEBHOOK_URL = os.getenv('WEBHOOK_URL')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///telegram_bot.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False