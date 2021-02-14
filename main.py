from abc import ABC, abstractmethod


class MarketData(ABC):
    @abstractmethod
    def get_quote(self):
        pass

    @abstractmethod
    def get_quote_delta(self):
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
