from tkinter import *
from tkinter import ttk

pro = Tk()
pro.geometry('600x400')
#---------- Combobox(window,values=(......))
# combo1 = ttk.Combobox(pro,values=('male','female'))
# combo1.place(x=1,y=1)   # to show combo
#----------
## the problem is you can write inside combo 
## solution >> state="readonly"
combo1 = ttk.Combobox(pro,values=('male','female'),state="readonly")
combo1.place(x=1,y=1)   # to show combo

combo2 = ttk.Combobox(pro,values=('Math','DSA','DS',"ML"),state="readonly")
combo2.place(x=1,y=40)   # to show combo
################################
pro.mainloop()