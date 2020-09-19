from sqlite3 import *
con = None
try:
	con = connect("employee_database.db")
	print(" Connected ")
	cur = con.cursor()
	sql = "insert into emp values(101, 'raju', 5000)"
	cur.execute(sql)
	con.commit()
	print(" Record Added in DB ")
except Exception as e:
	print(" Table Creation Issue ", e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print(" Disconnected ")	