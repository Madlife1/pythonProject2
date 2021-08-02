import MySQLdb
db=MySQLdb.connect("localhost", "root", "", "wordpress", charset='utf8' )

# 通过cursor创建游标
cursor = db.cursor()
# 执行数据查询
sql1 = "USE wordpress"
cursor.execute(sql)

#查询数据库单条数据
result = cursor.fetchone()
print(result)