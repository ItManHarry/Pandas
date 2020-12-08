import pandas as pd
import random as rd
data = [[rd.choice(['A','B','C','D']), rd.choice(['CLASS-1','CLASS-2','CLASS-3']), rd.randint(0, 100), i] for i in range(200)]
columns = ['Group', 'Class', 'Score' , 'Index']
df = pd.DataFrame(data=data, columns=columns)
print('Data is : \n', df)
df.to_excel('C:\\Users\\20112004\\Desktop\\tmp\\scores.xlsx')
print('Write source data to the Excel finished .')
#汇总函数
'''
    df.agg()
'''
#先进行分组
dg1 = df.groupby('Group')
#执行汇总

#导出数据
dg1.describe().to_excel('C:\\Users\\20112004\\Desktop\\tmp\\group1sum.xlsx')
#多重分组
dg2 = df.groupby(['Group','Class'])

#多重汇总

dg2.describe().to_excel('C:\\Users\\20112004\\Desktop\\tmp\\group2sum.xlsx')