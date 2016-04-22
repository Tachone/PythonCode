#!/usr/bin/env python
#coding=utf-8

# 统计目录下文件的代码行数

import os

def walk_dir(path):
    file_path=[]
    for root,dirs,files in os.walk(path):
        for f in files:
            if f.lower().endswith('py'):
                file_path.append(os.path.join(root,f))

    return file_path

def count_codeline(path):
    file_name=os.path.basename(path)
    line_num=0
    empty_line_num=0
    note_num=0
    note_flag=False
    with open(path) as f:
        for line in f.readlines():
            line_num+=1
            if line.strip().startswith('\"\"\"') and not note_flag:
                note_num+=1
                note_flag=True
                continue
            if line.strip().startswith('\"\"\"'):
                note_flag=False
                note_num+=1
            if line.strip().startswith('#') or note_flag:
                note_num+=1

            if line.strip()=='':
                empty_line_num+=1

    print u"在%s中，共有%d行代码，其中有%d空行，有%d行注释" %(file_name,line_num,empty_line_num,note_num)

if __name__ =='__main__':
    for f in walk_dir('.'):
        count_codeline(f)


