import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from handlers import start_handler, help_handler, message_handler, admin_handler

# Load environment variables (your token)
TELEGRAM_TOKEN = os.environ.get(8015540396:AAHGX0kwF5jpXcm4d06nE01_zPNs1lvBgwA)

# Flask app
app = Flask(__name__)

# Telegram bot and dispatcher
bot = Bot(token=8015540396:AAHGX0kwF5jpXcm4d06nE01_zPNs1lvBgwA)
dispatcher = Dispatcher(bot, None, workers=4)

# Command handlers
dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(CommandHandler('help', help_handler))
dispatcher.add_handler(CommandHandler('admin', admin_handler))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

# Route for Telegram webhook
@app.route(f'/8015540396:AAHGX0kwF5jpXcm4d06nE01_zPNs1lvBgwA', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

# Root route for testing
@app.route('/')
def index():
    return 'Bot is running!'

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT)
