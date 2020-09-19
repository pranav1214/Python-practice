from sqlite3 import *
con = None
try:
	con = connect("employee_database.db")
	print(" Connected ")
	cur = con.cursor()
	sql = "delete from emp where eid = '%d'"
	eid = int(input(" Enter id to delete "))
	cur.execute(sql % (eid))
	con.commit()
	if cur.rowcount > 0:
		print(" Record Deleted ")
	else:
		print(" Record does not exists ")
except Exception as e:
	print(" Delete Issue ", e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print(" Disconnected ")	