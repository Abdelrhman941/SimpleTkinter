from tkinter import *
pro = Tk()
pro.geometry('800x500')

fr1 = Frame(width='390', height='499',background='red')
fr1.place(x=1,y=1) 
fr2 = Frame(width='390', height='499',background='blue')
fr2.place(x=393,y=1) 

bt1 = Button(fr1,text="button1",fg="blue",bg="white",cursor="heart")
bt1.place(x=10,y=10)   # button place
bt2 = Button(fr2,text="button2",fg="red",bg="white")
bt2.place(x=10,y=10)   # button place by fr2
################################
## Label >> to create txt
lbl = Label(fr1,text='hello;',fg="black",bg='red',font=20)
lbl.place(x=10,y=40)
lb2 = Label(fr2,text='Python;',fg="black",bg='blue',font=20)
lb2.place(x=10,y=40)
################################
pro.mainloop()