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
print('data types : \n', data.dtypes)
'''
    df.astype(
        dtype=''        #指定希望转换的数据类型，可以使用numpy或者python中的类型:int/float/bool/str,
        copy=True,      #是否生成新的副本，而不是替换源数据
        errors='raise'  #转换出错时是否抛出错误，‘raise / ignore’
    )
'''
new_data = data.astype('str')
print('New data types are : \n', new_data.dtypes)
print('Old data types are : \n', data.dtypes)
new_data = data['C02'].astype('str',copy=False, errors='ignore')
print('Now the new data types are : \n', new_data.dtypes)
print('Old the new data types are : \n', data.dtypes)