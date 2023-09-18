from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define a function to show the popup message
def show_msg():
   
   #print(btn)
   messagebox.showinfo("clicked")
   #return btn

# Add an optional Label widget
Label(win, text= "Welcome Folks!", font= ('Aerial 17 bold italic')).pack(pady= 30)

# Create a Button to display the message
b = 'A1'
btn1 = ttk.Button(win, text= "Click Here", command=show_msg).pack(pady= 20)

win.mainloop()
