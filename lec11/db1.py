from sqlite3 import *
con = None
try:
	con = connect("employee_database.db")
	print("Connected")
except Exception as e:
	print(" Connection Issue ", e)
finally:
	if con is not None:
		con.close()
		print("Disconnected")	