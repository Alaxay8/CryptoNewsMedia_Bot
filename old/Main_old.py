import logging
import aiohttp
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Ваш API ключ от NewsAPI и Telegram Bot
NEWS_API_KEY = 'edc762423eb3488a981e88167b207a43'
TELEGRAM_BOT_TOKEN = '7017803773:AAEUeKQEMzLxZTjFlHosoVWeJ3P1dDXrF4s'


# Функция для получения новостей
async def get_crypto_news():
    url = (
        'https://newsapi.org/v2/everything?'
        'q=cryptocurrency&'
        'language=en&'
        'sortBy=publishedAt&'
        f'apiKey={NEWS_API_KEY}'
    )
    logger.info(f"Requesting URL: {url}")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                news = await response.json()
                logger.info("News fetched successfully")
                return news
    except aiohttp.ClientError as e:
        logger.error(f"Error fetching news: {e}")
        return None


# Функция обработчик команды /start с обычными кнопками
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Создание обычных кнопок клавиатуры
    keyboard = [
        [KeyboardButton("Новости"), KeyboardButton("Помощь")],
        [KeyboardButton("Контакты"), KeyboardButton("Настройки")]
    ]

    # Создание разметки клавиатуры
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Отправка сообщения с клавиатурой
    await update.message.reply_text(
        "Привет! Выберите опцию из меню ниже:",
        reply_markup=reply_markup
    )


# Функция обработчик команды /menu с встроенными кнопками
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Создание встроенных кнопок клавиатуры
    keyboard = [
        [InlineKeyboardButton("Новости", callback_data='news')],
        [InlineKeyboardButton("Помощь", callback_data='help')],
        [InlineKeyboardButton("Контакты", callback_data='contacts')],
        [InlineKeyboardButton("Настройки", callback_data='settings')]
    ]

    # Создание разметки клавиатуры
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправка сообщения с клавиатурой
    await update.message.reply_text(
        "Привет! Выберите опцию из меню ниже:",
        reply_markup=reply_markup
    )


# Функция для обработки нажатий встроенных кнопок
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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


# Функция для отправки новостей
async def send_news(message) -> None:
    news_data = await get_crypto_news()
    if news_data and news_data['status'] == 'ok' and news_data['articles']:
        for article in news_data['articles'][:5]:
            title = article['title']
            description = article.get('description', 'No description available')
            url = article['url']
            msg = f"Title: {title}\nDescription: {description}\nURL: {url}"
            logger.info(f"Attempting to send message: {msg}")
            try:
                await message.reply_text(msg)
                logger.info("Message sent successfully")
            except Exception as e:
                logger.error(f"Failed to send message: {e}")
    else:
        logger.error("Failed to get news or news data is invalid")
        try:
            await message.reply_text("Failed to get news.")
            logger.info("Error message sent successfully")
        except Exception as e:
            logger.error(f"Failed to send error message: {e}")


# Функция для обработки сообщений с обычными кнопками
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.text == "Новости":
        await send_news(update.message)


def main() -> None:
    # Вставьте ваш токен доступа
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    # Запуск бота
    try:
        logger.info("Starting bot")
        application.run_polling()
    except Exception as e:
        logger.error(f"Error starting bot: {e}")


if __name__ == '__main__':
    main()
