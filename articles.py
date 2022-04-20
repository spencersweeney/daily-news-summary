class Articles:
    def __init__(self, articles=None):
        self.articles = articles

    def __str__(self):
        output = ''
        for group_art in self.articles:
            article_links = '\n\t\t - '
            for i in range(len(group_art) - 1):
                article_links += f'{group_art[i].link}\n\t\t - '
            article_links += group_art[-1].link
            output += f'- {group_art[0].title}:{article_links}\n'
        return output

    def __add__(self, other):
        return Articles(self.articles + other.articles)

    def generate_articles(self, loa):
        """
        generates groups of similar articles off a given list of articles
        :param loa: list of articles to generate groups from
        :return: nothing mutates the articles object
        """
        loloa = [[loa[0]]]
        for i in range(1, len(loa)):
            added_to_group = False
            for group_of_articles in loloa:
                if loa[i].parse(group_of_articles[0]):
                    group_of_articles.append(loa[i])
                    added_to_group = True
                    break
            if not added_to_group:
                loloa.append([loa[i]])
        self.articles = loloa

    def group_similar(self, loa):
        """
        sorts the given list of articles into groups with the current groups of articles
        :param loa: the list to group into the current groups
        :return: nothing mutates the articles object
        """
        for article in loa:
            for group_of_articles in self.articles:
                added_to_group = False
                if article.parse(group_of_articles[0]):
                    group_of_articles.append(article)
                    added_to_group = True
                    break
            if not added_to_group:
                self.articles.append([article])
