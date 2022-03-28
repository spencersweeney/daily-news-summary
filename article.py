from util import similarity_title


class Article:
    def __init__(self, title: str, body: str, link: str):
        self.title = title
        self.body = body
        self.link = link

    def __str__(self):
        return f'{self.title}: {self.link}'

    def parse(self, other_article) -> bool:
        return similarity_title(self.title, other_article.title) > 20 \
               or similarity_body(self.body, other_article.body) > 15


# art1 = Article('Russia bombs Ukraine', 'Tension increases in russia as ...', 'www.nytimes.com/russia')
# art2 = Article('Russia attacks Ukraine', 'Tension increases in russia as ...', 'www.wsj.com/russia')
#
# art3 = Article('Smith slaps Rock', 'Will Smith slapped Chris Rock ...', 'www.nytimes.com/oscars')
#
# print(art1.parse(art2))
# print(art1.parse(art3))
