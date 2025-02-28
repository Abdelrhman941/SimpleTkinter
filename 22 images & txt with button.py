from tkinter import *
from tkinter import ttk

pro = Tk()
pro.geometry('500x400')
################################
photo = PhotoImage(file=r'C:\Users\Al-arab\Desktop\spyder.png')

res = photo.subsample(2,2)               # to resize photo
bt = Button(pro, text="spyder program",
            image=res , compound=LEFT)   # compound => to put image where by txt   [TOP - BOTTOM - LEFT - RIGHT]
bt.pack()
################################
pro.mainloop()