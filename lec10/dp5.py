# wapp to insert rows into student table -->input from users

from sqlite3 import *
con = None
try:
	con = connect("test.db")
	print("Connected")
	cur = con.cursor()
	sql = "select * from student"
	cur.execute(sql)
	data = cur.fetchall()
	for d in data:
		print("Roll No", d[0], "Name", d[1])
except Exception as e:
	print("Insertion issue", e)
finally:
	if con is not None:
		con.close()
		print("Disconnected")