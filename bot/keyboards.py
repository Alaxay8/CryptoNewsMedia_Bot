from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

def main_menu_keyboard(inline=False):
    if inline:
        keyboard = [
            [InlineKeyboardButton("Новости", callback_data='news')],
        ]
        return InlineKeyboardMarkup(keyboard)
    else:
        keyboard = [
            [KeyboardButton("Новости"), KeyboardButton("Помощь")],
            [KeyboardButton("Контакты"), KeyboardButton("Настройки")]
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
