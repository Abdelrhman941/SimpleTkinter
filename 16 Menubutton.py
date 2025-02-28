from tkinter import *

pro = Tk()
pro.geometry('600x400')
################################
mn  = Menubutton(pro,text="Learn "  ,relief="groove")    # relief الحواف
mn.place(x=10,y=20)

ss = Menu(mn,tearoff=0)  # to show menu inside button & tearoff=0 to remove ---
mn['menu'] = ss
ss.add_checkbutton(label='html')
ss.add_checkbutton(label='css')
ss.add_checkbutton(label='python')
################################
pro.mainloop()