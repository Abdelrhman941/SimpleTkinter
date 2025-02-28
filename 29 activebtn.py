from tkinter import *

pro = Tk()
pro.geometry('500x500')
################################
bt1 = Button(pro,text="button 1")
bt1.pack()

bt2 = Button(pro,text="button 2",activebackground="black",activeforeground="white")
bt2.pack()

bt3 = Button(pro,text="button 3",activebackground="red",activeforeground="white")
bt3.pack()
################################
pro.mainloop()