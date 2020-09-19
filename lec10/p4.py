from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Square Calculator")
root.geometry("500x300+400+200")

def sqr():
	try:
		s1 = entNumber.get()
		n1 = float(s1)
		r1 = n1 * n1
		showinfo("Result", r1)
	except ValueError:
		showerror("Issue", "numbers only")	
		entNumber.delete(0, END)
		entNumber.focus()

lblNumber = Label(root, text="Enter Number: ", font=('courier', 14,'bold italic'))
entNumber = Entry(root, bd=5, font=('courier', 14,'bold italic'))
entNumber.focus()
btnFind = Button(root, text="Find", font=('courier', 14,'bold italic'), command=sqr)

lblNumber.place(x=20, y=20)
entNumber.place(x=200, y=20)
btnFind.place(x=150, y=80)

root.mainloop()