# wapp to create a file -> file name given by user


import os.path
filename = input("Enter file name to create: ")
if os.path.exists(filename):
	print(filename, " already exists")
else:
	f = None
	try:
		f = open(filename, "a")
		print(filename, " created")
	except Exceptions as e:
		print("file creation issue: ", e)
	finally:
		if f is not None:
			f.close() 