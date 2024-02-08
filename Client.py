import socket
import json
import Terminal as terminal


class KilledSession(BaseException):
    pass


def server_message(func):
    def wrapper(client, option):
        terminal.request_to_server(client, option)
        print(terminal.get_from_server(client))

        func(client)

        print(terminal.get_from_server(client))

    return wrapper


class Client:
    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 65432
        self.options = {
            "1": self.create_client,
            "2": self.add_cash,
            "3": self.get_bank_status,
            "4": self.get_cash,
            "5": self.transfer_cash_to_another_account,
            "q": self.stop_client,
        }

    def start_client(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((self.HOST, self.PORT))

                while True:
                    option = input("Utworzyc klienta - 1, "
                                   "Dokonac wplaty - 2, "
                                   "Stan konta - 3, "
                                   "Wyplacic srodki - 4, "
                                   "Przelew na inne konto - 5, "
                                   "Wyjsc - q: ")

                    if option:
                        func = self.options.get(option, None)

                        if func:
                            func(client=client, option=option)
                        else:
                            print("Wybierz jedna z opcji!")
        except KilledSession:
            print("\t\n Do widzenia!")
        except ConnectionRefusedError:
            print("SERVER ISN`T RESPONDING")

    @staticmethod
    @server_message
    def create_client(client):
        """CREATING A USER"""

        name = input("Podaj imie: ")
        surname = input("Podaj nazwisko: ")
        pesel = input("Podaj PESEL: ")
        user_id = 0

        # SENDING DATA ABOUT USER TO SERVER
        user = {"Name": name, "Surname": surname, "ID": user_id, "PESEL": pesel, "Balance": 0}
        sent_data = json.dumps(user)

        terminal.request_to_server(client, sent_data)

    @staticmethod
    @server_message
    def add_cash(client):
        """ FIND .json DATA BY USER`s Name AND Surname """

        name = input("Podaj imie: ")
        surname = input("Podaj nazwisko: ")
        balance = input("Kwota: ")
        # SEND DATA TO SERVER
        user = {"Name": name, "Surname": surname, "Balance": balance}
        data_to_changing = json.dumps(user)

        terminal.request_to_server(client, data_to_changing)

    @staticmethod
    @server_message
    def get_bank_status(client):
        """FIND .json DATA BY USER`s Name AND Surname"""

        name = input("Podaj imie: ")
        surname = input("Podaj nazwisko: ")
        user = {"Name": name, "Surname": surname}
        data_to_find = json.dumps(user)

        terminal.request_to_server(client, data_to_find)

    @staticmethod
    @server_message
    def get_cash(client):
        """FIND .json DATA BY USER`s Name AND Surname"""

        name = input("Podaj imie: ")
        surname = input("Podaj nazwisko: ")
        balance_to_get = input("Kwota do wyplaty: ")

        # SEND DATA TO SERVER
        user = {"Name": name, "Surname": surname, "BalanceToGet": balance_to_get}
        data_to_changing = json.dumps(user)

        terminal.request_to_server(client, data_to_changing)

    @staticmethod
    @server_message
    def transfer_cash_to_another_account(client):
        ...

    @staticmethod
    @server_message
    def stop_client(client):
        terminal.request_to_server(client, 'q')

        raise KilledSession


if __name__ == "__main__":
    Client = Client()
    Client.start_client()
