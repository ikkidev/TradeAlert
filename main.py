import os
import sys
import argparse
import datetime
import secrets_manager

from market_data import AlphaVantage
from news_api import NewsApi


def main():
    input_parser = argparse.ArgumentParser(description='Get stock symbol and company name to search for from user')
    input_parser.add_argument('Stock_Symbol',
                              metavar='stock_symbol',
                              type=str,
                              help='The stock symbol to get the quote percentage difference eg:APPL')
    input_parser.add_argument('Company_Name',
                              metavar='company_name',
                              type=str,
                              help='The name of the company to search headlines for')
    input_parser.add_argument('Quote_Date',
                              metavar='quote_date',
                              type=str,
                              help='The date to search stock quote percentage difference eg: 2021-06-24'
                              )

    # Execute the parse_args() method
    args = input_parser.parse_args()

    # TODO: Sanitize user input before using them
    symbol = args.Stock_Symbol
    company = args.Company_Name
    quote_date = datetime.datetime.strptime(args.Quote_Date, '%Y-%m-%d')

    alpha_vantage_secret = "./secrets/alpha_vantage_secrets.json"
    secret = secrets_manager.get_secret(alpha_vantage_secret)
    alpha_vantage_api_key = secret.get("api_key")
    alpha_vantage_data = AlphaVantage(alpha_vantage_api_key)
    data = alpha_vantage_data.get_daily_adjusted_quote(symbol)
    percentage_difference, up_down = alpha_vantage_data.get_percentage_difference_of_quotes(data, quote_date=quote_date)

    news_api_secret_path = "./secrets/news_api_secrets.json"
    secret = secrets_manager.get_secret(news_api_secret_path)
    news_api = NewsApi(api_key=secret.get("api_key"))
    articles = news_api.get_top_headlines(keyword=company, num_of_articles=1)

    stock_price_msg = f"{symbol}: {up_down}{percentage_difference}%"
    print(stock_price_msg)
    article_headline = f"Headline: {articles[0]['title']}"
    article_brief = f"Brief: {articles[0]['description']}"
    print(article_headline)
    print(article_brief)


if __name__ == "__main__":
    main()
