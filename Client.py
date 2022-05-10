import json
import socket

host = "127.0.0.1"
port = 65432
run = True

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))

        while run:
            option = input("Utworzyc klienta - 1, "
                           "Zmienic stan salda - 2, "
                           "Wyjsc - q: ")

            if option == '1':
                # SENDING OPTION OF CREATING A USER
                data = '1'.encode('utf-8')
                client.sendall(data)

                # GETTING REQUEST FROM SERVER ABOUT OPTION
                request_from_server = client.recv(1024)
                server_message = request_from_server.decode('utf-8')
                print(server_message)

                # CREATING A USER
                name = input("Podaj imie: ")
                surname = input("Podaj nazwisko: ")
                pesel = input("Podaj PESEL: ")

                # SENDING DATA ABOUT USER TO SERVER
                user = {"Name": name, "Surname": surname, "PESEL": pesel, "Balance": 0}
                sent_data = json.dumps(user)
                client.sendall(data_to_changing.encode('utf-8'))

                # GETTING REQUEST ABOUT CREATING USER
                request_from_server = client.recv(1024)
                server_message = request_from_server.decode('utf-8')
                print(server_message)

            elif option == '2':
                # SENDING OPTION OF ADDING MONEY
                data = '2'.encode('utf-8')
                client.sendall(data)

                # GETTING REQUEST FROM SERVER ABOUT OPTION
                request_from_server = client.recv(1024)
                server_message = request_from_server.decode('utf-8')
                print(server_message)

                # FIND .json DATA BY USER`s Name AND Surname
                name = input("Podaj imie: ")
                surname = input("Podaj nazwisko: ")
                balance = input("Kwota: ")

                user = {"Name": name, "Surname": surname, "Balance": balance}
                data_to_changing = json.dumps(user)
                client.sendall(data_to_changing.encode('utf-8'))

                # MESSAGE FROM ABOUT STATUS OF OPERATION
                request_from_server = client.recv(1024)
                server_message = request_from_server.decode('utf-8')
                print(server_message)

            elif option == 'q':
                print("\t\n Do widzenia!")
                data = 'q'.encode('utf-8')
                client.sendall(data)
                run = False

            else:
                print("Wybierz jedna z opcji!")
except ConnectionRefusedError:
    print("SERVER ISN`T RESPONDING")
