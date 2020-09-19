#to connect to ipinfo.io and get some info

import socket
import requests
try:
	google = ("www.google.com", 80)
	socket.create_connection(google)
	print("Connected")
	
	res = requests.get("https://ipinfo.io")
	print(res)
	
	data = res.json()
	print(data)

	city_name = data['city']
	print(city_name)

	cur_loc = data['loc']
	print(cur_loc)
	x = cur_loc.split(",")
	print("Lat= ", x[0])
	print("Long= ", x[1])
	
except OSError as e:
	print("issue", e)