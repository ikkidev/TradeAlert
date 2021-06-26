import pytest
import secrets_manager
import datetime

from market_data import AlphaVantage
from pandas import DataFrame, read_csv


def test_instantiate_alpha_vantage_with_api_key():
    """
    Test instantiating alpha_vantage with api key
    """
    api_key = "TESTAPIKEY"
    alpha_vantage_data = AlphaVantage(api_key)
    print (alpha_vantage_data.api_key)

def test_alpha_vantage_get_quote():
    """
    Test fetching stock quotes from alpha vantage
    """
    path = "../secrets/alpha_vantage_secrets.json"
    secret = secrets_manager.get_secret(path)
    api_key = secret.get("api_key")

    alpha_vantage_data = AlphaVantage(api_key)
    data = alpha_vantage_data.get_quote('TSLA')
    print(data)
    assert isinstance(data, dict) is True

def test_alpha_vantage_get_daily_adjusted_quote():
    """
    Test fetching daily adjusted stock quote from alpha vantage
    """
    path = "../secrets/alpha_vantage_secrets.json"
    secret = secrets_manager.get_secret(path)
    api_key = secret.get("api_key")

    alpha_vantage_data = AlphaVantage(api_key)
    data = alpha_vantage_data.get_daily_adjusted_quote('TSLA')
    assert isinstance(data, DataFrame) is True


def test_alpha_vantage_get_percentage_difference_of_quotes():
    """
    Test calculating the difference of price
    """
    path = "../secrets/alpha_vantage_secrets.json"
    secret = secrets_manager.get_secret(path)
    api_key = secret.get("api_key")
    alpha_vantage_data = AlphaVantage(api_key)
    data = read_csv('TEST_DAILY_ADJUSTED_QUOTE.csv', index_col='date', parse_dates=True)
    quote_date = datetime.datetime.strptime("2021-02-12", '%Y-%m-%d')
    percentage_difference, up_down = alpha_vantage_data.get_percentage_difference_of_quotes(data, quote_date)
    assert percentage_difference == 1
    assert up_down == "🔺"

