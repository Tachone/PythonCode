#!/usr/bin/env python
#coding=utf-8

from bs4 import BeautifulSoup
import urllib
import urllib2

url='http://www.baidu.com'
def findAllLinl(url):
    #获取协议，域名
    proto,rest=urllib.splittype(url)
    domain=urllib.splithost(rest)[0]

    html=urllib2.urlopen(url).read()
    a=BeautifulSoup(html).findAll('a')
    alist=[i.attrs['href'] for i in a if i.attrs['href'][0]!='j']
    alist=map(lambda i: proto + '://'+domain+i if i[0]=='/' else url +i if i[0]=='#' else i,alist)

    return alist
if __name__=='__main__':
    for i in findAllLinl(url):
        print i


