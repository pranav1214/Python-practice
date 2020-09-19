# to read from an existing file

import os.path
filename  = input("Enter file name to read from: ")
if os.path.isfile(filename):
	f = None
	try:
		f = open(filename, "r")
		data = f.read()
		print(data)
	except Exception as e:
		print("Read issue ", e)
	finally:
		if f is not None:
			f.close()
else:
	print(filename, " does not exists ")