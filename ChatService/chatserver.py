from socket import *
from select import *


def broadcast_message(sender_socket, data):
    for client in conn_list:
        if client != server_socket and client != sender_socket:
            try:
                client.send(data)
            except:
                client.close()
                conn_list.remove(client)


def get_nickname(nick_list, peer_name):
    for nickname in nick_list:
        if nickname[1] == peer_name:
            sender_nickname = nickname[0]
            return str(sender_nickname)


conn_list = []
nickname_list = []
server_port = 12000
server_ip = "127.0.0.1"
wiggle = 4096
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen()
conn_list.append(server_socket)
print("Chat server is good!")
print("Started on port " + str(server_port) + ".")

while True:
    read, write, error = select(conn_list, [], [])
    for conn in read:
        if conn == server_socket:
            client, address = server_socket.accept()
            conn_list.append(client)
            print(str(client) + " has connected.")
            print("IP: " + str(address))
            client.send("ACTIVATEPROTOCOL:GIMMENICKNAME".encode())
            client_nickname = client.recv(1024).decode()
            nickname_list.append((client_nickname, str(conn.getpeername())))
            print("Nickname: " + client_nickname)
            broadcast_message(client_nickname + " has joined the chat!")
            client.send("Connected to chat server!".encode())
            broadcast_message(conn, get_nickname(nickname_list, str(conn.getpeername())) + " has connected.")
        else:
            try:
                message = conn.recv(wiggle).decode()
                if message:
                    broadcast_message(conn, get_nickname(nickname_list, str(conn.getpeername())) + ": " + message)
            except:
                broadcast_message(conn, get_nickname(nickname_list, str(conn.getpeername())) + " has disconnected.")
                print(str(conn.getpeername()) + " is offline.")
                conn.close()
                conn_list.remove(conn)
                continue


server_socket.close()







