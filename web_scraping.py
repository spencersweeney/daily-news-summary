import requests
from bs4 import BeautifulSoup

from article import Article


def get_articles(url) -> [Article]:

    r1 = requests.get(url)

    coverpage = r1.content
    soup1 = BeautifulSoup(coverpage, 'html.parser')
    coverpage_news = soup1.find_all('article')

    articles = []
    for article in coverpage_news:
        articles.append(Article(article.get_text(),
                                article.find_all('span', class_='WSJTheme--summaryText--2LRaCWgJ'),
                                article.find('a').get('href')))
    return articles


