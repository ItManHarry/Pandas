import pandas as pd
import random as rd
#创建数据
data = [['N%s' %i,'jack%s@163.com' %i, rd.randint(20, 45), '1%s%s%s%s' %(rd.choice([3,5]), rd.randint(0,9), rd.randint(1000,9999), rd.randint(1000,9999)), rd.choice(['F','M']), rd.choice(['山东','河南','山西','河北','湖南','湖北','北京','上海','广州'])] for i in range(5000)]
columns = ['职号','邮箱','年龄','手机号','性别','地区']
#print(data)
df = pd.DataFrame(data=data,columns=columns)
df.set_index(['地区','手机号'], inplace = True)
print('Data : \n', df)
#年龄范围筛选
print('Person whose age above 30 : \n',df[df.年龄 > 30])
#列表筛选
ages = [23,25,30,35,40]
print('Person whose age in (23,25,30,35,40) : \n', df[df.年龄.isin(ages)])
#将索引恢复为列
df.reset_index(['地区','手机号'],inplace=True)
#只设置地区为索引列
df.set_index('地区', inplace=True)
print('Person live in 山东 and 山西 : \n', df[df.index.isin(['山东','山西'])])
#多重条件联合查询
print('Person age between 25 and 35', df[(df.年龄 > 25) & (df.年龄 < 35)])