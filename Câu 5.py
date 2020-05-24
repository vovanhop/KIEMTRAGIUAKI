from tkinter import *
from tkinter import BooleanVar
def onClick():
    if var.get() == True:
        var.set(False)
    else:
        var.set(True)

root = Tk()
root.geometry("250x150+300+300")

var=BooleanVar()
cb=Checkbutton(root, text='Show title',variable=var)
cb.place(x=150,y=50)
bt=Button(root,text='Click',command=onClick)
bt.place(x=50,y=50)
root.mainloop()