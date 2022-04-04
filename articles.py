from article import Article


class Articles:
    def __init__(self, articles=None):
        self.articles = articles

    def __str__(self):
        output = ''
        for group_art in self.articles:
            article_links = ''
            for i in range(len(group_art) - 1):
                article_links += f'{group_art[i].link}, '
            article_links += group_art[-1].link
            output += f'- {group_art[0].title}:\n\t\t{group_art[0].body}\n\t\t{article_links}\n'
        return output

    def __add__(self, other):
        return Articles(self.articles + other.articles)

    def generate_articles(self, loa):
        loloa = [[loa[0]]]
        # i = 1
        # while i < len(loa):
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
        for article in loa:
            for group_of_articles in self.articles:
                added_to_group = False
                if article.parse(group_of_articles[0]):
                    group_of_articles.append(article)
                    added_to_group = True
                    break
            if not added_to_group:
                self.articles.append([article])


art1 = Article('Russia bombs Ukraine', 'Tension increases in russia as ...', 'www.nytimes.com/russia')
art2 = Article('Russia bombs Ukraine', 'Tension increases in russia as ...', 'www.wsj.com/russia')

art3 = Article('Smith slaps Rock', 'Will Smith slapped Chris Rock ...', 'www.nytimes.com/oscars')
art4 = Article('Hello', 'Goodbye ...', 'www.yeet.com/')

loa1 = [art1, art2, art3, art4]
loa2 = [art1, art2]
loa3 = [art1, art3]
loa4 = [art2, art4]

g_o_art1 = Articles([[art1], [art2]])
g_o_art2 = Articles([[art1], [art3]])
g_o_art3 = Articles([[art1], [art2], [art3]])
g_o_art4 = Articles([[art1], [art4], [art3]])

# articles1 = Articles()
# articles1.generate_articles(loa1)
# print(articles1)
# print('\nPrinting next test case...\n')
#
# articles2 = Articles()
# articles2.generate_articles(loa2)
# print(articles2)
# print('\nPrinting next test case...\n')
#
# articles3 = Articles()
# articles3.generate_articles(loa3)
# print(articles3)
# print('\nPrinting next test case...\n')
#
# articles3.group_similar(loa4)
# print(articles3)
# print('\nPrinting next test case...\n')

