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
#基本信息
print('Data information \n: ', data.info())
print('-' * 80)
#浏览前几条
print('Top 3 data : \n', data.head(3))
print('-' * 80)
#浏览后几条数据
print('Last 3 data : \n', data.tail(3))
print('-' * 80)
#输出列名
print('Columns are : \n', data.columns)
print('-' * 80)
#更换列名 - 全部更换
data.columns = ['列1','列2','列3','列4','列5']
print(data)
print('-' * 80)
#只更改某几个列名
'''
    df.rename(
        columns={'旧名称':'新名称',...},   #对应更改列名字典参数
        inplace=False                    #是否直接修改原数据，默认为False
    )
'''
#不修改源数据
new_data = data.rename(columns={'列2':'Column2','列5':'Column5'})
print('New Data : \n', new_data)
print('Old Data : \n', data)
print('-' * 80)
#修改源数据
data.rename(columns={'列2':'Column-2','列3':'Column-3'}, inplace=True)
print('Now data is : \n', data)
print('-' * 80)
