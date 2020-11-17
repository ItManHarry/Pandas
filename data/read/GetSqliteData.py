from data.read.DatabaseEngines import DatabaseEngines
import pandas as pd
#dbengine = DatabaseEngines()
engine = DatabaseEngines.create('sqlite')
print(engine)
age = 36
sql = '''
    select 
        *
    from user_tb
    where age > %d
''' %(age,)
users = pd.read_sql(sql, con=engine)
print(users)