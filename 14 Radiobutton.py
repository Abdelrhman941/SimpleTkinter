from tkinter import *
from tkinter import ttk

pro = Tk()
pro.geometry('600x400')
################################
## there are two ways to show button >>
r1 = Radiobutton(pro,text="male1",value=1)
# r1.pack()
r1.place(x=10,y=20)

r2 = Radiobutton(pro,text="female1",value=2)
# r2.pack()
r2.place(x=10,y=40)
# ---------
r3 = ttk.Radiobutton(pro,text="male2",value=3)
# r3.pack()
r3.place(x=10,y=80)

r4 = ttk.Radiobutton(pro,text="female2",value=4)
# r4.pack()
r4.place(x=10,y=100)
################################
pro.mainloop()
