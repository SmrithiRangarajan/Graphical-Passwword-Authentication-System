from tkinter import messagebox
import custom_button
import tkinter
from tkinter import ttk
from tkinter import *
from functools import partial

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import sendotp



def validateLogin(username, email):
	print("username entered :", username.get())
	print("email entered :", email.get())
	authenticate(username, email)
	vercode(email)
	return

def start() :
        tkWindow = tkinter.Tk()  
        tkWindow.geometry('600x600')
     
        tkWindow.title('Tkinter Login Form - pythonexamples.org')
        usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
        username = StringVar()
        usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1, sticky='NSEW')
       

        emailLabel = Label(tkWindow,text="Email").grid(row=1, column=0)  
        email = StringVar()
        emailEntry = Entry(tkWindow, textvariable=email).grid(row=1, column=1)
        
       

        def load_otp(email):
                sendotp.sendalpha(email)
                
                grid()

        
        loginButton = custom_button.TkinterCustomButton(master=tkWindow, text="Log In", height=40, corner_radius=10,
        command=lambda: validateLogin(username, email)).place(relx=0.3, rely=0.7, anchor=CENTER)

        otpButton = custom_button.TkinterCustomButton(master=tkWindow, text="Generate OTP", height=40, corner_radius=30,
        command=lambda: load_otp(email)).place(relx=0.7, rely=0.7, anchor=CENTER)


        tkWindow.mainloop()



        
def authenticate(username , email):
        filepath1 = "creds.txt"
        filepath2 = "creds_email.txt"
        f1 = open(filepath1 , "r")
        f2 = open(filepath2 , "r")
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        for i in range (len(lines1)):
            spl = lines1[i].split(" ")
            spl1 = lines2[i].split(" ")
            if spl[i] == username.get():
                if spl1[i] == email.get():
                    print("details authenticated!")
                    messagebox.showinfo("Login Page", "authenticated!!Please check your email")
                    break
                else:
                    print("invalid email")
                    messagebox.showinfo("Login Page", "incorrect email")
                    break
            else:
                print("invalid username")
                messagebox.showinfo("Login Page", "incorrect username!")
                break

def vercode(email):
        
        message = MIMEMultipart()

        message["from"] = "ipl project"

        message["to"] = email.get()

        message["subject"] = "verification link"

        #link = path2url(path)

        message.attach(MIMEText("verified!"))

        with smtplib.SMTP(host= "smtp.gmail.com", port=587) as smtp:
            try:
                smtp.ehlo()
                smtp.starttls()
                smtp.login("iplprjct@gmail.com","sodslypzrtjvshnt")
                smtp.send_message(message)
                print("message sent!")
            except:
                print("exception occurred")



