import tkinter as tk
from tkinter import messagebox
import os

# Assume user_author is set during the login process
user_author = "chef"

def open_employee_management():
    messagebox.showinfo("Access Granted", "You have access to Employee Management.")

def open_menuitems_management():
    messagebox.showinfo("Access Granted", "You have access to Menuitems Management.")

def on_exit():
    frm1.destroy()

def hide_menu_items():
    # Hide or disable menu items based on user_author
    if user_author == "chef":
        management_menu.entryconfigure("Employee Management", state='disabled')
        management_menu.entryconfigure("Menuitems Management", state='disabled')
        edit_menu.entryconfigure("Order",state='normal')
    

frm1 = tk.Tk()
frm1.geometry('1500x1000')
frm1.title('Tool Strip Example')

menu_bar = tk.Menu(frm1)
frm1.config(menu=menu_bar)

management_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Management", menu=management_menu)
management_menu.add_command(label="Employee Management", command=open_employee_management)
management_menu.add_command(label="Menuitems Management", command=open_menuitems_management)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Chef", menu=edit_menu)
edit_menu.add_command(label="Order", command=lambda: messagebox.showinfo("Click Me", "You clicked the 'Click Me' menu item."))

# Assume user_author is set based on the login process
user_author = "chef"

# Hide or disable menu items based on user_author
hide_menu_items()

frm1.mainloop()
