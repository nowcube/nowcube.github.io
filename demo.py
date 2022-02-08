import os
filePath="."
def output_FileByTime(filePath):
    dictTime={}
    for root, dirs, files in os.walk(filePath):
        for f in files:
            if f.endswith('.md'):
                fileDir=os.path.join(root, f)
                dictTime['{}'.format(fileDir)]=os.path.getmtime(fileDir)
    listTime = sorted(dictTime.items(), key=lambda kv: kv[1], reverse=True)
    for i in range(len(listTime)):
        print(listTime[i][0])

output_FileByTime(filePath)