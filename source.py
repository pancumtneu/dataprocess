import re
import pandas as pd





def deal(datalist=None):
    # 列表
    if datalist==None:
        datalist=[]


    num=['231.81', '241.23', '251.05', '259.26', '274.21', '280.75', '284.62', '290.05', '290.22', '292.22', '295.53', '300.09', '301.14', '306.15', '307.53', '310.25', '313.5', '310.51', '306.46', '305.94', '300.51', '300.21', '279.36', '279.72', '275.31', '260.48', '245.12', '243.68', '235.25', '229.04', '205.24', '202.8', '196.23', '177.59', '164.12', '159.91', '155.23', '157.57', '145.99', '141.11', '143.24', '131.93', '133.53', '130.69', '130.88', '135.8', '131.43', '122.22', '115.22', '113.53', '115.35', '112.23', '107.2', '117.21', '130.66', '136.36', '137.56', '135.99', '143.98', '136.3', '130.84', '123.38', '118.46', '117.1', '107.97', '107.8', '111.43', '107.14', '104.77', '105.38', '111.63', '105.38', '104.47', '98.27', '101.12', '109.17', '115.55', '114.46', '115.95', '113.47', '107.35', '87.31', '80.6', '87.79', '95.62', '94.08', '87.89', '74.22', '68.39', '59.8', '61.56', '60.85', '53.47', '59.9', '46.5', '16.5', '16.65', '28.11', '42.38', '45.62', '41.73']
    b=[float(i) for i in datalist ]
    # list转dataframe
    print(b)
    num2=[231.81, 241.23, 251.05, 259.26, 274.21, 280.75, 284.62, 290.05, 290.22, 292.22, 295.53, 300.09, 301.14, 306.15, 307.53, 310.25, 313.5, 310.51, 306.46, 305.94, 300.51, 300.21, 279.36, 279.72, 275.31, 260.48, 245.12, 243.68, 235.25, 229.04, 205.24, 202.8, 196.23, 177.59, 164.12, 159.91, 155.23, 157.57, 145.99, 141.11, 143.24, 131.93, 133.53, 130.69, 130.88, 135.8, 131.43, 122.22, 115.22, 113.53, 115.35, 112.23, 107.2, 117.21, 130.66, 136.36, 137.56, 135.99, 143.98, 136.3, 130.84, 123.38, 118.46, 117.1, 107.97, 107.8, 111.43, 107.14, 104.77, 105.38, 111.63, 105.38, 104.47, 98.27, 101.12, 109.17, 115.55, 114.46, 115.95, 113.47, 107.35, 87.31, 80.6, 87.79, 95.62, 94.08, 87.89, 74.22, 68.39, 59.8, 61.56, 60.85, 53.47, 59.9, 46.5, 16.5, 16.65, 28.11, 42.38, 45.62, 41.73]
    df = pd.DataFrame(num2, columns=['company_name'])

    writer = pd.ExcelWriter('test1.xlsx')
    # 保存到本地excel
    df.to_excel(writer, index=False)
    writer.save()







string ="xxxxxxxxxxxxxxxxxxxxxxxx entry '某某内容' for aaaaaaaaaaaaaaaaaa"
str="L10.55,231.81L15.82,241.23L21.09,251.05L26.36,259.26L36.91,274.21"
long="L10.55,231.81L15.82,241.23L21.09,251.05L26.36,259.26L36.91,274.21L42.18,280.75L47.45,284.62L52.73,290.05L58,290.22L63.27,292.22L68.55,295.53L73.82,300.09L79.09,301.14L84.36,306.15L89.64,307.53L94.91,310.25L105.45,313.5L110.73,310.51L121.27,306.46L126.55,305.94L131.82,300.51L137.09,300.21L147.64,279.36L152.91,279.72L158.18,275.31L163.45,260.48L168.73,245.12L174,243.68L179.27,235.25L184.55,229.04L195.09,205.24L200.36,202.8L205.64,196.23L210.91,177.59L216.18,164.12L221.45,159.91L226.73,155.23L232,157.57L237.27,145.99L242.55,141.11L253.09,143.24L258.36,131.93L263.64,133.53L268.91,130.69L274.18,130.88L279.45,135.8L284.73,131.43L290,122.22L295.27,115.22L300.55,113.53L305.82,115.35L311.09,112.23L316.36,107.2L321.64,117.21L326.91,130.66L332.18,136.36L337.45,137.56L342.73,135.99L348,143.98L353.27,136.3L358.55,130.84L363.82,123.38L369.09,118.46L374.36,117.1L379.64,107.97L384.91,107.8L390.18,111.43L395.45,107.14L400.73,104.77L406,105.38L411.27,111.63L416.55,105.38L421.82,104.47L427.09,98.27L437.64,101.12L442.91,109.17L448.18,115.55L453.45,114.46L458.73,115.95L464,113.47L469.27,107.35L474.55,87.31L479.82,80.6L485.09,87.79L490.36,95.62L495.64,94.08L500.91,87.89L506.18,74.22L511.45,68.39L516.73,59.8L522,61.56L527.27,60.85L532.55,53.47L537.82,59.9L543.09,46.5L548.36,16.5L553.64,16.65L558.91,28.11L564.18,42.38L569.45,45.62L574.73,41.73L580,43.61"
result =re.findall("(?<=L).*?(?=,)",long)   #包含和不包含

for x in result:

    print (x+"\t")

###############读取一列数据  处理好的####################
df = pd.read_excel("test1.xlsx")

aa = list(df.iloc[:, 0].values)
########################################################
arr = list(map(int,result))
wanzheng = []
for i in range(0, len(result)):
    # print(list1[i]+list2[i])
    wanzheng.append(arr[i] +aa[i])
print("输出结果为"+wanzheng)  # 输出结果  ['1.1', '2.2']




print ("*"*10)
resulty =re.findall("(?<=,).*?(?=L)",long)   #包含和不包含
deal(datalist=resulty)


for y in resulty:

    print (y+"\t")


deal()
# def loadDatadet(infile):
#     f=open(infile,'r')
#     sourceInLine=f.readlines()
#     dataset=[]
#     raw=[]
#     for line in sourceInLine:
#         temp1=line.strip('\n')
#         temp2=temp1.split(',')
#         dataset.append(temp2)
#         regex = r'L([\s\S]*),'
#         matches = re.findall(regex, str)
#         raw.append(matches)
#     return raw
# infile='comma.txt'
# infile=loadDatadet(infile)
# print('dataset=',infile)
