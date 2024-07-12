from telegram import Update
from telegram.ext import ContextTypes
from .keyboards import subscribe_keyboard
from .news import send_news


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Нажмите кнопку ниже, чтобы подписаться на новости:",
        reply_markup=subscribe_keyboard()
    )


async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="Вы подписались на новости. Вы будете получать новости сразу после их публикации.")

    # Отправляем новости сразу после подписки
    await send_news(query.message)
