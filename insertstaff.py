import tkinter 
from tkinter import ttk
import tkinter.messagebox as messagebox
import mysql.connector as mysql
from ConectDB import connect, close_connection


frm = tkinter.Tk()
frm.geometry("1000x600")
frm.title("Staff-Management")

lb_first=tkinter.Label(frm,text="Firstname :")
lb_first.place(x=20,y=30)
lb_first.config(font=("Times New Roman",15))

txt_first=tkinter.Entry(frm)
txt_first.place(x=130,y=30)
txt_first.config(font=('Times New Roman',15))


lb_last=tkinter.Label(frm,text="Lastname :")
lb_last.place(x=20,y=70)
lb_last.config(font=("Times New Roman",15))

txt_last=tkinter.Entry(frm)
txt_last.place(x=130,y=70)
txt_last.config(font=('Times New Roman',15))

lb_job=tkinter.Label(frm,text="Job :")
lb_job.place(x=20,y=110)
lb_job.config(font=("Times New Roman",15))

txt_job=tkinter.Entry(frm)
txt_job.place(x=130,y=110)
txt_job.config(font=('Times New Roman',15))


lbuser=tkinter.Label(frm,text="User :")
lbuser.place(x=20,y=150)
lbuser.config(font=("Times New Roman",15))

txt_user=tkinter.Entry(frm)
txt_user.place(x=130,y=150)
txt_user.config(font=('Times New Roman',15))

lbpass=tkinter.Label(frm,text="Password :")
lbpass.place(x=20,y=190)
lbpass.config(font=("Times New Roman",15))

txt_pass=tkinter.Entry(frm)
txt_pass.place(x=130,y=190)
txt_pass.config(font=('Times New Roman',15))

btnadd=tkinter.Button(frm,text="ADD",width=7,)
btnadd.place(x=20,y=230)
btnadd.config(font=('Time New Roman',15))

btnDel=tkinter.Button(frm,text="Delete",width=7,command=quit)
btnDel.place(x=130,y=230)
btnDel.config(font=('Time New Roman',15))

btnedit=tkinter.Button(frm,text="Update",width=7,)
btnedit.place(x=240,y=230)
btnedit.config(font=('Time New Roman',15))



frm.mainloop()
