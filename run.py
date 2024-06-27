from app import create_app
from app.utils import set_webhook
app = create_app()

if __name__ == '__main__':
    set_webhook.set_webhook()
    app.run(debug=True)
