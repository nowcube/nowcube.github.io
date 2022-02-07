#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os

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
        yield i
        # print(i)

if __name__ == '__main__':
    main()