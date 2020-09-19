from sqlite3 import *
con = None
try:
	con = connect("employee_database.db")
	print(" Connected ")
	cur = con.cursor()
	sql = "update emp set ename = '%s', esalary = '%d' where eid = '%d'"
	eid = int(input(" Enter id to update "))
	ename = input(" Enter emp name ")
	esalary = float(input(" Enter salary "))
	cur.execute(sql % (ename, esalary, eid))
	con.commit()
	if cur.rowcount > 0:
		print(" Record Updated ")
	else:
		print(" Record does not exists ")
except Exception as e:
	print(" Insert Issue ", e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print(" Disconnected ")	