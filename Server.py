import socket
from Terminal import *

host = "127.0.0.1"
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((host, port))
    server.listen(4)

    print("SERVER STARTED!")

    while True:
        user, address = server.accept()
        with user:
            print(f"Connected by {address}")
            while True:
                data = user.recv(1024).decode('utf-8')
                print("Option:", data)

                if data == '1':
                    try:
                        create_user(user)
                    except ConnectionRefusedError:
                        user.sendall("\n\t Cos poszlo nie tak :( ".encode('utf-8'))
                        print("USER DISCONNECTED!")
                elif data == '2':
                    try:
                        change_balance(user)
                    except ConnectionRefusedError:
                        user.sendall("\n\t Cos poszlo nie tak :( ".encode('utf-8'))
                        print("USER DISCONNECTED!")
                if not data:
                    print("SERVER STOPPED!")
                    break
