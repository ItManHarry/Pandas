import pandas as pd
import random as rd
#创建数据
data = [['N%s' %i,'jack%s@163.com' %i, rd.randint(20, 45), '1%s%s%s%s' %(rd.choice([3,5]), rd.randint(0,9), rd.randint(1000,9999), rd.randint(1000,9999)), rd.choice(['F','M']), rd.choice(['山东','河南','山西','河北','湖南','湖北','北京','上海','广州'])] for i in range(5000)]
columns = ['code','email','age','mobile','gender','area']
#print(data)
df = pd.DataFrame(data=data,columns=columns)
df.set_index(['area','mobile'], inplace = True)
print('Data : \n', df)
'''
    df.query(
        expr:           #类SQL语句表达式(可以使用前缀‘@’引用环境变量，等号为==，而不是=；注：目前不支持like)
        inplace=False   #是否替换原数据
    )
'''
#年龄25 - 35之间,非上海人
print('Person age between 25 and 35 : \n', df.query("age > 25 and age < 35 and area not in ('上海')"))
age = 30
#年龄30 - 35之间,非上海人
print('Person age between %s and 35 : \n' %age, df.query("age > @age and age < 35 and area not in ('上海')"))