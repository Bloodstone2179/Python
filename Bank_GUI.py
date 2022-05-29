from cProfile import label
from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("430x200+500+250")
root.resizable(False,False)
#main bank page that shows current balance and withdraw or deposit
def mainBank():
    bank = Tk()
    label = Label(bank, text="American standard bank", font=("Times new roman",20))
    label.config(bg="red")
    label.pack()
    bank.mainloop()

global verifyIN, verifyCode
verifyIN = StringVar()
verifyCode = StringVar()


def verifySignIN(event=None):
    verifyCode.set("A")
    if verifyIN.get() == verifyCode.get():
        mainBank()
        print("VERIFIED")
    else:
        tkinter.messagebox.showerror("Error","Verification code is wrong destroying the session\n PLEASE TRY AGAIN")
        #vm.quit()
        #root.quit()
#verification
def verify():

    global vm
    vm = Tk()
    label= Label(vm, text="PLEASE ENTER THE VERIFICATION CODE TO CONTINUE")
    label.pack()
    enter = Entry(vm, textvariable=verifyIN)
    enter.pack()
    enter.bind("<Return>",verifySignIN)
    login = Button(vm, text = "LOGIN", command=verifySignIN)
    login.pack()
    vm.mainloop()

#login page

username = StringVar()
password = StringVar()
Username = StringVar()
Password = StringVar()


Password.set("Admin")
Username.set("Admin")

def login(event=None):
    if username.get() == Username.get() and password.get() == Password.get():
        verify()
    elif username.get() == Username.get() and password.get() != Password.get():
        tkinter.messagebox.showerror("Error","Password is incorrect\n PLEASE TRY AGAIN")
    elif username.get() != Username.get() and password.get() == Password.get():
        tkinter.messagebox.showerror("Error","Username is incorrect\n PLEASE TRY AGAIN")
    elif username.get() != Username.get() and password.get() != Password.get():
        tkinter.messagebox.showerror("Error","Username and password is incorrect\n PLEASE TRY AGAIN")
    


l1=Label(root, text='Welcome To The American express bank of fortune', font=("Times new roman",10))
l1.pack()
l2=Label(root, text='Bank account number', font=('Times new roman', 10))
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