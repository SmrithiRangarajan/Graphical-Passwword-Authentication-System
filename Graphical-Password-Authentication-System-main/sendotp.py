import math as m
import random as r
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from tkinter import messagebox
from tkinter import ttk
import grid


def check(t, otp) :
    if(t == otp) :
        messagebox.showinfo("successfully verified!")
    else :

      messagebox.showinfo("error!")

    
def genalphaOTP(): 
    string1 = '12345'
    string2 = 'ABCD'
    OTP1 = ""
    OTP2 = ""
    l1 = len(string1)
    l2 = len(string2)
    for i in range(1) : 
        OTP1 += string1[m.floor(r.random() * l1)]
        OTP2 += string2[m.floor(r.random() * l2)]
        OTP3 = OTP2+OTP1
  
    return (OTP3) 


def gennumOTP():     
    string = '1234'
    OTP = ""
    l = len(string)
    for i in range(4) :
        OTP += string[m.floor(r.random() * l)] 
  
    return (OTP) 

def sendnum(email):
        
        message = MIMEMultipart()

        message["from"] = "ipl project"

        message["to"] = email.get()

        message["subject"] = "OTP"

        otp = gennumOTP()
        print("opt = ", otp)


        message.attach(MIMEText("Your One Time Password is : " ))
        message.attach(MIMEText(otp))
        

        with smtplib.SMTP(host= "smtp.gmail.com", port=587) as smtp:
            try:
                smtp.ehlo()
                smtp.starttls()
                smtp.login("iplprjct@gmail.com","sodslypzrtjvshnt")
                smtp.send_message(message)
                print("message sent!")
            except:
                print("exception occurred")

def sendalpha(email):
        global otp
        
        message = MIMEMultipart()

        message["from"] = "ipl project"

        message["to"] = email.get()

        message["subject"] = "OTP"

        otp = genalphaOTP()
        print("opt = ", otp)

        #link = path2url(path)

        message.attach(MIMEText("Your One Time Password is : " ))
        message.attach(MIMEText(otp))
        

        with smtplib.SMTP(host= "smtp.gmail.com", port=587) as smtp:
            try:
                smtp.ehlo()
                smtp.starttls()
                smtp.login("iplprjct@gmail.com","sodslypzrtjvshnt")
                smtp.send_message(message)
                print("message received")
            except:
                print("exception occurred")


