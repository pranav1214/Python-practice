# wapp to insert rows into student table

from sqlite3 import *
con = None
try:
	con = connect("test.db")
	print("Connected")
	cur = con.cursor()
	sql = "insert into student values(10, 'Amit')"
	cur.execute(sql)
	con.commit()
	print("Record Saved")
except Exception as e:
	print("Insertion issue", e)
finally:
	if con is not None:
		con.close()
		print("Disconnected")