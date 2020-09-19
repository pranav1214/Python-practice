from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("My First GUI")
root.geometry("400x200+400+200")
root.resizable(False, False)
root.configure(background ='red')

def wel():
	showwarning("Info Msg", "Welcome to the app")

btnWelcome = Button(root, text="Welcome", width=10, font=('arial', 20, 'bold'), command=wel)
btnWelcome.pack(pady = 20)

root.mainloop()