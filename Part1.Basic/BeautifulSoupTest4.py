# 使用bs4处理子标签和其他后代标签

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html.parser")

for child in bsObj.find("table",{"id","giftlist"}).children:
    print(child)
