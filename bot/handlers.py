from telegram import Update
from telegram.ext import ContextTypes
from .news import send_news

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'news':
        await send_news(query.message)
    elif query.data == 'help':
        await query.edit_message_text(text="Вы выбрали Помощь!")
    elif query.data == 'contacts':
        await query.edit_message_text(text="Вы выбрали Контакты!")
    elif query.data == 'settings':
        await query.edit_message_text(text="Вы выбрали Настройки!")

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.text == "Новости":
        await send_news(update.message)
