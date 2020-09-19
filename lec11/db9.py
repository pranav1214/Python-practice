from sqlite3 import *
con = None
try:
	con = connect("employee_database.db")
	print(" Connected ")
	cur = con.cursor()
	sql = "drop table emp"
	cur.execute(sql)
	print(" Table Dropped ")
except Exception as e:
	print(" Delete Issue ", e)
finally:
	if con is not None:
		con.close()
		print(" Disconnected ")	