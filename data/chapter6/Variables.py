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
#添加一新列
df.newcol = 1       #此写法虽然不会报错，但是不会生效
print('Now the data is : \n', df)
df['newcol'] = [100,200,300,400,480,980]    #此写法为正确的写法
print('-' * 80)
print('Now the data is : \n', df)
#改变新列值为平方根
df['newcol'] = np.sqrt(df['newcol'])
print('Change the new column value : \n', df)