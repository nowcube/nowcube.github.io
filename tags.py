#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# from importlib.resources import contents
import time #引入时间模块
import re #引入正则表达式模块
import os

#获取文件Tag
def get_FileTag(filePath):
    tag=os.path.basename(os.path.dirname(filePath))
    return tag
    # print(tag)

#获取文章标题
def get_FileTitle(filePath):
    fileName=os.path.basename(filePath).split('.')[0]
    return fileName
    # print(fileName)

#获取HTML文件的路径
def get_FileLink(filePath):
    return filePath.replace('.md','.html')

#获取MD文件路径
def get_FileMD(filePath):
    for root,dirs,files in os.walk(filePath):
        for f in files:
            if f.endswith('.md'):
                fullName=os.path.join(root,f)
                yield fullName

#创建tagItem
def create_tagItem(filePath):
    fileLink=get_FileLink(filePath)
    fileTitle=get_FileTitle(filePath)
    tagItem='''
        <div class="tag-item">
            <a href="{}">{}</a>
        </div>
    '''
    return tagItem.format(fileLink,fileTitle)
    # print(tagItem.format(fileLink,fileTitle))

#输出拥有MD文件的文件夹路径
def output_DirWithMD(filePath):
    listI=[]
    for i in get_FileMD(filePath):
        fileTitle=get_FileTitle(i)
        listI.append(i[0:-3].replace(fileTitle,''))
    for i in set(listI):
        yield i

#获取当前路径下的tag-item
def output_tagItemS(filePath):
    tagItemS=""
    for j in get_FileMD(filePath):#循环当前路径下的文件
        tagItemS=tagItemS+create_tagItem(j)
    return tagItemS


#获取完整的TagGroup
def get_tagGroupS(filePath):
    tagGroupS=""
    for i in output_DirWithMD(filePath):
        tagGroup='''
        <div class="tag-group">
            <p id="#{}" class="tag-title">「 {} 」</p>
                {}
        </div>
        '''
        tagTitle=i.replace(".",'').replace("/",'').replace("\\",'')
        tagItemS=output_tagItemS(i)
        tagGroup=tagGroup.format(tagTitle,tagTitle,tagItemS)
        # print("***")
        # print(tagGroup)
        tagGroupS=tagGroupS+tagGroup
    return tagGroupS

file = open( "tags.html", "r", encoding="utf-8" )
content = file.read()
part='''

<!doctype html>
<html>

<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width initial-scale=1'>
    <title>MoedayNano</title>
    <link rel="stylesheet" href="./tags.css">
</head>

<body>
    <div class="nav-area"><a href="./index.html">MoedayNano</a><a href="./tags.html">Tags</a><a
            href="./about.html">About</a>
    </div>

    {}
    
</body>

</html>

'''
filePath="."
content=part.format(get_tagGroupS(filePath))

file = open("tags.html",'w', encoding="utf-8" )
file.write(content)
file.close()