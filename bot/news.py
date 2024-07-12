import aiohttp
import logging
from telegram import Message
from deep_translator import GoogleTranslator
from bot.messages import send_text_message
from config.settings import NEWS_API_KEY

logger = logging.getLogger(__name__)


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


async def send_news(message: Message) -> None:
    news_data = await get_crypto_news()
    if news_data and news_data['status'] == 'ok' and news_data['articles']:
        translator = GoogleTranslator(source='en', target='ru')
        for article in news_data['articles'][:1]:  # Отправляем только одну самую свежую новость
            title = article['title']
            description = article.get('description', 'No description available')
            url = article['url']

            # Переводим заголовок и описание на русский
            title_ru = translator.translate(title)
            description_ru = translator.translate(description)

            msg = f"⚡️ Молния ⚡️\n\nЗаголовок: {title_ru}\n\nОписание: {description_ru}\n\nСсылка: {url}"
            await send_text_message(message, msg)
    else:
        await send_text_message(message, "Не удалось получить новости.")
