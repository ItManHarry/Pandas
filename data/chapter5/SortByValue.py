import pandas as pd
import random as rd
#创建数据
data = [['N%s' %i,'jack%s@163.com' %i, rd.randint(20, 45), '1%s%s%s%s' %(rd.choice([3,5]), rd.randint(0,9), rd.randint(1000,9999), rd.randint(1000,9999)), rd.choice(['F','M']), rd.choice(['山东','河南','山西','河北','湖南','湖北','北京','上海','广州'])] for i in range(5000)]
columns = ['职号','邮箱','年龄','手机号','性别','地区']
#print(data)
df = pd.DataFrame(data=data,columns=columns)
print('Data : \n', df)
'''
    df.sort_values(
        by :                        #指定用于排序的变量名，多列时使用列表提供
        ascending=True    ,         #是否升序排列，多列时以列表形式提供
        inplace=False      ,        #是否更改原数据
        na_position = 'last'  ,     #缺失值的排序顺序（first/last）
        ignore_index=False  ,       #是否忽略原索引值，若为True，则之前的索引消失并重置为0,1,2,...N - 1
        key = None                  #在排序前对索引值引用指定的key函数
    )
'''
#根据年龄排序
print('Sorted by age : \n', df.sort_values('年龄', ascending=False))
print('Source data : \n', df)