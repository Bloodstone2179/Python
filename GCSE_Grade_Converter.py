from tkinter import *
import  tkinter.messagebox 

root=Tk()
root.geometry("430x200+500+250")
root.resizable(False,False)

Username=StringVar()
Password=StringVar()
username=StringVar()
password=StringVar()

Username.set("Admin")
Password.set("password1")

#functions
#Function for the Grades
def ax():
	tkinter.messagebox.showinfo('A*', 'A* is now the equivilant of  9')
def a():
	tkinter.messagebox.showinfo('A','A is now the equivilant of a 7 and 8')
def b():
	tkinter.messagebox.showinfo('B','B is now the equivilant of a 6 and a 5')
def c():
	tkinter.messagebox.showinfo('C','C is now the equivilant of a 4 and 5')
def d():
	tkinter.messagebox.showinfo('D','D is now the equivilant of a 3')
def e():
	tkinter.messagebox.showinfo('E','E is the equivilant of a 2')
def f():
	tkinter.messagebox.showinfo('F','F is the equivilant of a 1')
def g():
	tkinter.messagebox.showinfo('G','G is the equivilant of a 1')

def exit():
	root.destroy()
	grades.destroy()
def login(event=None):
	if Username.get()==username.get():
		if Password.get()==password.get():
			root.withdraw()
			grades=Tk()
			grades.resizable(False,False)

			
			title_label=Label(grades, text='Old Grades To New Grades [A*-E] - [9-0]', font=('Times new roman', 10))
			title_label.pack()
			Ax=Button(grades, text='A*', command=ax, font=('Times new roman', 10))
			Ax.pack()
			A=Button(grades, text='A', font=('Times new roman', 10), command=a)
			A.pack()		
			B=Button(grades, text='B', font=('Times new roman', 10), command=b)
			B.pack()
			C=Button(grades, text='C', font=('Times new roman', 10), command=c)
			C.pack()
			D=Button(grades, text='D', font=('Times new roman', 10), command=d)
			D.pack()
			E=Button(grades, text='E', font=('Times new roman', 10), command=e)
			E.pack()
			F=Button(grades, text='F', font=('Times new roman', 10), command=f)
			F.pack()
			G=Button(grades, text='G', font=('Times new roman', 10), command=g)
			G.pack()
			grades.mainloop()
			
		else:
			tkinter.messagebox.showerror("Error","Username or password is incorrect")
	else:
		tkinter.messagebox.showerror("Error","Username or password is incorrect")


#widgets
#Login
l1=Label(root, text='Welcome To The New Grading System', font=("Times new roman",10))
l1.pack()
l2=Label(root, text='Username', font=('Times new roman', 10))
l2.place(x=0,y=40)
l3=Label(root, text='Password', font=('Times new roman', 10))
l3.place(x=0,y=80)
e1=Entry(root,textvariable=username)
e1.place(x=130,y=48)
e2=Entry(root,textvariable=password,show="*")
e2.bind("<Return>",login)
e2.place(x=130,y=88)
Login_Button=Button(root,text="login",command=login, font=('Times new roman', 10))
Login_Button.place(x=354,y=120)
Exit_Button=Button(root, text='Exit', command=exit, font=('Times new roman', 10))
Exit_Button.place(x=0,y=120)

root.mainloop()
