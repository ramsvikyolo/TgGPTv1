# handlers/basic_commands.py

from telegram import Update
from telegram.ext import CallbackContext
import config
from utils import create_menu

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id == config.ADMIN_ID:
        buttons = [
            ("Manage Shop", "manage_shop"),
            ("Settings", "settings"),
            ("Info", "info"),
        ]
    else:
        buttons = [
            ("Shop", "shop"),
            ("Help", "help"),
        ]
    
    menu = create_menu(buttons)
    update.message.reply_text("Welcome! Choose an option:", reply_markup=menu)
