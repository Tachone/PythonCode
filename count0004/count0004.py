#!/usr/bin/env python
#coding=utf-8

#统计文章中的单词个数
import re

def file_read(filename):
    with open(filename,'r') as fd:
        article=fd.read()
        return article

def counter(string):
    words=re.findall(r'[A-Za-z0-9]+',string)
    amount=len(words)
    return str(amount)

if __name__=='__main__':
    string=file_read('Github.txt')
    res=counter(string)
    print 'There are',res,'words in this article.'

