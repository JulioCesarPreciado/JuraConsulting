from urllib.request import urlopen
import bs4
import pandas as pd
import numpy as np

url = 'https://es.pornhub.com/'
#url = 'http://ligamx.net/'
html = urlopen(url).read()
soup = bs4.BeautifulSoup(html, "html.parser")

videos = soup.findAll("ul", {"class": "videos-morepad videos full-row-thumbs videos-being-watched logInHotContainer"})[0].findAll('li')

for video in videos:
    titles = video.findAll('span',{'class': 'title'})
    for title in titles:
        print(title.a.string) 

