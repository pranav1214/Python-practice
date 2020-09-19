# wapp to insert rows into student table -->input from users

from sqlite3 import *
con = None
try:
	con = connect("test.db")
	print("Connected")
	cur = con.cursor()
	sql = "insert into student values('%d', '%s')"
	rno = int(input("Enter Roll no: "))
	name = input("Enter Name: ")
	cur.execute(sql % (rno, name))
	con.commit()
	print("Record Saved")
except Exception as e:
	print("Insertion issue", e)
	con.rollback
finally:
	if con is not None:
		con.close()
		print("Disconnected")