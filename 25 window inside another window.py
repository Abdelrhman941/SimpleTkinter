from tkinter import *

pro = Tk()
pro.geometry('400x400')
################################
def pro1():
    pro1 = Tk()
    pro1.geometry('200x200')
    btn = Button(pro1, text="exit",command=pro1.quit)
    btn.pack()
    pro1.mainloop()

btn = Button(pro, text="My_program",command=pro1)
btn.pack()
################################
pro.mainloop()