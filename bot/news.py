import requests
import os

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

async def fetch_crypto_news():
    url = f"https://newsapi.org/v2/everything?q=cryptocurrency&language=ru&sortBy=publishedAt&apiKey=edc762423eb3488a981e88167b207a43"
    response = requests.get(url)
    response.raise_for_status()
    news_data = response.json()
    articles = news_data.get('articles', [])
    return articles