import re
import pandas as pd
import math
savetoxl="False"

#使用方法，直接把svg文件放在目录中，直接运行生成，注意123行M开头的是数据头，不同的svg不同 在，这是起始点的坐标
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


"""对数据处理"""
def applytonum(xraw=None,yraw=None):
    #xs = list(range(1, 100))测试数组    print(applytonum(xs))
    if xraw==None:
        xraw=[]



    #recv = list(map(float, xraw))
    recv=xraw

    # print("________________合并值______________")
    # print(recv)
    # print("________________合并值______________")
    #print ("recv is ",recv)
    pos=recv[0]+(recv[-1]-recv[0])*0.590   #超过55%后 曲线上升

    func = lambda x, pos: 0.5*x+20*math.cos(x)+30*math.sin(x)-20*math.cos(x)-50 if x < pos else -0.2*x+20*math.sin(x)+30*math.cos(x)
    #func = lambda x, pos: 100 if x > pos else 0
    res = [func(float(t),pos) for t in recv]
    #print ("变换的大小",res)
    # print("________________变换后V______________")
    # print(res)
    # print("________________变换后A______________")
    #res = [math.pow((float(t) * 0.05),2)  for t in xraw]
    #res = [math.exp(float(t)*0.05) + 100 for t in xraw]
    #res = [5.0*math.log(float(t))+100 for t in xraw]
    #res = [80.0*math.sin(float(t)) for t in xraw]
    #math.log(x[, base])  返回值
#    add= [2 for x in range(len(xraw))]   所有的数都是2   加到y中


    if yraw == None:
        yraw=[]
        return res

    else:
        #print("横坐标",type(yraw[1]))
        #print("纵坐标",type(res[1]))
        c = list(map(lambda x: x[0] + x[1], zip(yraw, res)))
        # print("________________处理后的值______________")
        # print(c)
        # print("________________处理后的值______________")
        return c


def savetoinput(data):
    outfile=open("outter.html",'w',encoding='utf-8')
    # for i in range(len(data)):
    #     s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
    #     s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
    outfile.write(data)


infile="1000.svg"
filecontent=loadDatadet(infile)
start=filecontent.split("<path class=\"js-line\" d=\"M0,206.88")
end=filecontent.split("\" style=\"vector-effect:")

positions=re.findall("(?<=<path class=\"js-line\" d=\"M0,206.88).*?(?=\" style=\"vector-effect:)",filecontent)
raw="".join(positions)
rawx=start[1]
rawy=end[0]
#print (raw)
# long="L10.55,231.81L15.82,241.23L21.09,251.05L26.36,259.26L36.91,274.21L42.18,280.75L47.45,284.62L52.73,290.05L58,290.22L63.27,292.22L68.55,295.53L73.82,300.09L79.09,301.14L84.36,306.15L89.64,307.53L94.91,310.25L105.45,313.5L110.73,310.51L121.27,306.46L126.55,305.94L131.82,300.51L137.09,300.21L147.64,279.36L152.91,279.72L158.18,275.31L163.45,260.48L168.73,245.12L174,243.68L179.27,235.25L184.55,229.04L195.09,205.24L200.36,202.8L205.64,196.23L210.91,177.59L216.18,164.12L221.45,159.91L226.73,155.23L232,157.57L237.27,145.99L242.55,141.11L253.09,143.24L258.36,131.93L263.64,133.53L268.91,130.69L274.18,130.88L279.45,135.8L284.73,131.43L290,122.22L295.27,115.22L300.55,113.53L305.82,115.35L311.09,112.23L316.36,107.2L321.64,117.21L326.91,130.66L332.18,136.36L337.45,137.56L342.73,135.99L348,143.98L353.27,136.3L358.55,130.84L363.82,123.38L369.09,118.46L374.36,117.1L379.64,107.97L384.91,107.8L390.18,111.43L395.45,107.14L400.73,104.77L406,105.38L411.27,111.63L416.55,105.38L421.82,104.47L427.09,98.27L437.64,101.12L442.91,109.17L448.18,115.55L453.45,114.46L458.73,115.95L464,113.47L469.27,107.35L474.55,87.31L479.82,80.6L485.09,87.79L490.36,95.62L495.64,94.08L500.91,87.89L506.18,74.22L511.45,68.39L516.73,59.8L522,61.56L527.27,60.85L532.55,53.47L537.82,59.9L543.09,46.5L548.36,16.5L553.64,16.65L558.91,28.11L564.18,42.38L569.45,45.62L574.73,41.73L580,43.61"

#print ("raw number is ",type(raw))
resultx =re.findall("(?<=L).*?(?=,)",raw)   #横坐标str
resulty =re.findall("(?<=,).*?(?=L)",raw)   #对应的纵坐标
# print ("resultx",resultx)
# print ("resulty",resulty)
#print ("*"*100)

xraw=list(map(float, resultx))
yraw=list(map(float, resulty))
# print ("resultx",xraw)
# print ("resulty",yraw)
afterprocess=applytonum(xraw,yraw) #将x和y分别处理


aftertrx=list(map(str, resultx))  #转换为字符
aftertry=list(map(str, afterprocess))  #y转换为字符



afterposi = []
indexrange=min(len(resultx),len(resulty))
for i in range(0, indexrange):
    # print(list1[i]+list2[i])
    afterposi.append("L"+aftertrx[i] +"," +aftertry[i])  #拼接

# print(wanzheng)  # 输出结果  ['1.1', '2.2']


s = "".join(afterposi)
#print ("处理后的坐标",s,"类型为",type(s))

# start=raw.split("<path class=\"js-line\" d=\"M0,206.88")
# end=raw.split("\" style=\"vector-effect:")



all=start[0]+"<path class=\"js-line\" d=\"M0,206.88"+s+"\" style=\"vector-effect:"+end[1]

linetag="<path class=\"js-line\" d=\"M0,206.88"+s+"\" style=\"vector-effect: non-scaling-stroke; fill: none; stroke: rgb(31, 119, 180); stroke-opacity: 1; stroke-width: 2px; opacity: 1;\"/>"
print ("曲线坐标群",linetag)
savetoinput(all)