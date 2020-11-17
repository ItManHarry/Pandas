#connect SQLite3
#1. 打开数据库连接
# SQLite是一个没有后台进程的数据库，磁盘上一个文件就可以对应SQLite数据库
import sqlite3
connection = sqlite3.connect('C:\\Users\\20112004\\Desktop\\tmp\\test.db')
#2. 打开游标
cursor = connection.cursor()
#3. 使用游标的execute方法执行任意的SQL语句（DDL）
#创建表
print('1. 创建用户表')
cursor.execute('''
	create table user_tb(
		id integer primary key autoincrement,
		name text,
		passed text,
		age integer
	)
''')
#写入数据
print('2. 写入用户数据')
cursor.executemany('''
	insert into user_tb(name,passed,age)
	values(?,?,?)
''', (
	('Harry1','12345678',36),
	('Harry2','12345678',37),
	('Harry3','12345678',38),
	('Harry4','12345678',39),
	('Harry5','12345678',40)
))
print('4. 提交数据')
#提交事务
connection.commit()
#4. 关闭游标
print('5. 关闭数据库游标')
cursor.close()
#5. 关闭连接
print('6. 关闭数据库链接')
connection.close()