from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Even Odd Calculator")
root.geometry("400x400+500+200")
root.configure(background="green")

lblNumber = Label(root, text="Enter Number", font=('courier', 24,'bold italic'))
lblNumber.pack(pady=10)

entNumber = Entry(root, bd =5, font=('courier', 24,'bold italic'))
entNumber.pack(pady=10)
entNumber.focus()

def eo():
	try:
		s1 = entNumber.get()
		n1 = int(s1)
		if n1 % 2 == 0:
			res = "Number is Even"
		else:
			res = "Number is Odd"
		showinfo("Result ", res)
	except ValueError:
		showerror("Mistake", 'You need to enter integers only')
		entNumber.delete(0, END)
		entNumber.focus()

btnFind = Button(root, text="Find", font=('courier', 24,'bold italic'), command=eo)
btnFind.pack(pady=10)

root.mainloop()