from tkinter import *
pro1 = Tk()
pro2 = Tk()
################################
pro1.title('window1')
pro2.title('window2')
################################
pro1.geometry('300x300+10+10')
pro2.geometry('200x200+320+10')
################################
pro1.configure(background="red")
pro2.configure(background="blue")
################################
pro1.mainloop()
# pro2.mainloop()   # you can write this line or no , no problem