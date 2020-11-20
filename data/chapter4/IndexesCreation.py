import pandas as pd
from data.read.DatabaseEngines import DatabaseEngines
#创建时指定索引
data = pd.DataFrame(data=[
    [1,2,3,4,5],
    [10,20,30,40,50],
    [100,200,300,400,500],
    [1000,2000,3000,4000,5000],
    [10000,20000,30000,40000,50000],
    [100000,200000,3000000,400000,500000]
],columns=['C01','C02','C03','C04','C05'],index=['a','b','c','d','e','f'])
print(data)
print('-' * 80)
#读取时指定某一列为索引(index_col=?)
engine = DatabaseEngines.create('mysql')
print(type(engine))
users_index = pd.read_sql('select * from sys_user',con=engine,index_col='tid')
users_no_index = pd.read_sql('select * from sys_user',con=engine)
print('MySQL user with index : \n', users_index)
print('MySQL user without index : \n', users_no_index)
#创建复合索引
engine = DatabaseEngines.create('oracle')
users_oracle = pd.read_sql('select * from gp_operator where status in (0, 1) and orgid = -1 order by name', con=engine)
users_oracle_copy = users_oracle.copy()     #oracle用户数据副本
users_oracle.set_index(['id','code'],drop=True, inplace=True)
print('Oracle users with index : \n', users_oracle)
print('Oracle users without index : \n', users_oracle_copy)
#指定某列为索引列
'''
    df.set_index(
        keys:''         #被指定的索引列列名，复合索引用list格式提供,
        drop=True,      #建立索引后是否删除该列
        append=False,   #是否在原索引基础上添加索引，默认是直接替换原索引
        inplace=False   #是否直接修改原数据
    )
'''
users_no_index.set_index('tid',drop=True,inplace=True)
print('Set MySQL user index : \n', users_no_index)
#将索引还原回列
'''
    df.reset_index(
        drop = False,   #是否将索引直接删除，而不是还原为变量列
        inplace = False,#是否直接修改原数据
        level=None      #对于多重索引，确定转换哪个级别为变量
    )
'''
#还原MySQL用户数据索引
users_no_index.reset_index('tid',inplace=True)
print('MySQL user index has been reset : \n', users_no_index)
users_oracle.reset_index(['code'],drop=True,inplace=True)
print('Oracle user reset index : \n', users_oracle)
print('-' * 80)
print('Indexes : ', users_oracle.index)
print('Index names : ', users_oracle.index.names)
#修改索引名称
users_oracle.index.names = ['数值ID']
print('Now the index names : ', users_oracle.index.names)
print(users_oracle)
#修改索引值：索引值是无法单个修改的，所以此处的修改本质上就是全部修改
print('MySQL user : \n', users_index)
users_index.index.names = ['自增ID']
print('MySQL user index name changed : \n', users_index)
users_index.index = ['id00%s' %i for i in range(12)]
print('MySQL user index value changed : \n', users_index)
