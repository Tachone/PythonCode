#!/usr/bin/env python
#coding=utf-8

word_set=set()
with open('filtered_words.txt','r') as f:
    for x in f.readlines():
        word_set.add(x.rstrip('\n'))
print word_set
while True:
    s=raw_input('输入词语:\n')
    if s=='exit':
        break
    elif s in word_set:
        print 'Freedom'
    else:
        print 'Human Rights'

