import pandas as pd
print('-' * 80)
users = pd.DataFrame(columns=['Name','Email','Address','Mobile','age'],
    data=[
        ['Harry','jack1@163.com','SD JN','13780924007',20],
        ['Jack','jack2@163.com','SD JN','13780924007',26],
        ['Tom','jack3@163.com','SD JN','13780924007',27],
        ['Will','jack4@163.com','SD JN','13780924007',28],
        ['Bill','jack5@163.com','SD JN','13780924007',24],
        ['Alex','jack6@163.com','SD JN','13780924007',29],
        ['Max','jack7@163.com','SD JN','13780924007',31],
        ['Jane','jack8@163.com','SD JN','13780924007',30],
        ['Jon','jack9@163.com','SD JN','13780924007',23],
        ['Dany','jack10@163.com','SD JN','13780924007',22]
    ]
)
print(users)
'''
    to_csv(
        filepath_or_buffer:''   #文件路径,
        sep=','                 #分隔符,
        columns=[...],          #导出的变量列表 
        header=True,            #重置变量名，也可提供新的列表
        index=True,             #是否导出索引
        mode='',                #导出模式：r,r+,w,w+,a,a+
        encoding='utf-8'        #编码集       
    )
'''
users.to_csv('C:\\Users\\20112004\\Desktop\\tmp\\users.txt',index=False,header=['姓名','邮箱','地址'],columns=['Name','Email','Address'],mode='a+')
print('-' * 80)