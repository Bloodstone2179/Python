import requests
from tkinter import *

root = Tk()
url = "https://api.nationalize.io?name="

name=StringVar()
en = Entry(root, textvariable=name)
en.pack()

def guess():
    headers = {'0': 'country_id'}
    out =  requests.get(url + name.get(), headers=headers)
    print("AVALIABLE HEADER: " + str(out.headers))
    print("OUTPUT: " + str(out))

bu = Button(root, text="Guess Nationality NOW!!!!!!!", command=guess())
bu.pack()



root.mainloop()