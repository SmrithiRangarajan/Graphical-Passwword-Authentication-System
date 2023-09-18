from tkinter import *
from tkinter import font
import custom_button
import segments
import email_ver


def load_email_ver(window, menu_frame):
    win.destroy()
    email_ver.start()

def start(win):
    win.geometry("600x600")
    win.title("Graphical Password Authentication System")
   
    menu_frame = Frame(win, height=600, width=1280, bg = "white")
    menu_frame.pack(fill='both', expand=1)

    label = Label(menu_frame, text="Graphical Password Authentication System", font=('Freestyle Script', 35))
    label.pack(padx=40, pady=30)

    btn_height = 100
    btn_width = 450
    btn_font = ('Trebuchet MS', 20)


    btn1 = custom_button.TkinterCustomButton(master=menu_frame, text="Login", text_font=50,
                                             height=40, width=70, corner_radius=10,
                                             command=lambda: load_email_ver(win, menu_frame)).place(relx=0.5,
                                                                                                    rely=0.5,
                                                                                                    anchor=CENTER)



    win.mainloop()


if __name__ == "__main__":
    win = Tk()
    start(win)
