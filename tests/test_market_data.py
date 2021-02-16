import pytest
import secrets_manager

from market_data import AlphaVantage

def test_instantiate_alpha_vantage_with_api_key():
    """
    Test instantiating alpha_vantage with api key
    """
    api_key = "TESTAPIKEY"
    alpha_vantage_data = AlphaVantage(api_key)
    print (alpha_vantage_data.api_key)

def test_get_quote_from_alpha_vantage():
    """
    Test fetching stock quotes from alpha vantage
    """
    path = "../alpha_vantage_secrets.json"
    secret = secrets_manager.get_secret(path)
    api_key = secret.get("api_key")

    alpha_vantage_data = AlphaVantage(api_key)
    data = alpha_vantage_data.get_quote('TSLA')
    print(data)
    assert isinstance(data, dict) is True

def test_get_quote_delta():
    pass