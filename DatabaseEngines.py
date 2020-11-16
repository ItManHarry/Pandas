import cx_Oracle as cxoc
from sqlalchemy import create_engine
#数据库引擎集
class DatabaseEngines:

    #数据库链接信息
    mysql_uri = 'mysql+pymysql://root:root2019@localhost:3306/sdb?charset=gbk'
    oracle_lib_dir = r"D:\Development\Python\db-drivers\instantclient_19_8"
    oracle_uri = 'oracle+cx_oracle://dcstest0801:Tsv33db#2016@10.40.128.171:1521/orcl?encoding=UTF-8&nencoding=UTF-8'
    sqlite_path = 'sqlite:///C:\\Users\\20112004\\Desktop\\tmp\\test.db'

    #创建数据库引擎
    @classmethod
    def create(cls,database_type):
        if database_type == 'mysql':
            engine = create_engine(cls.mysql_uri)
        if database_type == 'oracle':
            cxoc.init_oracle_client(lib_dir=cls.oracle_lib_dir)
            engine = create_engine(cls.oracle_uri)
        if database_type == 'sqlite':
            engine = create_engine(cls.sqlite_path)
        return engine