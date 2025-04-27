# utils.py

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def create_menu(buttons, row_width=2):
    """
    Creates an inline button menu.
    buttons: list of tuples (text, callback_data)
    row_width: how many buttons per row
    """
    keyboard = []
    temp = []
    for idx, button in enumerate(buttons, start=1):
        temp.append(InlineKeyboardButton(button[0], callback_data=button[1]))
        if idx % row_width == 0:
            keyboard.append(temp)
            temp = []
    if temp:
        keyboard.append(temp)
    return InlineKeyboardMarkup(keyboard)
