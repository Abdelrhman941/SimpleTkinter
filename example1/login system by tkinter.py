from tkinter import *

pro = Tk()

# --- set title ---
pro.title("Login system")
# --- put size of window ---
pro.geometry("500x500")
# --- control min & max window ---
pro. resizable(False,False)
# --- set bg ---
pro.config(background="#bfc9ca")
# --- change logo ---
pro.iconbitmap(r"P:\1-python\# GUI #\tkinter\example1\lock.ico")
# --- write txt ---
title = Label(pro , text="Login System" , font=("courier",15,"bold") , bg="black" , fg="white")
title.pack(fill=X)      # fill=X  > to fill all line by Properties as bg = black
# --- frame ---
fr1 = Frame(pro , width="300",height="350", bg="whitesmoke")
fr1.pack(pady=30)       # pady=   > to move away from y
# --- image ---
photo = PhotoImage(file=r"P:\1-python\# GUI #\tkinter\example1\lock.png")
res = photo.subsample(5,5)      # to resize photo
panel = Label(pro, image=res)
panel.place(x=200,y=60)
# --- Label ---
lbl1 = Label(fr1, text="username : ",font=("courier",15),bg="whitesmoke")
lbl1.place(x=10,y=140)
lbl2 = Label(fr1, text="password : ",font=("courier",15),bg="whitesmoke")
lbl2.place(x=10,y=180)
# --- Entry ---
en1 = Entry(fr1)
en1.place(x=135,y=145)
en2 = Entry(fr1)
en2.place(x=135,y=185)
# --- buttons ---
bt1 = Button(fr1, text="Login" , font=("courier",15,"italic"), bg="#a9cce3",width=11)
bt1.place(x=1,y=260)
bt2 = Button(fr1, text="SignUp", font=("courier",15,"italic"), bg="#eb984e",width=12)
bt2.place(x=144,y=260)
# --- checkbox ---
c1 = Checkbutton(fr1, text="forget password ?",font=("courier",15),bg="whitesmoke")
c1.place(x=40,y=220)
pw = Label(fr1, text="Developed by Abdelrhman",font=("courier",9))
pw.place(x=130,y=325)

pro.mainloop()