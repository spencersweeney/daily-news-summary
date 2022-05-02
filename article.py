from util import similarity


class Article:
    def __init__(self, __title: str, __link: str):
        self.__title = __title
        self.__link = __link

    def __str__(self):
        return f'{self.__title}:\n\t\t{self.__link}'

    def parse(self, other_article) -> int:
        """
        decides whether the articles are the same, about the same topic, or not about the same topic
        :param other_article: the article to compare this one to
        :return: 0: articles are the same 1: articles are about the same topic 2: articles are about different topics
        """
        similarity_of_titles = similarity(self.__title, other_article.__title)
        if similarity_of_titles == 100:
            return 0
        elif similarity_of_titles > 20:
            return 1
        else:
            return 2
