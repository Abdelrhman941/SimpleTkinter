from tkinter import *
pro = Tk()
pro.geometry('800x500')

fr1 = Frame(width='390', height='499',background='red')
fr1.place(x=1,y=1) 
fr2 = Frame(width='390', height='499',background='blue')
fr2.place(x=393,y=1) 
################################
input1  = Entry(fr1)                    # write from left
input1.place(x=10,y=100)

input2  = Entry(fr1,justify="center")   # write from center
input2.place(x=10,y=140)

input3  = Entry(fr1,justify="center",fg='red',bg='yellow')
input3.place(x=10,y=180)

input4  = Entry(fr1,justify="center",fg='red',bg='yellow',font=10)
input4.place(x=10,y=220)

input1_1  = Entry(fr2)
input1_1.place(x=10,y=100)
################################
pro.mainloop()