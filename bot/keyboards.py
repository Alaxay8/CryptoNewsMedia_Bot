from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard():
    keyboard = [
        [InlineKeyboardButton(text="Подписаться на новости", callback_data='subscribe')]
    ]
    return InlineKeyboardMarkup(keyboard)
