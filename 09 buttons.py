from tkinter import *
pro = Tk()
pro.geometry('800x500')

fr1 = Frame(width='390', height='499',background='red')
fr1.place(x=1,y=1) 
fr2 = Frame(width='390', height='499',background='blue')
fr2.place(x=393,y=1) 
################################
## variable = tool(master,option) :
# 1) master >> مكان وضع الزر
# 2) option >> خصائص التحكم بالزر
#    --> text   >> Button name
#    --> fg     >> txt color
#    --> bg     >> background color
#    --> font   >> txt size
#    --> cursor >> شكل موشر الفارة
#    --> width - heigh
bt1 = Button(fr1,text="button1",fg="blue",bg="white",font=20,
            cursor="heart",width=30,height=5)
bt1.place(x=10,y=10)   # button place by fr1

bt2 = Button(fr2,text="button2",fg="red",bg="white",font=20,
            cursor="arrow",width=30,height=5)
bt2.place(x=10,y=10)   # button place by fr2
################################
pro.mainloop()