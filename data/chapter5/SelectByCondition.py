import pandas as pd
import random as rd
#创建数据
data = [['N%s' %i,'jack%s@163.com' %i, rd.randint(20, 45), '1%s%s%s%s' %(rd.choice([3,5]), rd.randint(0,9), rd.randint(1000,9999), rd.randint(1000,9999)), rd.choice(['F','M']), rd.choice(['山东','河南','山西','河北','湖南','湖北','北京','上海','广州'])] for i in range(5000)]
columns = ['职号','邮箱','年龄','手机号','性别','地区']
#print(data)
df = pd.DataFrame(data=data,columns=columns)
print('Data : \n', df)
sl = [True, False, True, True]
print('0 - 10 records : \n', df.iloc[0:10])                         #取某个范围内的数据不包括右侧边界
print('0,3,5,7 records : \n', df.iloc[[0,3,5,7]])                   #取具体的某几条数据
print('0 - 10 rows, 1 - 3 columns : \n', df.iloc[0:11,1:4])         #取某几列、某几行数据(范围别)
print('0 , 11 rows, 1 , 4 columns : \n', df.iloc[[0,11],[1,4]])     #取某几列、某几行数据(指定哪行哪列)