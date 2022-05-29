from random import *
from tkinter import *
from tkinter import messagebox

mainMenu = Tk()

ranndomNumber1 = 0
randomNumber2 =0
def score():
    score = int(score)
    score = score + 1

    
def add():
    add1 = Tk()
    mainMenu.quit()
    label = Label(add1, text="What is  10 + 244")
    label.pack()
    op1 = Button(add1, text="255", command=AddNext())
    op1.pack()
    op2= Button(add1, text="420")
    op2.pack()
    add1.mainloop()
def AddNext():
    add2 = Tk()
    label = Label(add2, text="what is 718 + 42")
    label.pack() 
    op1 = Button(add2, text="760", command=  add2.quit())
    op1.pack()
    op2= Button(add2, text="780")
    op2.pack()

    add2.mainloop()

def multiply():
    m1 = Tk()
    label = Label(m1, text="What is  6844 * 484")
    label.pack()
    op1 = Button(m1, text="3312496", command=  multiNext())
    op1.pack()
    op2= Button(m1, text="331200")
    op2.pack()
    m1.mainloop()
def multiNext():
    m2 = Tk()
    label = Label(m2, text="what is 718 * 42")
    label.pack() 
    op1 = Button(m2, text="30156", command=m2.quit())
    op1.pack()
    op2= Button(m2, text="30000")
    op2.pack()

    m2.mainloop()
def sub():
    s1 = Tk()
    label = Label(s1, text="What is  6844  484")
    label.pack()
    op1 = Button(s1, text="6360 ", command=  subNext())
    op1.pack()
    op2= Button(s1, text="14.2251454959 ")
    op2.pack()
    s1.mainloop()
def subNext():
    s2 = Tk()
    label = Label(s2, text="what is 718 - 42")
    label.pack() 
    op1 = Button(s2, text="676", command=s2.quit())
    op1.pack()
    op2= Button(s2, text="592")
    op2.pack()

    s2.mainloop()
def div():
    d1 = Tk()
    label = Label(d1, text="What is  6844 / 484")
    label.pack()
    op1 = Button(d1, text="14.2231404959 ", command=  divNext())
    op1.pack()
    op2= Button(d1, text="14.2251454959")
    op2.pack()
    d1.mainloop()
def divNext():
    d2 = Tk()
    label = Label(d2, text="what is 718 / 42")
    label.pack() 
    op1 = Button(d2, text="17.0952380952", command=d2.quit())
    op1.pack()
    op2= Button(d2, text="17.095238095212234")
    op2.pack()

    d2.mainloop()
#mainMenu
title = Label(mainMenu, text="Pick a function to use")
title.grid(row=0, column=0)
addButton = Button(mainMenu, text="+", command=add)
addButton.grid(row=2, column = 0)

subButton = Button(mainMenu, text="-")
subButton.grid(row=2, column=1)

multiButton = Button(mainMenu, text="*", command=multiply)
multiButton.grid(row=3, column = 0)

divButton = Button(mainMenu, text="/")
divButton.grid(row=3, column=1)
mainMenu.mainloop()