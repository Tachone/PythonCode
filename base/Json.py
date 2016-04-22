#!/usr/bin/env python
#coding=utf-8

#json反序列化成对象
import json

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

'''def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }'''

class Teacher(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

s=Student('Bob',20,88)
p=Teacher('Tach',20)
print(json.dumps(s,default=lambda obj:obj.__dict__))
print(json.dumps(p,default=lambda obj:obj.__dict__))

class Target(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
def dict2Target(d):
    return Target(d['name'],d['age'],d['score'])
json_str='{"age":20,"score":88,"name":"Bob"}'
print(json.loads(json_str,object_hook=dict2Target))

