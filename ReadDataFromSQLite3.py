#connect SQLite3
#1. 打开数据库连接
# SQLite是一个没有后台进程的数据库，磁盘上一个文件就可以对应SQLite数据库
import sqlite3
connection = sqlite3.connect('C:\\Users\\20112004\\Desktop\\tmp\\test.db')
#2. 打开游标
cursor = connection.cursor()
#3. 使用游标的execute方法执行任意的SQL语句（DDL）
print('1. 读取用户数据')
cursor.execute('''
	select * from user_tb
''')
print('-' * 80)
#获取列信息
print('数据列 : ')
for columns in cursor.description:
	print(columns[0])
print('-' * 80)
print('数据值 : ')
while True:
	row = cursor.fetchone()
	if not row:
		break
	else:
		for data in row:
			print(data, end='\n')
	print('-' * 80)
#4. 关闭游标
print('-' * 80)
print('2. 关闭数据库游标')
cursor.close()
#5. 关闭连接
print('3. 关闭数据库链接')
connection.close()