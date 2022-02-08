#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from cgitb import html
import os

#文件相对路径获取
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            if f.endswith('.md'):
                fullname = os.path.join(root, f)
                yield fullname
                # yield f

def main():
    base = '.'
    for i in findAllFile(base):
        # yield i
        if i=='.\\about.md':
            continue
        if i=='.\\index.md':
            continue
        if i=='.\\tags.md':
            continue
        # print(i)
        yield i

if __name__ == '__main__':
    main()