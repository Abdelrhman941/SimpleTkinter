from tkinter import *

pro = Tk()
pro.geometry('600x400')
################################
lst1 = Listbox(pro,width=10,height=5)  # width,height are optional

lst1.insert(0,'one')   # insert in row 0 > one
lst1.insert(1,'two')   # insert in row 0 > one
lst1.pack()            # = place but it show auto in middle
################################
pro.mainloop()