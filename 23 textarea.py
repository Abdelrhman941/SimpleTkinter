from tkinter import *
import tkinter as tk

pro = Tk()
pro.geometry('500x400')
################################
T = tk.Text(pro)
T.pack()

learn = """----- welcome -----
lets learn html
lets learn css
lets learn php
lets learn sql
python is very easy
----- write down -----
"""
T.insert(tk.END,learn)
################################
pro.mainloop()