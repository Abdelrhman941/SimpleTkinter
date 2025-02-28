from tkinter import *

pro = Tk()
pro.geometry('600x400')
################################
menubar = Menu(pro)
f = Menu(menubar,tearoff=0)
f.add_command(label="new")
f.add_command(label="open")
f.add_separator()
f.add_command(label="save")
f.add_command(label="save as")
f.add_separator()
f.add_command(label="Exit",command=pro.quit)    # command=pro.quit >> to exit from file

menubar.add_cascade(label='File',menu=f)   # to add on menubar
pro.config(menu=menubar)    # to launch the command
################################
pro.mainloop()
