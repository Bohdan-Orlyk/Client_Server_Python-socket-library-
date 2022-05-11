import socket
import json
from Terminal import get_from_server, request_to_server

host = "127.0.0.1"
port = 65432
run = True

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))

        while run:
            option = input("Utworzyc klienta - 1, "
                           "Dokonac wplaty - 2, "
                           "Stan konta - 3, "
                           "Wyplacic srodki - 4, "
                           "Przelew na inne konto - 5, "
                           "Wyjsc - q: ")

            if option == '1':
                # SENDING OPTION OF CREATING A USER
                request_to_server(client, '1')

                # GETTING REQUEST FROM SERVER ABOUT OPTION
                server_message = get_from_server(client)
                print(server_message)

                # CREATING A USER
                name = input("Podaj imie: ")
                surname = input("Podaj nazwisko: ")
                pesel = input("Podaj PESEL: ")
                user_id = 0

                # SENDING DATA ABOUT USER TO SERVER
                user = {"Name": name, "Surname": surname, "ID": user_id, "PESEL": pesel, "Balance": 0}
                sent_data = json.dumps(user)
                request_to_server(client, sent_data)

                # MESSAGE FROM SERVER ABOUT STATUS OF OPERATION
                server_message = get_from_server(client)
                print(server_message)

            elif option == '2':
                # SENDING OPTION OF ADDING MONEY
                request_to_server(client, '2')

                # GETTING REQUEST FROM SERVER ABOUT OPTION
                server_message = get_from_server(client)
                print(server_message)

                # FIND .json DATA BY USER`s Name AND Surname
                name = input("Podaj imie: ")
                surname = input("Podaj nazwisko: ")
                balance = input("Kwota: ")

                # SEND DATA TO SERVER
                user = {"Name": name, "Surname": surname, "Balance": balance}

                data_to_changing = json.dumps(user)
                request_to_server(client, data_to_changing)

                # MESSAGE FROM SERVER ABOUT STATUS OF OPERATION
                server_message = get_from_server(client)
                print(server_message)

            elif option == '3':
                request_to_server(client, '3')

                # GETTING REQUEST FROM SERVER ABOUT OPTION
                server_message = get_from_server(client)
                print(server_message)

                # FIND .json DATA BY USER`s Name AND Surname
                name = input("Podaj imie: ")
                surname = input("Podaj nazwisko: ")

                user = {"Name": name, "Surname": surname}
                data_to_find = json.dumps(user)
                request_to_server(client, data_to_find)

                # MESSAGE FROM SERVER ABOUT STATUS OF OPERATION
                server_message = get_from_server(client)
                print(server_message)

            elif option == 'q':
                print("\t\n Do widzenia!")
                request_to_server(client, 'q')
                run = False

            else:
                print("Wybierz jedna z opcji!")
except ConnectionRefusedError:
    print("SERVER ISN`T RESPONDING")
