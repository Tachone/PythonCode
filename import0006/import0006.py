#!/usr/bin/env python
#coding=utf-8

# 统计每个文件中出现次数最多的词

import os,re

def listword(string):
    words=re.findall(r'[a-zA-Z]+',string)
    return words

def file_read(filename):
    with open(filename,'r') as fd:
        article=fd.read()
    return article

def most_word_number(word_list):
    str_dict={}
    for item in word_list:
        if item in str_dict:
            str_dict[item]+=1
        else:
            str_dict[item]=1
    str_dict={str_dict[key]:key for key in str_dict}
    return (max(str_dict),str_dict[max(str_dict)])

def solve(file_path):
    file_list=os.listdir(file_path)
    for x in file_list:
        if os.path.isfile(x) and os.path.splitext(x)[1]=='.txt':
            try:
                words=listword(file_read(x))
                times,word=most_word_number(words)
            except:
                print 'Open %s Error' %x

    print 'Word: ',word,'appears %d times' %times

if __name__=='__main__':
    solve('.')

