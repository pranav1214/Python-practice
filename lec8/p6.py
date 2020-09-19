# wapp to delete a file -> file name given by user


import os.path
filename = input("Enter file name to delete: ")
if os.path.exists(filename):
		os.remove(filename)
		print(filename, " removed")
else:
	print(filename, " does not exists ") 