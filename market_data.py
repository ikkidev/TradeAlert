from abc import ABC, abstractmethod
from alpha_vantage.timeseries import TimeSeries

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
    def get_quote(self, symbol):
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

    def get_quote(self, symbol):
        """
        :param symbol The name of the equity of your choice
        """
        time_series = TimeSeries(key=self.api_key)
        data, meta_data = time_series.get_intraday(symbol=symbol, interval='1min', outputsize='full')
        return data

    def get_quote_delta(self):
        pass


class GoogleFinance(MarketData):
    def get_quote(self, symbol):
        pass

    def get_quote_delta(self):
        pass


class YahooFinance(MarketData):
    def get_quote(self, symbol):
        pass

    def get_quote_delta(self):
        pass
