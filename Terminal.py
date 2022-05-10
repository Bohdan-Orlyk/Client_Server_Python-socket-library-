import json


def create_user(user):
    # SERVER REQUEST TO CREATE A USER
    user.sendall("\n\t Tworzenie uzytkownika: ".encode('utf-8'))

    # GETTING DATA FROM USER AND SAVING IN .json FORMAT
    user_info = user.recv(1024).decode('utf-8')
    user_info_json = json.loads(user_info)
    print("USER DATA:", user_info_json)

    name = user_info_json["Name"]
    surname = user_info_json["Surname"]
    with open(f'Users/{name}_{surname}.json', 'w') as data_file:
        json.dump(user_info_json, data_file)

    user.sendall("Uzytkownik utworzony! \n".encode('utf-8'))


def change_balance(user):
    # SERVER REQUEST TO CREATE A USER
    user.sendall("\n\t Zmiana salda dla uzytkownika: ".encode('utf-8'))

    # GETTING DATA FROM USER AND SAVING IN .json FORMAT
    user_info = user.recv(1024).decode('utf-8')
    user_info_json = json.loads(user_info)
    print("USER DATA:", user_info_json)

    # ADDING MONEY ON USER`s BALANCE
    name = user_info_json["Name"]
    surname = user_info_json["Surname"]
    balance = user_info_json["Balance"]

    with open(f'Users/{name}_{surname}.json', 'r') as file_to_changing:
        data = json.load(file_to_changing)

    data["Balance"] += float(balance)

    with open(f'Users/{name}_{surname}.json', 'w') as file_to_changing:
        json.dump(data, file_to_changing)

    # SENDING STATUS OF OPERATION
    user.sendall(f"\n\t Kwota po operacji wynosi: {data['Balance']} PLN".encode('utf-8'))
