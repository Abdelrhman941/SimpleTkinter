from tkinter import *

pro = Tk()
pro.geometry('500x400')
################################
sc1 = Scale(pro,from_=1,to=100,orient=VERTICAL)
sc1.place(x=10,y=20)
sc2 = Scale(pro,from_=1,to=100,orient=HORIZONTAL)
sc2.place(x=90,y=10)
################################
pro.mainloop()