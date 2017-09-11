# 使用bs

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.con/pages/page1.html")
bsObj = BeautifulSoup(html.read(),"lxml")
print(bsObj.h1)
