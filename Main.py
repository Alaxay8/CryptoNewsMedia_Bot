from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot.commands import start, button, subscribed_users, sent_articles
from bot.news import fetch_crypto_news
from bot.translator import translate_to_russian
from utils.logger import logger
from config.settings import TELEGRAM_BOT_TOKEN
import asyncio

async def send_news_task(application):
    logger.info("Получение новостей")
    news_articles = await fetch_crypto_news()
    logger.info(f"Полученные статьи: {news_articles}")
    for article in news_articles:
        title = translate_to_russian(article['title'])
        description = translate_to_russian(article['description'])
        text = f"Title: {title}\nDescription: {description}\nURL: {article['url']}"
        article_id = article['url']
        if article_id not in sent_articles:
            for user_id in subscribed_users:
                await application.bot.send_message(chat_id=user_id, text=text)
            sent_articles.add(article_id)

def start_bot():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))

    # Настройка и запуск планировщика
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_news_task, args=[application], trigger='interval', minutes=1)
    scheduler.start()

    logger.info("Starting bot")
    application.run_polling()

if __name__ == '__main__':
    start_bot()
