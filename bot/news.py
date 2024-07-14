import logging

import aiohttp
import requests
from config.settings import NEWS_API_KEY

logger = logging.getLogger(__name__)

async def fetch_crypto_news():
    url = f"https://newsapi.org/v2/everything?q=cryptocurrency&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()
            return data['articles']
