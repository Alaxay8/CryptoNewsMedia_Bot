from telegram import Update
from telegram.ext import ContextTypes
from .keyboards import main_menu_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Выберите опцию из меню ниже:",
        reply_markup=main_menu_keyboard()
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Выберите опцию из меню ниже:",
        reply_markup=main_menu_keyboard(inline=True)
    )
