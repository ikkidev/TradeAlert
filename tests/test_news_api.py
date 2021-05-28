import pytest
import secrets_manager
import requests

from news_api import NewsApi



def test_get_top_headlines_from_news_api():
    secret = secrets_manager.get_secret("../secrets/news_api_secrets.json")
    news_api = NewsApi(api_key=secret.get("api_key"))
    keyword = 'TESLA'
    articles = news_api.get_top_headlines(keyword=keyword, num_of_articles=3)
    assert len(articles) == 3

    keyword = 'Articlesthatdoesnotexist1234'
    articles = news_api.get_top_headlines(keyword=keyword, num_of_articles=3)
    assert len(articles) == 0


def test_get_everything_from_news_api():
    secret = secrets_manager.get_secret("../secrets/news_api_secrets.json")
    news_api = NewsApi(api_key=secret.get("api_key"))
    keyword = 'TESLA'
    response = news_api.get_everything(keyword=keyword)

    assert response.get("status") == "ok"
    assert response.get("totalResults") >= 0


