from tkinter import *
from tkinter.messagebox import *
from datetime import *

root = Tk()
root.title("Age Calculator")
root.geometry("400x400+500+200")

lblNumber = Label(root, text="Enter DOB --> dd/mm/yyyy", font=('courier', 14,'bold italic'))
lblNumber.pack(pady=10)

entNumber = Entry(root, bd=5, font=('courier', 14,'bold italic'))
entNumber.pack(pady=10)
entNumber.focus()

def age():
	try:
		s1 = entNumber.get()
		d = s1.split("/")
		dob = date(int (d[2]), int (d[1]), int (d[0]))
		today = datetime.now().date()
		days = (today - dob)
		age = (today - dob) / timedelta(365.24)
		age = round(age, 2)
		msg = "Age = " + str(age) + " days " + str(days)
		showinfo("Your Age ", msg )
	except (ValueError, IndexError):
		showerror("Mistake", 'You need to enter dd/mm/yyyy only ')
		entNumber.delete(0 , END)
		entNumber.focus()

btnFind = Button(root, text="Find", font=('courier', 24,'bold italic'), command=age)

btnFind.pack(pady=10)

root.mainloop()