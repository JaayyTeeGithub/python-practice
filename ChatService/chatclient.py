from socket import *
from select import *
from string import *
from sys import *


def get_input():
    stdout.write("You: ")
    stdout.flush()


host = "127.0.0.1"
port = 12000
client_nickname = input("What is your nickname?")

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((host, port))

print("Connected to chat!")
get_input()

while True:
    client_list = [stdin, client_socket]
    read, write, error = select(client_list, [], [])
    for client in client_list:
        if client == client_socket:
            message = client.recv(4096)
            if not message:
                print("Disconnected from chat server!")
                exit()
            else:
                received_message = client_socket.recv(1024).decode()
                if received_message == "ACTIVATEPROTOCOL:GIMMENICKNAME":
                    client_socket.send(client_nickname.encode())
                else:
                    stdout.write(message.decode())
                    get_input()
        else:
            message = stdin.readline()
            client_socket.send(message.encode())
            get_input()