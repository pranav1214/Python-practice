import requests
import socket
try:
	google = ("www.google.com", 80 )
	socket.create_connection(google)
	print("connected")
	
	movie_name = input("Enter Movie Name to Search: ")
	
	a1 = "http://www.omdbapi.com/?"
	a2 = "&apikey=b88add31"
	a3 = "&s=" + movie_name

	web_address = a1 + a2 + a3
	res = requests.get(web_address)
	
	data = res.json()
	print(data)
	
	search = data['Search']
	print(search)
	
	for s in search:
		print('*' * 30)
		title = s['Title']
		print("Title -->", title)
		year = s['Year']
		print("Year -->", year)
		poster = s['Poster']
		print("Poster -->", poster)
	
# to download posters
		if poster != 'N/A':
			res = requests.get(poster)
			file_name = title + ".jpg"
			f = None
			try:
				f = open(file_name, "wb")
				f.write(res.content)
			except Exception as e:
				print("Download Issue ",e)
			finally:
				if f is not None:
					f.close()

except OSError as e:
	print("Issue ", e)
except KeyError as e:
	print("Check Movie Name ", e)