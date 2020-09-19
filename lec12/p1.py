#to check if you are connected to internet


import socket
try:
	google = ("www.google.com", 80)
	socket.create_connection(google)
	print("Connected")
except OSError as e:
	print("issue", e)