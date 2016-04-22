#!/usr/bin/env python
#coding=utf-8

#头像右上角添加数字

from PIL import Image,ImageDraw,ImageFont

def add_num(picPath,num):
    img=Image.open(picPath)
    x,y=img.size
    myfont=ImageFont.truetype('/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf',x/3)
    draw=ImageDraw.Draw(img)
    draw.text((y/5*4,0),str(num),font=myfont,fill='red')
    img.save("ans.jpg")

if __name__=='__main__':
    add_num('pre.jpg',9)


