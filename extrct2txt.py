import pandas as pd
import openpyxl as op

def extract2txt(flag):
    if flag:
        path='C:\\Users\\piguai\\Desktop\\设备信息采集总表(1)(1).xlsx'

        wb = op.load_workbook(path)

        #获取workbook中所有的表格
        sheets = wb.sheetnames
        print(sheets)
        sheet_hadle=[]
        sheet_hadle.append(sheets[0])
        print(sheet_hadle)

        with open('extract.txt','w') as f:

                for item in sheet_hadle:
                    data=pd.read_excel(path,sheet_name=item,index_col=0)

                    print(list(data))

                    #每列数据
                    for headName in list(data):
                        if headName=='生产厂家（制造商）名称':
                            continue
                        print(headName)
                        #每行
                        for index,row in data.iterrows():
                            f.write(str(row[headName])+'\n')
    return