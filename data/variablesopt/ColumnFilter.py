import pandas as pd
data = pd.DataFrame(data=[
    [1,2,3,4,5],
    [10,20,30,40,50],
    [100,200,300,400,500],
    [1000,2000,3000,4000,5000],
    [10000,20000,30000,40000,50000],
    [100000,200000,3000000,400000,500000]
],columns=['C01','C02','C03','C04','C05'])
print(data)
print('-' * 80)
#筛选变量列
print('第一列(Series) : \n', type(data['C01']),  data['C01'])
print('第一列(DataFrame) : \n', type(data[['C01']]),  data[['C01']])
#多列只能是DataFrame
print('第五一二列 : \n', data[['C05','C01','C02']])
#删除列
deleted = data.drop(columns=['C01','C03'])
print('After delete columns : \n', deleted)
print('Source data : \n', data)
#删除源数据列
data.drop(columns=['C02','C05'], inplace=True)
print('Now the data is : \n', data)
#删除行
deleted = data.drop(index=[2,4])
print('After deleted rows : \n', deleted)
print('Source data : \n', data)
data.drop(index=[2,4], inplace=True)
print('Now the data is : \n', data)
#使用del进行删除，该操作直接作用于源数据，慎用！！！
del data['C03']
print('Use del : \n', data)