from tkinter import *
################################
class TK:
    def __init__(self,pro):
        self.pro = pro
        self.pro.geometry('400x400')
        self.pro.title("My_program")

pro = Tk()
obj = TK(pro)
################################
pro.mainloop()