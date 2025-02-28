from tkinter import *
from tkinter import messagebox
pro = Tk()
pro.geometry('500x500')
################################
def info():
    # messagebox.showinfo("program","hello azzoz")
    # messagebox.showwarning("program","here warning")
    # messagebox.showerror("program","here error")
    # messagebox.askokcancel("program","save?")
    # messagebox.askquestion("program","are you programmer?")  # = askyesno
    messagebox.askretrycancel("program","again?")


B1 = Button(pro,text="info",command=info)
B1.pack()
################################
pro.mainloop()