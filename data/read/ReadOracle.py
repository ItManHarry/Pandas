import pandas as pd
from data.read.DatabaseEngines import DatabaseEngines
#读取Oracle数据
engine = DatabaseEngines.create('oracle')
print('执行获取所有的用户信息')
users = pd.read_sql('select * from gp_operator where status in (0, 1) and orgid = -1 order by name', con=engine)
print(users)
#写入到Excel
print('执行用户信息写入Excel')
users.to_excel('C:\\Users\\20112004\\Desktop\\tmp\\DCS用户清单.xlsx', encoding='GBK')
#统计用户总数
print('统计用户总数')
uc = pd.read_sql('select count(*) from gp_operator', con=engine)
print('User count is : ', uc)
