import requests

from news_api_auth import NewsApiAuth
import news_api_const


class NewsApi:
    """
    Handles implementation to fetch data from News API endpoints `https://newsapi.org/docs/endpoints`
    :param api_key: Your News API key `https://newsapi.org/register`
    :type api_key: str
    """

    def __init__(self, api_key, session=None):
        self.auth = NewsApiAuth(api_key=api_key)
        self.request_method = requests

    #TODO: Add support to pass country parameter
    def get_top_headlines(self, keyword, num_of_articles):
        """
        Return top num_of_articles from news api top headlines endpoint

        :param keyword: keyword to search for in body and title of news articles
        :type keyword: str

        :param num_of_articles: number of articles to return
        :type num_of_articles: int

        :return List of articles found from the api
        :rtype: list
        :raises HTTP error from api if one occurs
        """

        payload = dict()
        payload["q"] = keyword
        response = self.request_method.get(news_api_const.TOP_HEADLINES_URL, auth=self.auth, timeout=30, params=payload)
        response.raise_for_status()
        articles = response.json().get("articles")[:num_of_articles]
        #TODO: Add logger for debugging msg
        #print(f'Found {num_of_articles} articles: {articles}')
        return articles

    def get_everything(self, keyword,
                       keyword_in_title=None,
                       num_of_articles=None,
                       pageSize=None,
                       page=None):
        """
        Return articles from news api everything endpoint

        :param keyword: keyword to search for in news articles
        :type keyword: str

        :param keyword_in_title: keyword to search in the title of news articles
        :type keyword: str

        :poram pageSize: The number of results to return per page
        :type pageSize: int

        :param page: Use this to page through the results
        :type page: int

        :return JSON response from the api
        :rtype: dict
        :raises HTTP error from api if one occurs
        """

        payload = dict()
        payload["q"] = keyword
        payload["qintitle"] = keyword_in_title
        payload["pageSize"] = pageSize
        payload["page"] = page

        response = self.request_method.get(news_api_const.TOP_HEADLINES_URL, auth=self.auth, timeout=30, params=payload)
        response.raise_for_status()
        return response.json()