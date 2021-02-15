import pytest

from market_data import AlphaVantage

def test_instantiate_alpha_vantage_with_api_key():
    api_key = "TESTAPIKEY"
    alpha_vantage_data = AlphaVantage(api_key)
    print (alpha_vantage_data.api_key)

def test_get_quote():
    """
    Test fetching stock quotes from financial market data provider
    """
    pass

def test_get_quote_delta():
    pass