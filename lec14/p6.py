from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Corona Counter")
root.geometry("400x400+400+200")

total_count, total_deaths, total_recovered = 0, 0, 0

def f1():
	global total_count, total_deaths, total_recovered
	import socket
	import requests
	import bs4
	import lxml

	try:
		google = ("www.google.com", 80)
		socket.create_connection(google)
		cn = entCountry.get()

		a1 = "https://www.worldometers.info/coronavirus/country/"
		a2 = cn + "/"
		web_address = a1 + a2

		res = requests.get(web_address)
		print(res)
	
		s= bs4.BeautifulSoup(res.text, 'lxml')

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
	except Exception as e:
		showerror("Error", "Enter Valid Country")
		entCountry.delete(0, END)
		entCountry.focus()

def f2():
	global total_count, total_deaths, total_recovered
	import matplotlib.pyplot as plt
	count = ['Total', 'Deaths', 'Recovered']
	total_count = total_count.replace(",", "")
	total_deaths = total_deaths.replace(",", "")	
	total_recovered = total_recovered.replace(",", "")

	values = [float(total_count), float(total_deaths), float(total_recovered)]
	plt.pie(values, labels=count, autopct='%.2f%%')
	plt.axis('equal')
	plt.title("Corona Count")
	plt.show()


lblCountry = Label(root, text="Enter Country Name ", font=('arial', 18, 'bold'))
entCountry = Entry(root, bd=5, font=('arial', 18, 'bold'))
btnGet = Button(root, text="Get Count", font=('arial', 18, 'bold'), command=f1)
btnChart = Button(root, text="Pie Chart", font=('arial', 18, 'bold'), command=f2)
lblCountry.pack(pady=10)
entCountry.pack(pady=10)
btnGet.pack(pady=10)
btnChart.pack(pady=10)
root.mainloop()

