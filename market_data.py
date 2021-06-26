from abc import ABC, abstractmethod
from alpha_vantage.timeseries import TimeSeries
from datetime import date
from datetime import timedelta

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

    def get_daily_adjusted_quote(self, symbol, output_format='pandas'):
        """
        :param symbol: The name of the equity of your choice
        :param output_format: The output format of your choice (json, csv or pandas)
        :return: data:  The raw (as-traded) daily open/high/low/close/volume values, daily adjusted close values,
                        and historical split/dividend events of the specified equity,
                        covering 20+ years of historical data.
        """
        time_series = TimeSeries(key=self.api_key, output_format=output_format)
        data, meta_data = time_series.get_daily_adjusted(symbol)
        return data

    def get_percentage_difference_of_quotes(self, data, quote_date=None):
        """
        Calculate the difference between the closing quote of day before quote_date and 2 days before quote_date
        :param data: The pandas dataframe with the adjusted daily quotes historical data
        :param quote_date: The date for the quote
        :return: percentage_difference: percentage difference of quote rounded to the closest integer
                 up_down:               whether the price went up or down
        """
        today = quote_date or date.today()
        yesterday = today - timedelta(days=1)
        yesterday = yesterday.strftime('%Y-%m-%d')
        day_before_yesterday = today - timedelta(days=2)
        day_before_yesterday = day_before_yesterday.strftime('%Y-%m-%d')

        yesterday_closing_price = data.loc[yesterday, '5. adjusted close'][0]
        day_before_yesterday_closing_price = data.loc[day_before_yesterday, '5. adjusted close'][0]
        difference = yesterday_closing_price - day_before_yesterday_closing_price

        up_down = 0
        if difference > 0:
            up_down = "🔺"
        else:
            up_down = "🔻"

        percentage_difference = round(difference / yesterday_closing_price * 100)
        return percentage_difference, up_down


class YahooFinance(MarketData):
    def get_quote(self, symbol):
        pass

    def get_quote_delta(self):
        pass
