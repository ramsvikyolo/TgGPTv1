# app.py

import os
from flask import Flask
from flask import Flask, request
from telegram import Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext import Updater
import config
from handlers.welcome import welcome
from handlers.basic_commands import start

app = Flask(__name__)

updater = Updater(token=config.TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

@app.route('/')
def index():
    return "Bot is running!"

@app.route(f"/{config.TELEGRAM_TOKEN}", methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), updater.bot)
    dispatcher.process_update(update)
    return 'ok'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's PORT, default to 5000 if not set
    app.run(host='0.0.0.0', port=port)
