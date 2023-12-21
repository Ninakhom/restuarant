import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import mysql.connector as mysql
from ConectDB import connect, close_connection
import os
def insert_employee():
    fname = entry_first_name.get()
    lname = entry_last_name.get()
    job = val_major.get()
    user = entry_username.get()
    passs = entry_password.get()

    connection = connect()

    if connection:
        try:
            cursor = connection.cursor()

            # SQL query to insert an employee
            sql_query = "INSERT INTO employees (first_name, last_name, job_title, user, password) VALUES (%s, %s, %s, %s, %s)"
            values = (fname, lname, job, user, passs)

            # Execute the query
            cursor.execute(sql_query, values)

            # Commit the changes to the database
            connection.commit()

            messagebox.showinfo("Success", "Employee information inserted successfully!")
            show_employees()

        except mysql.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()

            close_connection(connection)

def show_employees():
    connection = connect()

    if connection:
        try:
            cursor = connection.cursor()

            # SQL query to select all employees
            sql_query = "SELECT employee_id, first_name, last_name, job_title FROM employees"
            cursor.execute(sql_query)

            # Clear existing items in the TreeView
            for row in treeview.get_children():
                treeview.delete(row)

            # Insert new items into the TreeView
            for row in cursor.fetchall():
                treeview.insert("", "end", values=row)

        except mysql.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()

            close_connection(connection)
def cancel():
    frm.destroy()
    os.system("python dash.py")

    
# GUI setup
frm = tk.Tk()
frm.geometry("1500x1000")
frm.title("Employee Information")

# Entry widgets for employee details
label_first_name = tk.Label(frm, text="First Name:")
label_first_name.grid(row=0, column=0, padx=10, pady=10)
entry_first_name = tk.Entry(frm)
entry_first_name.grid(row=0, column=1, padx=10, pady=10)

label_last_name = tk.Label(frm, text="Last Name:")
label_last_name.grid(row=1, column=0, padx=10, pady=10)
entry_last_name = tk.Entry(frm)
entry_last_name.grid(row=1, column=1, padx=10, pady=10)

label_job_title = tk.Label(frm, text="Job Title:")
label_job_title.grid(row=2, column=0, padx=10, pady=10)

val_major = tk.StringVar()
cbb=ttk.Combobox(frm,textvariable=val_major,state='readonly')
cbb.place(x=150,y=100)
cbb.config(font=("Times New Roman",16))
cbb['values'] = ('Admin', 'Casheir', 'Chef',)

label_username = tk.Label(frm, text="Username:")
label_username.grid(row=3, column=0, padx=10, pady=10)
entry_username = tk.Entry(frm)
entry_username.grid(row=3, column=1, padx=10, pady=10)

label_password = tk.Label(frm, text="Password:")
label_password.grid(row=4, column=0, padx=10, pady=10)
entry_password = tk.Entry(frm)
entry_password.grid(row=4, column=1, padx=10, pady=10)

# Button to insert employee information
button_insert_employee = tk.Button(frm, text="Insert Employee", command=insert_employee)
button_insert_employee.grid(row=5, column=0, columnspan=2, pady=10)

button_cancel = tk.Button(frm, text="Cancel", command=cancel)
button_cancel.grid(row=10, column=0, columnspan=2, pady=10)

# TreeView to display employee information
treeview_columns = ("Employee ID", "First Name", "Last Name", "Job Title")
treeview = ttk.Treeview(frm, columns=treeview_columns, show="headings")
treeview.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

# Configure column headings
for col in treeview_columns:
    treeview.heading(col, text=col)
    treeview.column(col, width=100)

# Button to refresh employee information in TreeView
button_refresh_employees = tk.Button(frm, text="Refresh Employees", command=show_employees)
button_refresh_employees.grid(row=7, column=0, columnspan=2, pady=10)

# Show initial employee information
show_employees()

frm.mainloop()
