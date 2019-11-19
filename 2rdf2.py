from entity2 import *
#from extrct2txt import *
import pandas as pd
import openpyxl as op
import re
import os

if __name__ == "__main__":

    #extract2txt(1)
    
    print('ok')

    path='C:\\Users\\piguai\\Desktop\\设备信息采集总表(1)(1).xlsx'

    wb = op.load_workbook(path)

    #获取workbook中所有的表格
    sheets = wb.sheetnames
    print(sheets)
    sheet_hadle=[]
    sheet_hadle.append(sheets[0])
    print(sheet_hadle)

    for item in sheets:
        data=pd.read_excel(path,sheet_name=item,index_col=0)

        #每列数据
        for headName in list(data):
            if headName=='生产厂家（制造商）名称':
                continue
            #每行数据
            for index,row in data.iterrows():
                if str(row[headName]).strip().replace(' ','').replace('\n','')!='nan':
                    headName_p=headName
                    if '（' in headName:
                        headName=headName[:4]+headName[5:8]+headName[9:]

                    # #设备类
                    # class3=eval(item)
                    # device=class3(item+str(index))

                    # #对象属性类(具体数据类)
                    # class1=eval(headName)#字符串转类方法
                    # #单元格数据str(row[headName_p])
                    # ind=class1(str(row[headName_p]).strip().replace(' ','').replace('\n',''))

                    # #边属性类
                    # o='有'+headName
                    # s=headName+'类型'
                    # # print(o)
                    # # print(s)

                    # #数据类型类
                    # ind.s=[str(row[headName_p]).strip().replace(' ','').replace('\n','')]

                    # device.method1=[ind]

                    #设备类
                    device=onto[item](item+str(index))
                    #实体类
                    ind=onto[headName](str(row[headName_p]).strip().replace(' ','').replace('\n',''))
                    #关系类
                    p=onto['有'+headName].name
                    #数据类型类
                    t=onto[headName+'类型'].name
                    #定义关系
                    ##对象属性
                    exec('device.%s.append(ind)'%p)
                    na=str(row[headName_p]).strip().replace(' ','').replace('\n','')
                    ##数据类型属性
                    exec('ind.%s.append(na)'%t)


    # dtu=DTU('dtu')
    # na=设备名称('jauu')
    # na.设备名称类型=['jauu']
    # dtu.有设备名称=[na]


    
    #onto.save(file='device_onto5.nt',format='ntriples')
    onto.save(file='device_onto5.rdf',format='rdfxml')
    #转换格式为utf-8
    # with open('device_onto3.nt') as f1:
    #     s='device_onto2.nt'
    #     with open('a.txt','w',encoding='UTF-8') as f2:
    #         f2.write(f1.read())
    # os.remove(s)
    # os.rename('a.txt',s)


