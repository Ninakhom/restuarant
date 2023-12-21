import tkinter as tk
from tkinter import messagebox
from ConectDB import connect, close_connection
import os

# Set up the connection and cursor
connection = connect()
cursor = connection.cursor()

# Set up the main window
frm = tk.Tk()
frm.geometry('700x500')
frm.title('Login Form')

# Function to handle login
def login():
    user = entry_username.get()
    password = entry_password.get()

    sql = "SELECT employee_id, first_name, last_name, job_title FROM employees WHERE user=%s AND password=%s"
    cursor.execute(sql, (user, password))
    user_info = cursor.fetchone()

    if user_info is None:
        messagebox.showinfo("Error", "Sorry, your username or password is incorrect")
    else:
        employee_id, first_name, last_name, job_title = user_info

        # Store user information globally for access in other parts of the program
        set_user_info(employee_id, first_name, last_name, job_title)
        user_author = job_title  # Replace this with your actual logic to determine the user's role
        
        

        frm.destroy()
        os.system(f"python dash.py {job_title}")
        messagebox.showinfo("Success", "Login successful")
        # Add your logic for what happens after a successful login here
        return user_author, job_title

def set_user_info(employee_id, first_name, last_name, job_title):
    global user_author
    user_author = job_title

def move_to_next(event):
    widget = event.widget
    widget.tk_focusNext().focus()

# Labels
label_username = tk.Label(frm, text='Username')
label_username.place(x=20, y=20)

label_password = tk.Label(frm, text='Password')
label_password.place(x=20, y=70)

# Entry widgets
entry_username = tk.Entry(frm, width=30)
entry_username.place(x=100, y=20)
entry_username.bind("<Down>", move_to_next)

entry_password = tk.Entry(frm, width=30, show='*')  # Use 'show' to hide the password
entry_password.place(x=100, y=70)
entry_password.bind("<Up>", move_to_next)


# Bind the Enter key to the password entry
entry_password.bind("<Return>", lambda event: login())

# Buttons
btn1 = tk.Button(frm, text='Login', width=20, command=login)
btn1.place(x=100, y=120)

btn2 = tk.Button(frm, text='Cancel', width=20, command=frm.destroy)
btn2.place(x=100, y=170)

frm.mainloop()
