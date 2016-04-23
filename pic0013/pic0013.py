#!/usr/bin/env python
#coding=utf-8

import urllib,re

def get_html(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def get_img(html):
    reg=r'src="(.*?\.jpg)" bdwater='
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)

    i=0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'./pic/%d.jpg'%i,Schedule)
        i+=1

def Schedule(a,b,c):
    per=100.0*a*b/c
    if per>100:
        per=100
        print '%.2f%%' %per

if __name__=='__main__':
    target_html=get_html('http://tieba.baidu.com/p/2166231880')
    get_img(target_html)

