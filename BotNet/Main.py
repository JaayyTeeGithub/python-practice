import smtplib
import ssl
from tkinter import Tk
from tkinter.filedialog import askopenfilename

smtp_server = "smtp.gmail.com"
port = 465
email = input("Enter your gmail address: ")
password = input("Enter password: ")
recipient = input(" Enter recipient's email: ")
print("Select plain text file to send.")
Tk().withdraw()
filename = askopenfilename()
subject = input("Enter subject of message: ")
message = "Subject: " + subject + "\n \n"

with open(filename) as file_object:
    for line in file_object:
        message = message + line

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(email, password)
    server.sendmail(email, recipient, message)

