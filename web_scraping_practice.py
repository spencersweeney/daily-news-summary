from bs4 import BeautifulSoup
import requests


r1 = requests.get('https://www.wsj.com/')
coverpage = r1.content

soup1 = BeautifulSoup(coverpage, 'html.parser')

coverpage_news = soup1.find_all('article')
print(coverpage_news)



