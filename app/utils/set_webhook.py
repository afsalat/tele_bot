import requests
import sys, os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from config import Config

def set_webhook():
    print("----- ",Config.TOKEN)
    url = f'https://api.telegram.org/bot{Config.TOKEN}/setWebhook'
    data = {'url': Config.WEBHOOK_URL}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print('Webhook set successfully.')
    else:
        print('Failed to set webhook:', response.text)

if __name__ == '__main__':
    set_webhook()
