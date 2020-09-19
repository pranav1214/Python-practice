# to read from an existing file

import os.path
filename  = input("Enter file name to read from: ")
if os.path.isfile(filename):
	f = None
	try:
		with open(filename, "r") as f:
			data = f.read()
			print(data)
	except Exception as e:
		print("Read issue ", e)
else:
	print(filename, " does not exists ")