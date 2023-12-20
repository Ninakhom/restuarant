#import 
import tkinter  as Tk




#setup from
frm = Tk.Tk()
frm.title("Obee Resturant")
frm.geometry("1000x800")
frm.config(bg = "#008000")

#GUI
lb_wel = Tk.Label(text="Welcome To Obee Resturant" ,fg = "White")
lb_wel.place( x = "10" , y = "20")

frm.mainloop()