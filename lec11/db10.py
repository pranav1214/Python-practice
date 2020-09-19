from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *

def f1():
	adst.deiconify()
	root.withdraw()

def f2():
	root.deiconify()
	adst.withdraw()

def f3():
	vist_stData.delete(1.0, END)
	vist.deiconify()
	root.withdraw()
	con = None
	try:
		con = connect("student_database.db")
		cur = con.cursor()
		sql = "select * from student"
		cur.execute(sql)
		data = cur.fetchall()
		msg = ""
		for d in data:
			msg = msg + " Rno= " + str(d[0]) + " Name= " + str(d[1]) + "\n"
		vist_stData.insert(INSERT, msg)
	except Exception as e:
		showerror(" Issue ", e)
	finally:
		if con is not None:
			con.close()

def f4():
	root.deiconify()
	vist.withdraw()

def f5():
	con = None
	try:
		con = connect("student_database.db")
		cur = con.cursor()
		sql = "insert into student values('%d', '%s')"
		srno = adst_entRno.get()
		if not srno.isdigit():
			showerror("Mistake", "rno should be integers")
			adst_entRno.delete(0, END)
			adst_entRno.focus()
			return
		rno = int(srno)
		name = adst_entName.get()
		if not name.isalpha():
			showerror("Mistake", "Name should contain letter only")
			adst_entName.delete(0, END)
			adst_entName.focus()
			return			
		cur.execute(sql % (rno, name))
		con.commit()
		showinfo("Success ", "Row Inserted ")
	except Exception as e:
		con.rollback()
		showerror("Issue ", e)
	finally:
		if con is not None:
			con.close()
	adst_entRno.delete(0, END)
	adst_entName.delete(0, END)
	adst_entRno.focus()	


#first window
root = Tk()
root.title("S.M.S")
root.geometry("500x500+400+100")

btnAdd = Button(root, text="Add", width=10, font=('arial', 18, 'bold'), command=f1)
btnView = Button(root, text="View", width=10, font=('arial', 18, 'bold'), command=f3)

btnAdd.pack(pady=10)
btnView.pack(pady=10)

def on_close():
	if askokcancel("Quit", "Are you sure you want to exit? "):
		root.destroy()
root.protocol("WM_DELETE_WINDOW", on_close)


#Add student window
adst = Toplevel(root)
adst.title("Add St.")
adst.geometry("500x500+400+100")

adst_lblRno = Label(adst, text="Enter Rno", font=('arial', 18, 'bold'))
adst_lblName = Label(adst, text="Enter Name", font=('arial', 18, 'bold'))
adst_entRno = Entry(adst, bd=5, font=('arial', 18, 'bold'))
adst_entName = Entry(adst, bd=5, font=('arial', 18, 'bold'))
adst_btnSave = Button(adst, text="Save", font=('arial', 18, 'bold'), command=f5)
adst_btnBack = Button(adst, text="Back", font=('arial', 18, 'bold'), command=f2)

adst_lblRno.pack(pady=5)
adst_entRno.pack(pady=5)
adst_lblName.pack(pady=5)
adst_entName.pack(pady=5)
adst_btnSave.pack(pady=5)
adst_btnBack.pack(pady=5)

adst.withdraw()

#view window
vist = Toplevel(root)
vist.title("View St.")
vist.geometry("500x500+400+100")

vist_stData = ScrolledText(vist, width=35, height=10, font=('arial', 18, 'bold'))
vist_btnBack = Button(vist, text="Back", font=('arial', 18, 'bold'), command=f4)

vist_stData.pack(pady=10)
vist_btnBack.pack(pady=10)

vist.withdraw()

root.mainloop()










































