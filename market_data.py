from abc import ABC, abstractmethod
import secrets_manager


class MarketData(ABC):

    @abstractmethod
    def __init__(self, api_key):
        self.__api_key = api_key

    @property
    @abstractmethod
    def api_key(self):
        pass

    @api_key.setter
    @abstractmethod
    def api_key(self, value):
        pass

    @abstractmethod
    def get_quote(self):
        pass

    @abstractmethod
    def get_quote_delta(self):
        pass


class AlphaVantage(MarketData):
    def __init__(self, api_key):
        self.__api_key = api_key

    @property
    def api_key(self):
        return self.__api_key

    @api_key.setter
    def api_key(self, value):
        self.__api_key = value

    def get_quote(self):
        pass

    def get_quote_delta(self):
        pass


class GoogleFinance(MarketData):
    def get_quote(self):
        pass

    def get_quote_delta(self):
        pass


class YahooFinance(MarketData):
    def get_quote(self):
        pass

    def get_quote_delta(self):
        pass
