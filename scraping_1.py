import requests
from bs4 import BeautifulSoup
import time

i = 0;
for page in range(1,41):
    url = "https://news.yahoo.co.jp/flash?page={}".format(page)

    res = requests.get(url)
    #print(res.content)

    soup = BeautifulSoup(res.content)
    #print(soup)
    parent = soup.find('div', 'newsFeed')
    targets = parent.findAll('div', 'newsFeed_item_title')
    for target in targets:
        i += 1
        print(str(i) + " " + target.text)
        #time.sleep(