import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#settup from
frm = tk.Tk()
frm.geometry('700x500')
frm.title('Login Form')

#label
label_username = tk.Label(frm, text='Username')
label_username.place(x=20, y=20)

label_password = tk.Label(frm, text='Password')
label_password.place(x=20, y=70)

#entry
entry_username = tk.Entry(frm, width=30)
entry_username.place(x=100, y=20)

entry_password = tk.Entry(frm, width=30)
entry_password.place(x=100, y=70)

#button
btn1 = tk.Button(frm, text='Login', width=20, command="Login()")
btn1.place(x=100, y=120)

btn2 = tk.Button(frm, text='Cancel', width=20, command= "frm.destroy()")
btn2.place(x=100, y=170)

#combobox
cb1 = ttk.Combobox(frm, values=['chef', 'waiter' ,'cashier'])
cb1.place(x=100, y=220)


#function

def Login():
    username = entry_username.get()
    password = entry_password.get()

    if username == 'admin' and password == 'admin':
        messagebox.showinfo('Login info', 'Login successful')
    else:
        messagebox.showinfo('Login info', 'Login failed')

frm.mainloop()