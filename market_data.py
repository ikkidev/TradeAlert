from abc import ABC, abstractmethod
import secrets_manager


class MarketData(ABC):
    api_key: str

    @abstractmethod
    def get_quote(self):
        pass

    @abstractmethod
    def get_quote_delta(self):
        pass

    @abstractmethod
    def get_api_key(self, path):
        pass


class AlphaVantage(MarketData):
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
