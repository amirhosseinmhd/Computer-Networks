import socket

def send_message():
    # to whom you want to send
    print(client.recv(1024).decode())

    # fining the Right Guy
    while True:
        user_input = input()
        client.send(user_input.encode())
        flag = client.recv(1024).decode()
        print(flag)
        if flag == "Accepted":
            break
        else:
            print(flag)
    # Right Guy was found
    #What do you want to say?
    print(client.recv(1024).decode())
    message = input()
    client.send(message.encode())
    #Message sent



def user_op():
    while True:
        print(client.recv(1024).decode())
        # User Telling Client what he wants.
        user_input = input()
        client.send(user_input.encode())
        if user_input == '1':
            list_of_client = client.recv(1024).decode()
            print(list_of_client)
        elif user_input == '2':
           send_message()
        elif user_input == '3':
            print(client.recv(1024).decode())



client = socket.socket()
port = 9000
client.connect(('127.0.0.1', port))
# Greeting
print(client.recv(1024).decode())
# user Telling His name
user_input = input()
client.send(user_input.encode())
# he told his name, Now he want to do more
user_op()