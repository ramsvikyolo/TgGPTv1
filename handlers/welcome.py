from telegram import Update
from telegram.ext import CallbackContext

from config import WELCOME_MESSAGE

def welcome(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_text(f"{WELCOME_MESSAGE}, {user.first_name}!")
