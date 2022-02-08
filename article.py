#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time #引入时间模块
import re #引入正则表达式模块
import os #引入OS模块
import all_md #引入自定义查找.md结尾的文件
mdDirs=all_md.main()
for mdDir in mdDirs:
    print(mdDir)
    noMd=mdDir.replace('.md','')
    file_path = "{}".format(mdDir)
    basename = os.path.basename(file_path)
    file_name = os.path.splitext(basename)[0]
    # print(noMd)
    os.system("pandoc {} -o {}.html".format(mdDir,noMd))
    file = open( "{}.html".format(noMd), "r", encoding="utf-8" )
    # print("{}.html".format(noMd))
    content = file.read()
    # print(content)
    file.close()
    strHtmlPart1 = "<!doctype html><html><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width initial-scale=1'><title>{}</title></head><body>".format(file_name)
    strHtmlPart2 = '</body></html>'
    content = strHtmlPart1+content+strHtmlPart2#让pandoc生成的网页有完整的格式
    # print(content)
    post1 = content.find( "<body>" )
    str1 = "<div class=\"nav-area\"><a href=\"../index.html\">MoedayNano</a><a href=\"../tags.html\">Tags</a><a href=\"../about.html\">About</a></div>"
    post2 = content.find( "</title>" )
    str2 = "<link rel=\"stylesheet\" href=\"article.css\">"
    postTitleStrat=content.find("<title>")
    postTitleEnd=content.find("</title>")
    title=content[postTitleStrat+len("<title>"):postTitleEnd]#从html文档中获取<title></title>中的内容
    if post1 != -1: #插入nav元素
        content = content[:post1+len("<body>")] + str1 + content[post1+len("<body>"):]
        file=open("{}.html".format(noMd),"w", encoding="utf-8" )
        file.write( content )
        file.close()
    if post2 != -1: #插入link:css标签
        content = content[:post2+len("</title>")] + str2 + content[post2+len("</title>"):]
        file=open("{}.html".format(noMd),"w", encoding="utf-8" )
        file.write( content )
        file.close()

    # print(len(content))
    strContent="".join(content.replace('\n',''))#.replace实现换行符替换为''，注：本身content也为str类型
    contentLable = re.findall("<.*?>",content)#获取所有的<*>
    strContentLable="".join(contentLable)#成为一个str
    count=len(strContent)-len(strContentLable)#去掉换行符的内容 - 所有的<*> = 实际的字数
    # print(contentLable)

    post3 = content.find(str1)
    dirName=noMd.replace('.\\','').replace('\{}'.format(title),'')
    str3 = "<p class=\"title\">{}</p><p class=\"tag\"><a href=\"../tags.html#{}\">「 {} 」</a></p><p class=\"char-counter\">字数:{}</p>".format(title, dirName, dirName,count)
    if post3 != -1:  #插入文章title，Tag，字数统计
        content = content[:post3+len(str1)] + str3 + content[post3+len(str1):]
        file=open("{}.html".format(noMd),"w", encoding="utf-8" )
        file.write( content )
        file.close()
