import pandas as pd
from data.read.DatabaseEngines import DatabaseEngines
users = pd.DataFrame(columns=['Name','Email','Address','Mobile','age','birthday'],
    data=[
        ['Harry','jack1@163.com','SD JN','13780924007',20,'1985-12-02'],
        ['Jack','jack2@163.com','SD JN','13780924007',26,'1985-12-02'],
        ['Tom','jack3@163.com','SD JN','13780924007',27,'1985-12-02'],
        ['Will','jack4@163.com','SD JN','13780924007',28,'1985-12-02'],
        ['Bill','jack5@163.com','SD JN','13780924007',24,'1985-12-02'],
        ['Alex','jack6@163.com','SD JN','13780924007',29,'1985-12-02'],
        ['Max','jack7@163.com','SD JN','13780924007',31,'1985-12-02'],
        ['Jane','jack8@163.com','SD JN','13780924007',30,'1985-12-02'],
        ['Jon','jack9@163.com','SD JN','13780924007',23,'1985-12-02'],
        ['Dany','jack10@163.com','SD JN','13780924007',22,'1985-12-02']
    ]
)
print(users)
'''
    df.to_sql(
        name='table name',      #表名
        con=engine,             #SQLAlchemy引擎
        if_exists='append',     #如果表已经存在，如何处理,取值：‘fail’：不做任何处理，‘replace’：删除源表并重建新表；‘append’：在原表追加数据
        index=False             #是否导出索引
    )
'''
connection_engine = DatabaseEngines.create('mysql')
users.to_sql(name='tb_user',con=connection_engine,if_exists='replace',index=True)
print('数据已导入数据库')