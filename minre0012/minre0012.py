#!/usr/bin/env python
#coding=utf-8


if __name__=='__main__':
    word_set=set()
    with open('filtered_words.txt','r') as f:
        for x in f.readlines():
            word_set.add(x.strip("\n"))

    while True:
        s=raw_input('输入语句:\n')
        if s=='exit':
            break
        for x in word_set:
            if x in s:
                s=s.replace(x,'*'*len(x))
        print s

