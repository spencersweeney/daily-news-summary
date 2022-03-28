from article import Article


class Articles:
    def __init__(self, articles):
        self.articles = articles

    def __str__(self):
        output = ''
        for group_art in self.articles:
            article_links = ''
            for i in range(len(group_art) - 1):
                article_links += f'{group_art[i].link}, '
            article_links += group_art[-1].link
            output += f'- {group_art[0].title}: {article_links}\n'
        return output


# art1 = Article('Russia bombs Ukraine', 'Tension increases in russia as ...', 'www.nytimes.com/russia')
# art2 = Article('Russia attacks Ukraine', 'Tension increases in russia as ...', 'www.wsj.com/russia')
#
# art3 = Article('Smith slaps Rock', 'Will Smith slapped Chris Rock ...', 'www.nytimes.com/oscars')
#
# g_o_art1 = Articles([[art1, art2], [art3]])
#
# print(g_o_art1)
