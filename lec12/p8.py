import socket
import requests
import bs4
import lxml

try:
	google = ("www.google.com", 80)
	socket.create_connection(google)
	print("Connected")

	res = requests.get("https://www.worldometers.info/coronavirus/country/india/")
	print(res)
	
	s= bs4.BeautifulSoup(res.text, 'lxml')
	print(s)

	data = s.find_all("div", {"class":"maincounter-number"})
	print(data)
	
	total_count = data[0].find('span').text
	total_deaths = data[1].find('span').text
	total_recovered = data[2].find('span').text

	print("Total Count: ", total_count)
	print("Total Deaths: ", total_deaths)
	print("Total Recovered: ", total_recovered)

except OSError as e:
	print("Issue ", e)