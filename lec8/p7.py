#to write into an existing file
# filename and data wud be provided by the user


import os.path
filename = input("Enter Filename to write into: ")
if os.path.isfile(filename):
	f = None
	try:
		f = open(filename, "a")
		data = input("Enter data to write")
		f.write("\n" +data + "\n")
	except Exception as e:
		print("write issues ", e)
	finally:
		if f is not None:
			f.close()
else:
	print(filename, " does not exists ")