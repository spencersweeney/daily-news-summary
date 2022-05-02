from util import similarity


class Article:
    def __init__(self, title: str, link: str):
        self.title = title
        self.link = link

    def __str__(self):
        return f'{self.title}:\n\t\t{self.link}'

    def parse(self, other_article) -> int:
        """
        decides whether the articles are the same, about the same topic, or not about the same topic
        :param other_article: the article to compare this one to
        :return: 0: articles are the same 1: articles are about the same topic 2: articles are about different topics
        """
        similarity_of_titles = similarity(self.title, other_article.title)
        if similarity_of_titles == 100:
            return 0
        elif similarity_of_titles > 20:
            return 1
        else:
            return 2
