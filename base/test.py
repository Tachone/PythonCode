#!/usr/bin/env python
#coding=utf-8
import math

#默认参数的使用
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny

def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
def func(a,b,c=0,*args,**kw):
    print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw

def fib(max):
    n,a,b=0,0,1
    while(n<max):
        yield b
        a,b=b,a+b
        n=n+1

def normalize(s):
    return s[0].upper()+s[1:].lower()

def prod(a):
    def calc(a,b):
        return a*b
    return reduce(calc,a)

def cmp_ignore_case(s1,s2):
    u1=s1.upper()
    u2=s2.upper()
    if u1<u2:
        return -1
    if u1>u2:
        return 1
    return 0

def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

names=['tach','lotile','jett']
temp=raw_input()
if temp in names:
    x,y=move(100,100,60,math.pi/6)
    print x,y
    print power(5,n=2)
    func(1,2,3,'a','b',x=99)
    args=(1,2,3,4);
    kw={'x':99}
    func(1,2,3,*args,**kw)
    d={'a':1,'b':2,'c':3}
    for key,value in d.items():
        print '%s:%s' %(key,value)
    for key,value in enumerate(names):
        print key,value
    for k,v in d.iteritems():
            print k,'=',v

    LL=['Hello','World',15,'Apple']
    LL=[s.lower() for s in LL if isinstance(s,str)]
    print LL
    for n in fib(5):
        print n
    print '我是华丽的分割线:\n'

    print map(normalize,['adam','LISA','barT'])
    print prod([1,2,3,4,5])
    print sorted(['bob','about','Zoo','Credit'],cmp_ignore_case)

    print 'lambda'
    print map(lambda x:x*x,[1,2,3,4])






