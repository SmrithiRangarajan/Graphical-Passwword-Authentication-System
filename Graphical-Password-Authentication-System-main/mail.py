from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()

message["from"] = "ipl project"

message["to"] = "smrithirangaraajan@gmail.com"

message["subject"] = "this is a message"

message.attach(MIMEText("body"))

with smtplib.SMTP(host= "smtp.gmail.com", port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("iplprjct@gmail.com","sodslypzrtjvshnt")
        smtp.send_message(message)
        print("message sent!")
    except:
        print("exception occurred")
