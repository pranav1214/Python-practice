from sqlite3 import *
con = None
try:
	con = connect("employee_database.db")
	print(" Connected ")
	cur = con.cursor()
	sql = "select * from emp"
	cur.execute(sql)
	d = cur.fetchone()
	while d:
		print(" Eid= ", d[0], " Ename= ", d[1], " Esalary= ", d[2] )
		d = cur.fetchone()
except Exception as e:
	print(" Insert Issue ", e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print(" Disconnected ")	