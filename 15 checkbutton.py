from tkinter import *

pro = Tk()
pro.geometry('600x400')
################################
r1 = Checkbutton(pro,text="male")
# r1.pack()
r1.place(x=10,y=20)

r2 = Checkbutton(pro,text="female")
# r2.pack()
r2.place(x=10,y=40)
################################
pro.mainloop()
