# handlers/welcome.py

from telegram import Update
from telegram.ext import CallbackContext
import config

def welcome(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(config.WELCOME_MESSAGE)
