from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def subscribe_keyboard():
    keyboard = [
        [InlineKeyboardButton("Подписаться на новости", callback_data='subscribe')]
    ]
    return InlineKeyboardMarkup(keyboard)
