from sqlite3 import *
con = None
try:
	con = connect("employee_database.db")
	print(" Connected ")
	cur = con.cursor()
	sql = "insert into emp values('%d', '%s', '%f')"
	eid = int(input(" Enter the id "))
	ename = input(" Enter the Name ")
	esalary = float(input(" Enter the Salary "))
	cur.execute(sql % (eid, ename, esalary))
	con.commit()
	print(" Record Added ")
except Exception as e:
	print(" Insert Issue ", e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print(" Disconnected ")	