from tkinter import *
from tkinter import ttk

pro = Tk()
pro.geometry('500x400')
################################
nb = ttk.Notebook(pro)
nb.pack()

fr1 = Frame(nb, width=500, height=100,bg="silver")
nb.add(fr1,text="Home")
lbl = Label(fr1,text="Learn Python",bg="silver")
lbl.place(x=10, y=10)

fr2 = Frame(nb,width=500,height=100,bg="silver") 
nb.add(fr2,text="Tools")
lbl = Label(fr2,text="ML",bg="red")
lbl.place(x=10, y=10)

nb.select(fr2)      # to make it the basic
################################
pro.mainloop()