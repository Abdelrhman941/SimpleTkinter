from tkinter import *
from tkinter import ttk
################################
class Student:
    def __init__(self,pro):
        self.pro = pro
        self.pro.geometry("1900x760+1+1")
        self.pro.title("School management program")
        self.pro.configure(background="silver")
        self.pro.resizable(TRUE,False)   # to control in max & min
        
        
        
        ####################### project name ############################
        title = Label(  self.pro, 
                        text="[ Student registration system ]",
                        bg="#67b0b5",
                        fg="white",
                        font=("monospace",15,"bold"))
        title.pack(fill=X)
        
        
        
        ####################### DataBase ############################
        # Call these variables inside the input fields :
        self.gender_var  = StringVar()
        self.id_var      = StringVar()
        self.name_var    = StringVar()
        self.email_var   = StringVar()
        self.phone_var   = StringVar()
        self.certif_var  = StringVar()
        self.address_var = StringVar()
        self.delete_var  = StringVar()
        self.search_var  = StringVar()
        ## now put it in his place by [ ]text variable inside Entry ]
        
        
        
        ####################### input data ##########################
        Manage_Frame = Frame(self.pro, bg="white")
        Manage_Frame.place(x=5,y=30,width=350,height=450)
        #-------------
        lbl_gender = Label(Manage_Frame,text="choose gender",bg="white",font="bold")
        lbl_gender.pack()
        combo_gender = ttk.Combobox(Manage_Frame,justify="center",textvariable=self.gender_var)
        combo_gender["value"] =("Male","Female")
        combo_gender.pack(fill=X)
        #-------------
        lbl_ID = Label(Manage_Frame,text="Serial number",bg="white",font="bold")
        lbl_ID.pack()
        ID_Entry = Entry(Manage_Frame,bd="2",font=10,textvariable=self.id_var)  # bd : to make boundaries
        ID_Entry.pack()
        #-------------
        lbl_name = Label(Manage_Frame,text="Student name",bg="white",font="bold")
        lbl_name.pack()
        name_Entry = Entry(Manage_Frame,bd="2",justify="left",font=10,textvariable=self.name_var) 
        name_Entry.pack()
        #-------------
        lbl_email = Label(Manage_Frame,text="Student e-mail",bg="white",font="bold")
        lbl_email.pack()
        email_Entry = Entry(Manage_Frame,bd="2",font=10,textvariable=self.email_var)
        email_Entry.pack()
        #-------------
        lbl_phone = Label(Manage_Frame,text="Student phone",bg="white",font="bold")
        lbl_phone.pack()
        phone_Entry = Entry(Manage_Frame,bd="2",font=10,textvariable=self.phone_var)
        phone_Entry.pack()
        #-------------
        lbl_certification = Label(Manage_Frame,text="certification",bg="white",font="bold")
        lbl_certification.pack()
        certification_Entry = Entry(Manage_Frame,bd="2",font=10,textvariable=self.certif_var)
        certification_Entry.pack()
        #-------------
        lbl_address = Label(Manage_Frame,text="Student address",bg="white",font="bold")
        lbl_address.pack()
        address_Entry = Entry(Manage_Frame,bd="2",font=10,textvariable=self.address_var)
        address_Entry.pack()
        #-------------
        lbl_delete = Label(Manage_Frame,text="Delete student",fg="red",bg="white",font="bold")
        lbl_delete.pack()
        delete_Entry = Entry(Manage_Frame,justify="center",bd="2",font=10,textvariable=self.delete_var)
        delete_Entry.pack()
        
        
        
        ####################### control panel ########################
        btn_frame = Frame(self.pro,bg="white")
        btn_frame.place(x=5,y=490,width=350,height=245)
        #-------------
        title1 = Label(btn_frame,text="control panel",fg="black",bg="#318b91",font=("Deco",14,"bold"))
        title1.pack(fill=X)
        #-------------
        add_btn = Button(btn_frame,text="add student",bg="#aed6f1",font="bold")
        add_btn.place(x=10,y=50,width=150,height=30)
        #-------------
        del_btn = Button(btn_frame,text="delete student",bg="#aed6f1",font="bold")
        del_btn.place(x=180,y=50,width=150,height=30)
        #-------------
        update_btn = Button(btn_frame,text="update student",bg="#aed6f1",font="bold")
        update_btn.place(x=10,y=105,width=150,height=30)
        #-------------
        clear_btn = Button(btn_frame,text="clear fields",bg="#aed6f1",font="bold")
        clear_btn.place(x=180,y=105,width=150,height=30)
        #-------------
        about_btn = Button(btn_frame,text="about",bg="#f7dc6f",font="bold")
        about_btn.place(x=10,y=190,width=150,height=30)
        #-------------
        exit_btn = Button(btn_frame,text="Exit",fg="white",bg="#873600",font="bold")
        exit_btn.place(x=180,y=190,width=150,height=30)
        
        
        
        ####################### Search ###########################
        search_frame = Frame(self.pro,bg="white")
        search_frame.place(x=360,y=31,width=1535,height=50)
        #-------------
        lbl_search  = Label(search_frame,text="Search for a student: ",bg="white",font="bold")
        lbl_search.place(x=10,y=12)
        #-------------
        combo_search = ttk.Combobox(search_frame,justify="center")
        combo_search["value"] =("id","name","email","phone","address")
        combo_search.place(x=200,y=15)
        #-------------
        search_Entry = Entry(search_frame,bd="2",textvariable=self.search_var)
        search_Entry.place(x=350,y=15)
        #-------------
        search_btn = Button(search_frame,text="Search",bg="#aab7b8")
        search_btn.place(x=490,y=12)
        
        
        
        ###################### table search ############################
        Details_frame = Frame(self.pro,bg="white",background="#d6dbdf")
        Details_frame.place(x=360,y=85,width=1535,height=650)
        #-------------
        Scroll_X = Scrollbar(Details_frame, orient=HORIZONTAL)
        Scroll_Y = Scrollbar(Details_frame, orient=VERTICAL)
        #-------------
        self.student_table = ttk.Treeview(  Details_frame,
                                            columns=("Id","Name","gender","e-mail","phone","address","certification"),
                                            xscrollcommand=Scroll_X.set,
                                            yscrollcommand=Scroll_Y.set  )
        self.student_table.place(x=6,y=4 ,width=1510,height=500)
        Scroll_X.pack(side=BOTTOM,fill=X)
        Scroll_Y.pack(side=RIGHT,fill=Y)
        Scroll_X.config(command=self.student_table.xview)
        Scroll_Y.config(command=self.student_table.yview)
        #-------------
        self.student_table["show"] = "headings"
        self.student_table.heading("Id",text="Id")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("gender",text="gender")
        self.student_table.heading("e-mail",text="e-mail")
        self.student_table.heading("phone",text="phone")
        self.student_table.heading("address",text="address")
        self.student_table.heading("certification",text="certification")
        
        ## to resize table columns size :
        self.student_table.column("Id",width=80)
        self.student_table.column("Name",width=150)
        self.student_table.column("gender",width=60)
        self.student_table.column("e-mail",width=170)
        self.student_table.column("phone",width=130)


pro = Tk()
obj = Student(pro)
################################
pro.mainloop()