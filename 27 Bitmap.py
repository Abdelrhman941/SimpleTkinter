from tkinter import *

pro = Tk()
pro.geometry('500x500')
################################
B1 = Button(pro,text="error",bitmap="error")
B1.pack()
B2 = Button(pro,text="hourglass",bitmap="hourglass")
B2.pack()
B3 = Button(pro,text="info",bitmap="info")
B3.pack()
B4 = Button(pro,text="warning",bitmap="warning")
B4.pack()
B5 = Button(pro,text="question",bitmap="question")
B5.pack()
B6 = Button(pro,text="gray12",bitmap="gray12")
B6.pack()
B7 = Button(pro,text="gray25",bitmap="gray25")
B7.pack()
B8 = Button(pro,text="gray50",bitmap="gray50")
B8.pack()
################################
pro.mainloop()
