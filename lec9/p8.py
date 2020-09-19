from tkinter import *

root = Tk()
root.title("Color Me")
root.geometry("300x400+400+200")

def r():
	root.configure(background = 'red')
def g():
	root.configure(background = 'green')
def b():
	root.configure(background = 'blue')

btnRed = Button(root, text="Red", width=10, font=('times', 20,'bold'), command=r)
btnGreen = Button(root, text="Green", width=10, font=('times', 20,'bold'), command=g)
btnBlue = Button(root, text="Blue", width=10, font=('times', 20,'bold'), command=b)

btnRed.pack(pady=20)
btnGreen.pack(pady=20)
btnBlue.pack(pady=20)

root.mainloop()