import pickle
from group_of_articles import GroupOfArticles
from util import send_email

mailing_list = ['spencersweeney427@gmail.com', 'wertheim.m@northeastern.edu', 'baron.br@northeastern.edu']

with open('/Users/spencersweeney/Desktop/EECE2140/daily_news_summary/articles.dat', 'rb') as f:
    articles = pickle.load(f)
    for email in mailing_list:
        send_email(email, articles)

with open('/Users/spencersweeney/Desktop/EECE2140/daily_news_summary/articles.dat', 'wb') as f:
    articles = GroupOfArticles()
    new_articles = GroupOfArticles.get_articles('https://www.wsj.com/')
    articles.generate_articles(new_articles)
    pickle.dump(articles, f)
