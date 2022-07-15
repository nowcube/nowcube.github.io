#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import time
import re #引入正则表达式模块


#转化时间戳
def TimeStampToTime(timestamp):
    timeStruct=time.localtime(timestamp)
    return time.strftime('%Y-%m-%d',timeStruct)

#获取文件修改时间
def get_FileModifyTime(filePath):
    # filePath = unicode(filePath,'utf8')
    t=os.path.getmtime(filePath)
    # return TimeStampToTime(t)
    return TimeStampToTime(t)
    # print(TimeStampToTime(t)) 

#获取文件修改时间戳
def get_FileModifyTimeStamp(filePath):
    # return os.path.getmtime(filePath)
    # print(os.path.getmtime(filePath))
    yield os.path.getmtime(filePath)

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

#文章摘取
def get_FileExtract(filePath):
    os.system("pandoc {} -o {}Temp.html".format(filePath,filePath.replace('.md','')))
    file = open( "{}".format(filePath.replace('.md','Temp.html')), "r", encoding="utf-8" )
    content = file.read()
    file.close()
    extract=re.compile(r'<[^>]+>',re.S).sub('',content)
    # print(extract.replace('\n','')[0:100])
    os.remove("{}Temp.html".format(filePath.replace('.md','')))
    return extract.replace('\n','')[0:100]

#获取文件字数
def get_FileNumbers(filePath):
    os.system("pandoc {} -o {}Temp.html".format(filePath,filePath.replace('.md','')))
    file = open( "{}".format(filePath.replace('.md','Temp.html')), "r", encoding="utf-8" )
    content = file.read()
    file.close()
    extract=re.compile(r'<[^>]+>',re.S).sub('',content)
    # print(len(extract.replace('\n','')))
    os.remove("{}Temp.html".format(filePath.replace('.md','')))
    return len(extract.replace('\n',''))

#文件相对路径获取
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            if f.endswith('.md'):
                fullname = os.path.join(root, f)
                yield fullname
                # print(fullname)


#获取HTML文件的路径
def get_FileLink(filePath):
    return filePath.replace('.md','.html')

#创建每一篇文章的卡片
def createPostLine(filePath):
    fileLink=get_FileLink(filePath)
    fileTitle=get_FileTitle(filePath)
    fileExtract=get_FileExtract(filePath)
    fileTag=get_FileTag(filePath)
    fileNumbers=get_FileNumbers(filePath)
    fileModifyTime=get_FileModifyTime(filePath)
    postLine="<li class=\"post-line\"><a class=\"post-title\" href=\"{}\">{}</a><a href=\"{}\"><div class=\"post-summary\">{}</div></a><div class=\"post-info\"><div class=\"category-left\"><a href=\"./tags.html#{}\">{}</a></div><div class=\"category-right\">字数{} 日期{}</div></div><hr></li>".format(fileLink,fileTitle,fileLink,fileExtract,fileTag,fileTag,fileNumbers,fileModifyTime)
    # print(postLine)
    return postLine

#按照文件修改时间从大到小输出
def output_FileByTime(filePath):
    dictTime={}
    for root, dirs, files in os.walk(filePath):
        for f in files:
            if f.endswith('.md'):
                fileDir=os.path.join(root, f)
                dictTime['{}'.format(fileDir)]=os.path.getmtime(fileDir)
    listTime = sorted(dictTime.items(), key=lambda kv: kv[1], reverse=True)
    for i in range(len(listTime)):
        yield (listTime[i][0])

#统计所有文章个数
def count_AllFileNums(filePath):
    fileNums=0
    for i in output_FileByTime(filePath):
        fileNums=fileNums+1
    # print(fileNums)
    return(fileNums)

#统计所有文章文字数
def count_AllFileChars(filePath):
    fileChars=0
    for i in output_FileByTime(filePath):
        fileChars=fileChars+get_FileNumbers(i)
    # print(fileChars)
    return(fileChars)

# filePath="."
# postLineS=""
# for i in output_FileByTime(filePath):
#     postLineS=postLineS+createPostLine(i)#postLineS为所有渲染的post加在一起
# file = open( "index.html", "r", encoding="utf-8" )
# content = file.read()
# post = content.find("<ul>")
# postEnd = content.find("</ul>")
# if post != -1:
#     content=content[:post+len("<ul>")]+content[postEnd:]#删除原本的<ul></ul>里的内容
#     content = content[:post+len("<ul>")]+postLineS+content[post+len("<ul>"):]#加入postLineS
#     file = open("index.html",'w', encoding="utf-8" )
#     file.write(content)
# file.close()

filePath="."
postLineS=""
for i in output_FileByTime(filePath):
    postLineS=postLineS+createPostLine(i)#postLineS为所有渲染的post加在一起
allFileNums=count_AllFileNums(filePath)
allFileChars=count_AllFileChars(filePath)
file = open( "index.html", "r", encoding="utf-8" )
content = file.read()
part='''
<!doctype html>
<html>

<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width initial-scale=1'>
    <title>MoedayNano</title>
    <link rel="stylesheet" href="index.css">
</head>

<body>
    <div class="nav-area"><a href="./index.html">🏠MoedayNano</a><a href="./tags.html">📑Tags</a><a
            href="./about.html">🐱About</a><a href="./MoEditor.html">✍🏻️MoEditor</a>
    </div>
    <div class="slogan" style="color:#5C89A4;">让爱伴随永生</div>
    <div class="char-total-counter">{}篇文章 {}字</div>
    <ul>
        
        {}

    </ul>
</body>

</html>
'''
content=part.format(allFileNums,allFileChars,postLineS)

file = open("index.html",'w', encoding="utf-8" )
file.write(content)
file.close()
