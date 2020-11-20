import pandas as pd
import random as rd
#创建数据
data = [['N%s' %i,'jack%s@163.com' %i, rd.randint(20, 45), '1%s%s%s%s' %(rd.choice([3,5]), rd.randint(0,9), rd.randint(1000,9999), rd.randint(1000,9999)), rd.choice(['F','M'])] for i in range(4000)]
columns = ['姓名','邮箱','年龄','手机号','性别']
print(data)
df = pd.DataFrame(data=data,columns=columns)
print(df)
df.to_excel('C:\\Users\\20112004\\Desktop\\tmp\\uis.xlsx',index=False)
#强行更新索引
'''
    df.reindex(
        labels: [...],          #类数组结构的数值，将按此数值重建索引，非必需
        axis:                   #针对哪个轴进行重建 : ('index','columns') or number(0, 1)
        copy=True,              #建立新对象而不是直接修改原数据
        level :                 #考虑被重建的索引级别  
        #缺失数据的处理方式
        method :                #针对已经排过序的索引，确定数据单元格无数据的填充方式，非必需
        pad / ffill:            #用前面有效值进行填充
        backfill / bfill:       #用后面有效值进行填充
        nearest:                #使用最接近的数值进行填充
        fill_value=np.NaN:      #缺失值使用什么数值代替
        limit=None              #向前/向后填充的最大步长                              
    )
'''
print('Reindex without fill : \t', df.reindex([1,2,40,50,100,1000,2000,4001]))
print('Reindex using ffill : \t', df.reindex([1,2,40,50,100,1000,2000,4001], method='ffill'))
print('Reindex using a value : \t', df.reindex([1,2,40,50,100,1000,2000,4001], fill_value='Null'))