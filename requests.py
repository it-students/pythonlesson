import requests
from bs4 import BeautifulSoup
import re

uri = 'https://ja.wikipedia.org/wiki/%E5%B8%B8%E7%94%A8%E6%BC%A2%E5%AD%97%E4%B8%80%E8%A6%A7'
soup = BeautifulSoup(requests.get(uri).text, 'lxml')
tags  = soup.find_all('a', title=re.compile("wikt:."))

for tag in tags:
    print(tag.text)