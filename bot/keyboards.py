from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

def main_menu_keyboard(inline=False):
    if inline:
        keyboard = [
            [InlineKeyboardButton("Новости", callback_data='news')],
            [InlineKeyboardButton("Помощь", callback_data='help')],
            [InlineKeyboardButton("Контакты", callback_data='contacts')],
            [InlineKeyboardButton("Настройки", callback_data='settings')]
        ]
        return InlineKeyboardMarkup(keyboard)
    else:
        keyboard = [
            [KeyboardButton("Новости"), KeyboardButton("Помощь")],
            [KeyboardButton("Контакты"), KeyboardButton("Настройки")]
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
