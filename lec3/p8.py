# read username and pss from user
# if username = kamal and pass = abc123 print success else failure



import getpass
username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")

if (username == 'kamal') and (password == 'abc123'):
	print("Success")
else:
	print("Failure")