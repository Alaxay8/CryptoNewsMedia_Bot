from telegram import Update
from telegram.ext import CallbackContext
from bot.keyboards import get_keyboard

subscribed_users = set()
sent_articles = set()  # Набор для отслеживания отправленных новостей

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        text="Добро пожаловать! Нажмите на кнопку ниже, чтобы подписаться на новости.",
        reply_markup=get_keyboard()
    )

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if query.data == 'subscribe':
        subscribed_users.add(user_id)
        await query.edit_message_text(text="Вы подписались на новости!")
    else:
        await query.edit_message_text(text="Неизвестная команда.")
