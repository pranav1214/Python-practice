from tkinter import *

root = Tk()
root.title("Color Me")
root.geometry("300x400+400+200")

def c(num):
	if num == 1:
		root.configure(background = 'red')
	elif num ==2:
		root.configure(background = 'green')
	else:
		root.configure(background = 'blue')

btnRed = Button(root, text="Red", width=10, font=('times', 20,'bold'), command=lambda:c(1))
btnGreen = Button(root, text="Green", width=10, font=('times', 20,'bold'), command=lambda:c(2))
btnBlue = Button(root, text="Blue", width=10, font=('times', 20,'bold'), command=lambda:c(3))

btnRed.pack(pady=20)
btnGreen.pack(pady=20)
btnBlue.pack(pady=20)

root.mainloop()