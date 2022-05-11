import json


def get_from_client(user):
    user_request = user.recv(1024).decode('utf-8')
    user_info_json = json.loads(user_request)

    return user_info_json


def request_to_client(user, message_to_client):
    user.sendall(f"\t {message_to_client} \n".encode('utf-8'))


def get_from_server(client):
    request_from_server = client.recv(1024)
    server_message = request_from_server.decode('utf-8')

    return server_message


def request_to_server(client, message_to_server):
    client.sendall(f"{message_to_server}".encode('utf-8'))


def create_user(user):
    # SERVER REQUEST TO CREATE A USER
    request_to_client(user, "Tworzenie uzytkownika: ")

    # GETTING DATA FROM USER AND SAVING IN .json FORMAT
    user_info_json = get_from_client(user)
    print("USER DATA:", user_info_json)

    name = user_info_json["Name"]
    surname = user_info_json["Surname"]
    with open(f'Users/{name}_{surname}.json', 'w') as data_file:
        json.dump(user_info_json, data_file)

    message_to_client = "Uzytkownik utworzony!"
    request_to_client(user, message_to_client)


def change_balance(user):
    # SERVER REQUEST TO CREATE A USER
    request_to_client(user, "Zmiana salda dla uzytkownika: ")

    # GETTING DATA FROM USER AND SAVING IN .json FORMAT
    user_info_json = get_from_client(user)
    print("USER DATA:", user_info_json)

    # ADDING MONEY ON USER`s BALANCE
    name = user_info_json["Name"]
    surname = user_info_json["Surname"]
    balance = user_info_json["Balance"]

    if float(balance) <= 0:
        request_to_client(user, "Kwota nie moze byc ujemna albo zero! ")

    else:
        with open(f'Users/{name}_{surname}.json', 'r') as file_to_changing:
            data = json.load(file_to_changing)

        data["Balance"] += float(balance)

        with open(f'Users/{name}_{surname}.json', 'w') as file_to_changing:
            json.dump(data, file_to_changing)

        # SENDING STATUS OF OPERATION
        message_to_client = f"Kwota po operacji wynosi: {data['Balance']} PLN"
        request_to_client(user, message_to_client)


def show_information(user):
    # SERVER REQUEST TO SHOW INFORMATION ABOUT USER
    request_to_client(user, "Informacja o koncie: ")

    # GETTING DATA FROM USER AND SAVING IN .json FORMAT
    user_info_json = get_from_client(user)
    print("USER DATA:", user_info_json)

    # GETTING name AND surname FROM USER TO CHECK DATA
    name = user_info_json["Name"]
    surname = user_info_json["Surname"]

    with open(f'Users/{name}_{surname}.json', 'r') as show_info_file:
        data = json.load(show_info_file)

    # SENDING STATUS OF OPERATION
    message_to_client = f"Uzytkownik: {data['Name']} {data['Surname']}. " \
                        f"Numer konta: {data['ID']}. " \
                        f"Saldo: {data['Balance']} PLN"
    request_to_client(user, message_to_client)
