import pickle
from group_of_articles import GroupOfArticles
from web_scraping import get_articles
from util import send_email

mailing_list = ['spencersweeney427@gmail.com']

with open('/Users/spencersweeney/Desktop/EECE2140/daily_news_summary/articles.dat', 'rb') as f:
    articles = pickle.load(f)
    for email in mailing_list:
        send_email(email, articles)

with open('/Users/spencersweeney/Desktop/EECE2140/daily_news_summary/articles.dat', 'wb') as f:
    articles = GroupOfArticles()
    articles.generate_articles(get_articles('https://www.wsj.com/'))
    pickle.dump(articles, f)
