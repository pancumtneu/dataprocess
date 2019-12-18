import re
import pandas as pd
import math
"""输入一个字符串"""
def loadDatadet(infile):
    f=open(infile,'r',encoding='utf-8')
    sourceInLine=f.readlines()
    dataset=[]
    for line in sourceInLine:
        temp1=line.strip('\n')
        temp2=temp1.split('\t')
        dataset.append(temp2)

    f.close()
    #return dataset
    for j in sourceInLine:

        return j
infile='1000.svg'
raw=loadDatadet(infile)




def loadpoutter(outfile):
    f=open(outfile,'r',encoding='utf-8')
    sourceInLine=f.readlines()
    dataset=[]
    for line in sourceInLine:
        temp1=line.strip('\n')
        temp2=temp1.split('\t')
        dataset.append(temp2)

    f.close()
    #return dataset
    for j in sourceInLine:

        return j











##############提取字符串x###############

resultx =re.findall("(?<=<path class=\"js-line\" d=\"M0,206.88).*?(?=\" style=\"vector-effect:)",raw)   #包含和不包含          L到，之间  左边


"""返回到文件中"""



###############把字符写入文件###########################
def savetoinput(data):
    outfile=open("outter.html",'w',encoding='utf-8')
    # for i in range(len(data)):
    #     s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
    #     s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
    outfile.write(data)


inputnum="".join(resultx)
print ("内容",inputnum)
#savetoinput(inputnum)


start=raw.split("<path class=\"js-line\" d=\"M0,206.88")
end=raw.split("\" style=\"vector-effect:")
# ddd="Peoples repub of"
# end =ddd.split("re")
#print(end)
#print (start[0])
#loadpoutter("ouput.txt")
all=start[0]+"<path class=\"js-line\" d=\"M0,206.88"+"".join(loadpoutter("ouput.txt"))+"\" style=\"vector-effect:"+end[1]


savetoinput(all)