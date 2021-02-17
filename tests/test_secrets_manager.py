import pytest
import secrets_manager


def test_read_alpha_vantage_api_key():
    path = '../secrets/alpha_vantage_secrets.json'
    secret = secrets_manager.get_secret(path)
    assert secret.get("api_key") is not None

def test_read_news_api_api_key():
    path = '../secrets/news_api_secrets.json'
    secret = secrets_manager.get_secret(path)
    assert secret.get("api_key") is not None

