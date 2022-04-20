from util import similarity_title


class Article:
    def __init__(self, title: str, body: str, link: str):
        self.title = title
        self.body = body
        self.link = link

    def __str__(self):
        return f'{self.title}:\n\t\t{self.link}'

    def parse(self, other_article) -> bool:
        """
        decides whether the articles are about the same topic or not
        :param other_article: the article to compare this one to
        :return: boolean value of whether the articles are about the same topic or not
        """
        return similarity_title(self.title, other_article.title) > 25

