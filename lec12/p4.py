import requests
import socket
try:
	google = ("www.google.com", 80 )
	socket.create_connection(google)
	print("connected")
	
	img_url= "https://upload.wikimedia.org/wikipedia/commons/d/d3/Gateway_of_India_-Mumbai.jpg"
	res = requests.get(img_url)
	print(res)
		
	file_name = "mumbai.jpg"
	f= None
	try:
		f = open(file_name, "wb")
		f.write(res.content)
	except Exception as e:
		print("Download Issue ", e)
	finally:
		if f is not None:
			f.close()

except OSError as e:
	print("Issue ", e)

