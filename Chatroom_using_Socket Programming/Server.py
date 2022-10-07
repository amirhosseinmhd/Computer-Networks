import socket
from _thread import *


def mess_buffer(buffer, name, message, reciver):
    buffer.append(reciver + "* Message from: " + name + "\n" + message)


# each message has index in message buffer this function find that
def recive_message_index(msg_buffer_arg, client):
    j = 0
    index = []
    for i in msg_buffer_arg:
        if i == '*':
            index.append(j)
            j = j + 1
            continue
        j = j + 1
    rec = msg_buffer_arg[0:index[0]]
    if rec == client:
        return True
    else:
        return False


def recive_messages(list_of_clients, bufferd_message):
    end = len(list_of_clients) - 1
    client = list_of_clients[end]
    j = 0
    tru_mess_ind = []
    for i in bufferd_message:
        # Behesh msg buffer ro midim reciver ro barmigardone
        recived_mes = recive_message_index(i, client)
        if recived_mes:
            tru_mess_ind.append(j)
        j = j + 1
    return tru_mess_ind


def send_mess(list_of_clients, msg_buffer):
    conn.send("To whom you want send message?".encode())
    flag = False
    while True:
        name = conn.recv(1024).decode()
        for i in list_of_clients:
            if i == name:
                flag = True
                conn.send("Accepted".encode())
                conn.send("What do you want to send?\n".encode())

        if not flag:
            conn.send("Client did'nt found try again.".encode())
            continue
        break
    message = conn.recv(1024).decode()
    print(message)
    # Name-> be ki mifreste,
    mess_buffer(msg_buffer, name, message, list_of_clients[len(list_of_clients) - 1])


def user_interface(list_of_clients, msg_buffer):
    while True:
        conn.send("What Do you want to do? \n  "
                  "1.List 2.Send 3.Recive 4.Exit".encode())
        # try:
        ########

        data_from_client = conn.recv(1024).decode()

        # Here we will Serve Client
        if data_from_client == '1':
            conn.send(str(list_of_clients).encode())

        elif data_from_client == '2':
            send_mess(list_of_clients, msg_buffer)

        elif data_from_client == '3':
            index = recive_messages(list_of_clients, msg_buffer)
            sending_message = ""
            for i in index:
                sending_message = sending_message + "\n Next Message for: " + msg_buffer[i]+"\n"
            conn.send(sending_message.encode())
        else:
            conn.send("Thank you for joining".encode())
            list_of_clients.pop()
            conn.close()


def remove_con(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

# except:
#     continue

def threaded_client(connection):
    connection.send("Tell Me Your Name".encode())
    # adding name to list of clients
    data_from_client = connection.recv(1024)
    name_of_clients.append(data_from_client.decode())
    print(name_of_clients)
    # now doing what he wants!
    user_interface(name_of_clients, message_buffer)
    # except:
    #     print("Error Issued")
    #     continue


def initiate_server():
    server = socket.socket()
    print("Socket successfully created")
    port = 9000
    server.bind(('127.0.0.1', port))
    print("socket binded to %s" % port)
    return server


# Main Code


server_socket = initiate_server()
server_socket.listen(5)
print("socket is listening")
name_of_clients = []
message_buffer = []
while True:
    #########################
    # try:
    conn, addr = server_socket.accept()
    print('Got connection from ', addr[0], addr[1])
    start_new_thread(threaded_client, (conn, ))
