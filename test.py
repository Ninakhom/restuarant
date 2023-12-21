import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ConectDB import connect, close_connection
import mysql.connector as mysql

class MainForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('800x400')
        self.title('Menu-Items')

        # Create a menu bar
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        # Create a Management menu with "Employee Management" item
        management_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Management", menu=management_menu)
        management_menu.add_command(label="Employee Management", command=self.open_employee_management)

        # Create an Edit menu with a "Click Me" item
        self.edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Click Me", command=self.on_menu_click)

        # Dictionary to store frames
        self.frames = {}

        # For demonstration purposes, set the job title to "chef"
        self.job_title = "chef"

        # Check job title and show/hide "Edit" menu
        self.update_edit_menu()

    def open_employee_management(self):
        # Check user role before opening the form
        user_role = get_user_role()  # Implement a function to get the user's role from the database
        if user_role == "employee":
            messagebox.showinfo("Access Denied", "You don't have permission to access Employee Management.")
        else:
            # Check if the frame already exists
            if "employee_management" not in self.frames:
                # Create a new frame for Employee Management
                frame = tk.Frame(self)
                self.frames["employee_management"] = frame
                frame.pack(fill=tk.BOTH, expand=True)

                # Add title to the frame
                title_label = tk.Label(frame, text="Employee Management Form", font=("Helvetica", 16, "bold"))
                title_label.pack(pady=20)

                # Add widgets/content to the frame (you can replace this with your form content)
                # Example: label = tk.Label(frame, text="Employee Details:")
                # label.pack(pady=10)

            # Hide other frames
            self.hide_frames("employee_management")

    def on_menu_click(self):
        messagebox.showinfo("Menu Clicked", "Menu item clicked!")

    def hide_frames(self, current_frame):
        # Hide all frames except the specified one
        for frame_name, frame in self.frames.items():
            if frame_name != current_frame:
                frame.pack_forget()

    def update_edit_menu(self):
        # Check job title and show/hide "Edit" menu
        if self.job_title == "chef":
            self.edit_menu.entryconfig("Click Me", state="normal")
        else:
            self.edit_menu.entryconfig("Click Me", state="disabled")

def get_user_role():
    # Implement a function to get the user's role from the database
    # For demonstration purposes, return "employee" for now
    return "employee"

if __name__ == "__main__":
    app = MainForm()
    app.mainloop()
