from tkinter import *
pro = Tk()
pro.geometry('800x500')
################################
fr1 = Frame(width='390', height='499',background='red') # background=''  =>  bg=''
fr1.place(x=50,y=50)    # you show write it line to make Frame tool work
                        # x: take distance from left
                        # y: take distance from up

# fr1.place(x=100,y=20) # run this kline to know the difference

fr2 = Frame(width='390', height='499',background='blue')
fr2.place(x=369,y=50)    # x !=1 because fr1 from left _1_ to right 1+390 = _391_
################################
pro.mainloop()
