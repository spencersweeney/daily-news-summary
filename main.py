import pickle
from articles import Articles
from web_scraping import get_articles
from util import send_email

with open('/Users/spencersweeney/Desktop/EECE2140/daily_news_summary/articles.dat', 'rb') as f:
    articles = pickle.load(f)
    send_email('spencersweeney427@gmail.com', articles)

with open('/Users/spencersweeney/Desktop/EECE2140/daily_news_summary/articles.dat', 'wb') as f:
    articles = Articles()
    articles.generate_articles(get_articles('https://www.wsj.com/'))
    pickle.dump(articles, f)
