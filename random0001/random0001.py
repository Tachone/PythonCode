#!/usr/bin/env python
#coding=utf-8

#生成序列号
import random,string

def ran_str(num,len=7):
    fd=open('ans.txt','wb')
    chars=string.letters+string.digits
    for i in range(num):
        s=[]
        for j in range(len):
            s.append((random.choice(chars)))
        fd.write(''.join(s)+\n')
    fd.close()

if __name__=='__main__':
    ran_str(200)

