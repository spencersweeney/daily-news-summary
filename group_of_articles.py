import requests
from bs4 import BeautifulSoup
from article import Article


class GroupOfArticles:
    def __init__(self, __articles=None):
        self.__articles = __articles

    def __str__(self):
        output = ''
        for group_art in self.__articles:
            article_links = '\n\t\t - '
            for i in range(len(group_art) - 1):
                article_links += f'{group_art[i]._Article__link}\n\t\t - '
            article_links += group_art[-1]._Article__link
            output += f'- {group_art[0]._Article__title}:{article_links}\n'
        return output

    def generate_articles(self, loa: [Article]):
        """
        generates groups of similar articles off a given list of articles
        :param loa: list of articles to generate groups from
        :return: nothing mutates the articles object
        """
        loloa = [[loa[0]]]
        for i in range(1, len(loa)):
            added_to_group = False
            for group_of_articles in loloa:
                if loa[i].parse(group_of_articles[0]) == 1:
                    group_of_articles.append(loa[i])
                    added_to_group = True
                    break
                elif loa[i].parse(group_of_articles[0]) == 1:
                    added_to_group = True
                    break
            if not added_to_group:
                loloa.append([loa[i]])
        self.__articles = loloa

    def group_similar(self, loa: [Article]):
        """
        sorts the given list of articles into groups with the current groups of articles
        :param loa: the list to group into the current groups
        :return: nothing mutates the articles object
        """
        for article in loa:
            for group_of_articles in self.__articles:
                added_to_group = False
                if article.parse(group_of_articles[0]) == 1:
                    group_of_articles.append(article)
                    added_to_group = True
                    break
                if article.parse(group_of_articles[0]) == 2:
                    added_to_group = True
                    break
            if not added_to_group:
                self.__articles.append([article])

    @staticmethod
    def get_articles(url: str) -> [Article]:
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
