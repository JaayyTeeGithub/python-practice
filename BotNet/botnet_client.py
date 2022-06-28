'''
Creator: Jeremy Thomas

Will receive the recipient's email, the sender's email, and the sender's email password and send a text file using SMTP.
'''

import smtplib
import ssl
from socket import *
import sys
import os

server_ip = '127.0.0.1'
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.sendto("###IAMWILLING###".encode(), (server_ip, server_port))
info_str, server_address = client_socket.recvfrom(2048)
info = info_str.decode().split("#")
print("Sending email to the address " + info[2] + " from " + info[0] + ".")
client_socket.close()

smtp_server = "smtp.gmail.com"
smtp_port = 465
message = "Subject: botnet \n \n"

with open(os.path.join(sys.path[0], "dummyfile.txt"), "r") as file_object:
    for line in file_object:
        message = message + line

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", smtp_port, context=context) as server:
    server.login(info[0], info[1])
    server.sendmail(info[0], info[2], message)
print("Done.")

