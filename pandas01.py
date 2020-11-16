import pandas as pd
print('-' * 80)
df1 = pd.DataFrame(
    {
        'Col1': 1.2,
        'Col2': [1,2,3,4,5,6],
        'Col3': ['a','b','c','d','e','f'],
        'Col4': 'Cons1',
        'Col5': 100
    }
)
print(df1)
print('-' * 80)
df2 = pd.DataFrame(data=[
    [1,2,3,4,5],
    [10,20,30,40,50],
    [100,200,300,400,500],
    [1000,2000,3000,4000,5000],
    [10000,20000,30000,40000,50000],
    [100000,200000,3000000,400000,500000]
],columns=['C01','C02','C03','C04','C05'])
print(df2)
print('-' * 80)
df2.to_excel('C:\\Users\\20112004\\Desktop\\tmp\\DATA.xlsx',encoding='GBK')