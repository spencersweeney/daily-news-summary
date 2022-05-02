import requests
from bs4 import BeautifulSoup
from article import Article


def get_articles(url) -> [Article]:
    """
    get the current top articles from the given url
    :param url: the news website to get the articles from
    :return: a list of the articles taken from the website
    """
    r1 = requests.get(url)

    webpage = r1.content
    soup1 = BeautifulSoup(webpage, 'html.parser')
    webpage_news = soup1.find_all('article')

    articles = []
    for article in webpage_news:
        articles.append(Article(article.get_text(': '),
                                article.find('a').get('href')))
    return articles
