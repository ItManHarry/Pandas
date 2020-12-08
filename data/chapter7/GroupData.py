import pandas as pd
import random as rd
data = [[rd.choice(['A','B','C','D']), rd.choice(['CLASS-1','CLASS-2','CLASS-3']), rd.randint(0, 100), i] for i in range(200)]
columns = ['Group', 'Class', 'Score' , 'Index']
df = pd.DataFrame(data=data, columns=columns)
print('Data is : \n', df)
df.to_excel('C:\\Users\\20112004\\Desktop\\tmp\\scores.xlsx')
print('Write to the Excel finished ...')
#分组
'''
    df.groupby(
        by :                #用于分组的变量名/函数
        axis = 0 :
        level = None :      #相应的轴存在多重索引时，指定用于分组的级别
        as_index = True :   #在结果中将组标签作为索引
        sort = True :       #结果是否按照分组关键字进行排序 
        dropna = True :     #是否将NA看作普通键值用于分组
    )
'''
dg1 = df.groupby('Group')
#分组结果（值为字典，key为列值，value为索引list）
print('Group data 1 column : \n', dg1.groups)
#分组结果描述
print('Group describe 1 column : \n', dg1.describe())
dg1.describe().to_excel('C:\\Users\\20112004\\Desktop\\tmp\\group1columns.xlsx')
dg2 = df.groupby(['Group','Class'])
print('Group data 2 columns : \n', dg2.groups)
print('Group describe 2 columns : \n', dg2.describe())
dg2.describe().to_excel('C:\\Users\\20112004\\Desktop\\tmp\\group2columns.xlsx')