def grid() :

    def clicked(b):
        global t
        t = b.cget('text')
        print(t)

   

        sendotp.check(t, sendotp.otp)
        
    master=tkinter.Tk()
    master.title("grid() method")
  
    master.geometry("600x600")

        
    btn1 = PhotoImage(file = '1,1.png')
    l1 = Label(image = btn1)
   

    A1=ttk.Button(master,text="A1",image = btn1, command=lambda : clicked(A1))
    A1.grid(row=1,column=1)
   
    btn2 = PhotoImage(file = '1,2.png')
    l2 = Label(image = btn2)
    
    A2=ttk.Button(master,text="A2",image = btn2, command=lambda : clicked(A2))
    A2.grid(row=1,column=2)

    

    btn3 = PhotoImage(file = '1,3.png')
    l3 = Label(image = btn3)
    A3=ttk.Button(master,text="A3", image = btn3,command=lambda : clicked(A3))
    A3.grid(row=1,column=3)
    
    btn4 = PhotoImage(file = '1,4.png')
    l4 = Label(image = btn4)
    A4=ttk.Button(master,text="A4", image = btn4,command=lambda : clicked(A4))
    A4.grid(row=1,column=4)


    btn5 = PhotoImage(file = '1,5.png')
    l5 = Label(image = btn5)
    A5=ttk.Button(master, text="A5", image = btn5,command=lambda : clicked(A5))
    A5.grid(row=1,column=5)
   

    btn6 = PhotoImage(file = '2,1.png')
    l6 = Label(image = btn6)
    B1=ttk.Button(master,text="B1",image = btn6,command=lambda : clicked(B1))
    B1.grid(row=2,column=1)

    btn7 = PhotoImage(file = '2,2.png')
    l7 = Label(image = btn7)
    B2=ttk.Button(master,text="B2",image = btn7,command=lambda : clicked(B2))
    B2.grid(row=2,column=2)

    btn8 = PhotoImage(file = '2,3.png')
    l8 = Label(image = btn8)
    B3=ttk.Button(master,text="B3",image = btn8,command=lambda : clicked(B3))
    B3.grid(row=2,column=3)

    btn9 = PhotoImage(file = '2,4.png')
    l9 = Label(image = btn9)
    B4=ttk.Button(master,text="B4",image = btn9,command=lambda : clicked(B4))
    B4.grid(row=2,column=4)

    btn10 = PhotoImage(file = '2,5.png')
    l10 = Label(image = btn10)
    B5=ttk.Button(master,text="B5", image = btn10,command=lambda : clicked(B5))
    B5.grid(row=2,column=5)

    btn11 = PhotoImage(file = '3,1.png')
    l11 = Label(image = btn11)
    C1=ttk.Button(master,text="C1",image = btn11,command=lambda : clicked(C1))
    C1.grid(row=3,column=1)

    btn12 = PhotoImage(file = '3,2.png')
    l12 = Label(image = btn12)
    C2=ttk.Button(master,text="C2",image = btn12,command=lambda : clicked(C2))
    C2.grid(row=3,column=2)

    btn13 = PhotoImage(file = '3,3.png')
    l13 = Label(image = btn13)
    C3=ttk.Button(master,text="C3",image = btn13,command=lambda : clicked(C3))
    C3.grid(row=3,column=3)

    btn14 = PhotoImage(file = '3,4.png')
    l14 = Label(image = btn14)
    C4=ttk.Button(master,text="C4",image = btn14,command=lambda : clicked(C4))
    C4.grid(row=3,column=4)

    btn15 = PhotoImage(file = '3,5.png')
    l15 = Label(image = btn15)
    C5=ttk.Button(master,text="C5",image = btn15,command=lambda : clicked(C5))
    C5.grid(row=3,column=5)

    btn16 = PhotoImage(file = '4,1.png')
    l16 = Label(image = btn16)
    D1=ttk.Button(master,text="D1", image = btn16,command=lambda : clicked(D1))
    D1.grid(row=4,column=1)

    btn17 = PhotoImage(file = '4,2.png')
    l17 = Label(image = btn17)
    D2=ttk.Button(master,text="D2",image = btn17,command=lambda : clicked(D2))
    D2.grid(row=4,column=2)

    btn18 = PhotoImage(file = '4,3.png')
    l18 = Label(image = btn18)
    D3=ttk.Button(master, text="D3",image = btn18,command=lambda : clicked(D3))
    D3.grid(row=4,column=3)

    btn19 = PhotoImage(file = '4,4.png')
    l19 = Label(image = btn19)
    D4=ttk.Button(master,text="D4",image = btn19,command=lambda : clicked(D4))
    D4.grid(row=4,column=4)

    btn20 = PhotoImage(file = '4,5.png')
    l20 = Label(image = btn20)
    D5=ttk.Button(master,text="D5",image = btn20,command=lambda : clicked(D5))
    D5.grid(row=4,column=5)


    
    col_labels = [ttk.Label(master, text="{}".format(i)) for i in range(1,6)]

    labels = ["A", "B", "C", "D"]
    for i, label_text in enumerate(labels):
        label =ttk.Label(master, text=label_text)
        label.grid(row=i+1, column=0)


    for i, label in enumerate(col_labels):
        label.grid(row=0, column=i+1)

   
                

    master.mainloop()

        

start()



