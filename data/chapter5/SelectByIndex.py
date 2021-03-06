import pandas as pd
import random as rd
#创建数据
data = [['N%s' %i,'jack%s@163.com' %i, rd.randint(20, 45), '1%s%s%s%s' %(rd.choice([3,5]), rd.randint(0,9), rd.randint(1000,9999), rd.randint(1000,9999)), rd.choice(['F','M']), rd.choice(['山东','河南','山西','河北','湖南','湖北','北京','上海','广州'])] for i in range(5000)]
columns = ['职号','邮箱','年龄','手机号','性别','地区']
#print(data)
df = pd.DataFrame(data=data,columns=columns)
df.set_index(['地区','手机号'], inplace = True)
print('Data : \n', df)
sl = [True, False, True, True]
#按照索引值筛选
print('Shanghai and Hunan : \n', df.loc[['上海','湖南']])
#print(df.loc[[('河北','15254809555'),('广州','15273142801')]])
#多索引筛选
'''
    df.xs(
        key,            #索引值
        level=None      #使用哪个索引
        drop_level=True #是否删除索引列
    )
'''
print('ShangHai data : \n', df.xs('上海', level=0, drop_level=False))