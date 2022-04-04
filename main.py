from articles import Articles
from web_scraping import get_articles

articles = Articles()
articles.generate_articles(get_articles('https://www.wsj.com/'))

print(articles)
