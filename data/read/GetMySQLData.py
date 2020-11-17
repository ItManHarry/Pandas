from data.read.DatabaseEngines import DatabaseEngines
import pandas as pd
#dbengine = DatabaseEngines()
engine = DatabaseEngines.create('mysql')
print(engine)
users = pd.read_sql('select * from sys_user',con=engine)
print(users)
uc = pd.read_sql('select count(*) from sys_user', con=engine)
print(type(uc))
print(uc)
ud = users.to_dict()
print(type(ud))
for k,v in ud.items():
    print('Key is : ', k, ' value type is : ', type(v), ' the 12th data is : ', v.get(11))
    for kk,vv in v.items():
        print('Key is :', kk, ' value is : ', vv)