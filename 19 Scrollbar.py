from tkinter import *
from tkinter import ttk

pro = Tk()
pro.geometry('500x400')
################################
## there are two ways to show button >>
sc1 = Scrollbar(pro,orient=VERTICAL)
sc1.pack(side=RIGHT,fill=Y)
## fill = Y  >> if VERTICAL
## fill = X  >> if HORIZONTAL

sc2 = ttk.Scrollbar(pro,orient=HORIZONTAL)
sc2.pack(side=BOTTOM,fill=X)
################################
pro.mainloop()