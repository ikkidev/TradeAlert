from abc import ABC, abstractmethod
from alpha_vantage.timeseries import TimeSeries
import datetime
import pandas


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

    def get_daily_adjusted_quote(self, symbol, output_format):
        time_series = TimeSeries(key=self.api_key, output_format=output_format)
        data, meta_data = time_series.get_daily_adjusted(symbol)
        return data

    def get_percentage_difference_of_quotes(self, data):
        """
        Calculate the difference between the closing quote of yesterday and day before yesterday
        :param data:
        :return: percentage_difference: percentage difference of quote rounded to the closest integer
                 up_down:               whether the price went up or down
        """

        yesterday_closing_price = data.loc[0, '5. adjusted close']
        day_before_yesterday_closing_price = data.loc[1, '5. adjusted close']
        difference = yesterday_closing_price - day_before_yesterday_closing_price

        up_down = 0
        if difference > 0:
            up_down = "🔺"
        else:
            up_down = "🔻"

        percentage_difference = round(difference / yesterday_closing_price * 100)
        return percentage_difference, up_down


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
