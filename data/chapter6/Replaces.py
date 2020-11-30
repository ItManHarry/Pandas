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
#iloc绝对定位替换
df['Col1'].iloc[2:5] = 2.5
print('Now the data is : \n', df)
#loc相对位置替换
df['Col4'].loc[2:5] = 'NewValue'
print('Now the data is : \n', df)
df.loc[df['Col2'] < 5, 'Col5'] = 200
print('Now the data is : \n', df)
df.Col5[df.Col2 < 5] = 300
print('Now the data is : \n', df)
#query必须使用index定位，然后实现数值替换
df.loc[df.query("Col1 < 2 and Col5 < 300").index, 'Col4'] = 'Harry'
print('Now the data is : \n', df)