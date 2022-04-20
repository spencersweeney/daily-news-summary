import pickle
from web_scraping import get_articles

with open('/Users/spencersweeney/Desktop/EECE2140/daily_news_summary/articles.dat', 'rb') as f:
    articles = pickle.load(f)
with open('/Users/spencersweeney/Desktop/EECE2140/daily_news_summary/articles.dat', 'wb') as f:
    new_articles = get_articles('https://www.wsj.com/')
    articles.group_similar(new_articles)
    pickle.dump(articles, f)

