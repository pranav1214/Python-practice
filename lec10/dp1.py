# wapp to connect and disconnect

from sqlite3 import *
con = None
try:
	con = connect("test.db")
	print("Connected")
except Exception as e:
	print("Connection issue", e)
finally:
	if con is not None:
		con.close()
		print("Disconnected")