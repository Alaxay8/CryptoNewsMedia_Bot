import logging
import aiohttp
import asyncio

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Ваш API ключ от NewsAPI
NEWS_API_KEY = 'edc762423eb3488a981e88167b207a43'

# Функция для проверки API NewsAPI
async def test_newsapi():
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

async def main():
    news_data = await test_newsapi()
    if news_data:
        logger.info(f"News data: {news_data}")
    else:
        logger.error("Failed to fetch news data")

if __name__ == '__main__':
    asyncio.run(main())
