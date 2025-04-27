from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm your assistant bot.")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Use /start to start, and /help to get help!")
