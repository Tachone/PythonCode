#!/usr/bin/env python
#coding=utf-8

#HTML找出正文

import requests
from bs4 import BeautifulSoup

url='http://www.baidu.com'
html=requests.get(url)

soup=BeautifulSoup(html.text)
print soup.body.text.encode('GBK','ignore').decode('GBK')

