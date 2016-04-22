#!/usr/bin/env python
#coding=utf-8

#改变图片分辨率

from PIL import Image
import glob

def get_list():
    return glob.glob('*.jpg')

def image_resize(imagename,number):
    im=Image.open(imagename)
    imrez=im.resize((1136,640))
    number=str(number)
    #save函数 路径+函数
    imrez.save('./'+number+'.jpg','jpeg')

def solve():
    imagelist=get_list()
    n=1
    for name in imagelist:
        image_resize(name,n)
        n+=1

if __name__=='__main__':
    solve()
