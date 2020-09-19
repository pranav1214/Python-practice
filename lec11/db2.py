from sqlite3 import *
con = None
try:
	con = connect("employee_database.db")
	print(" Connected ")
	cur = con.cursor()
	sql = "create table emp(eid int primary key, ename text, esalary double)"
	cur.execute(sql)
	print(" Table Created ")
except Exception as e:
	print(" Table Creation Issue ", e)
finally:
	if con is not None:
		con.close()
		print(" Disconnected ")	