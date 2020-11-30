import pandas as pd
import numpy as np
print('-' * 80)
df = pd.DataFrame(
    {
        'Col1': 1.2,
        'Col2': [1,2,3,4,5,6],
        'Col3': ['a','b','c','d','e','f'],
        'Col4': 'Cons1',
        'Col5': 100
    }
)
print('Source data is : \n', df)
print('-' * 80)
#哑变量
'''
    pd.get_dummies(
        data:               #对应的数据框/变量列
        prefix = None       #哑变量前缀
        prefix_sep = '_'    #哑变量序号分隔符
        dummy_na = False    #是否为NaNs专门设定一个哑变量列
        drop_first = False  #是否返回k-1哑变量，而不是k个变量
    )
'''
print(pd.get_dummies(df.Col2, prefix='Dummy'))
print(pd.get_dummies(df, columns=['Col3'], prefix='列4'))
#数值变量分段(分箱)
'''
    pd.cut(
        x:                      #进行分段的变量名称
        bins:                   #具体的分段设定(int : 被等距等分的段数, sequence of scalars : 具体的每一个分段起点，必须包括最值，可不等距)
        right=True              #每段是否包括右侧界值
        labels=None             #为每个分段提供自定义标签
        include_lowest = False  #第一段是否包括最左侧界值，需要和right参数配合使用
    )
    
    pd.pcut()       #按照频数，而不是按照取值范围进行等分
'''
df['Class'] = pd.cut(df.Col2, bins=[1,3,7], right=False)
print('Now the data is : \n', df)