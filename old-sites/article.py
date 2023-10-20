#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from importlib.resources import contents
import time #引入时间模块
import re #引入正则表达式模块
import os #引入OS模块

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
        # print (listTime[i][0])

# 从Markdown生成基本HTML文档,并返回HTML文档路径
def output_BasicHtml(filePath):
    for i in output_FileByTime(filePath):
        fileLink=get_FileLink(i)
        # print(i)
        os.system("pandoc {} -o {}".format(i,fileLink))
        yield fileLink

#开始进行文件写入
filePath="."
for i in output_BasicHtml(filePath):
    # print(i)
    fileTitle=get_FileTitle(i)
    fileTag=get_FileTag(i)
    fileNumber=get_FileNumbers(i)
    fileModifyTime=get_FileModifyTime(i.replace("html", "md"))
    # print(fileTitle,fileTag,fileNumber,fileModifyTime)
    file = open( "{}".format(i), "r", encoding="utf-8" )
    content=file.read()
    articlePart='''
<!doctype html>
<html>

<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width initial-scale=1'>
    <title>{}</title>
    <link rel="stylesheet" href="../article.css">
</head>

<body>
    <header class="header">
        <div class="navbar mica no-border no-shadow">
            <div class="hamburger">
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
            <div class="link-group">
                <a class="link-item" href="../index.html">Home</a>
                <a class="link-item" href="../tags.html">Tags</a>
                <a class="link-item" href="../about.html">About</a>
                <a class="link-item" href="../MoEditor.html">MoEditor</a>
            </div>
        </div>
    </header>

    <div class="content">
        <p class="title">{}</p>
        <p class="tag"><a href="../tags.html#{}">「 {} 」</a></p>
        <p class="char-counter">字数{}</p>
        {}
    </div>
    <script src="../navbar.js"></script>
</body>

</html>
'''
    content=articlePart.format(fileTitle,fileTitle,fileTag,fileTag,fileNumber,content)
    # print(content)
    file = open( "{}".format(i), "w", encoding="utf-8" )
    file.write(content)
    file.close()





