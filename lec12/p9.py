from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Corona Counter")
root.geometry("400x400+400+200")

def f1():
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
		
		msg = "Total Count " + total_count + "\nDeath Count: " + total_deaths + "\nTotal Recovered: " + total_recovered
		showinfo("Count ", msg)
	
	except OSError as e:
		showerror("Issue ", e)
btnGet = Button(root, text="Get Info", command=f1)
btnGet.pack(pady=10)
root.mainloop()

