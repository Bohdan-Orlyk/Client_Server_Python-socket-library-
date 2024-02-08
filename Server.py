import socket
import Terminal as terminal


class Server:
    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 65432
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.options = {
            '1': terminal.create_user,
            '2': terminal.change_balance,
            '3': terminal.show_information,
            '4': terminal.get_money,
            'q': self.stop_server,
        }

    def run_server(self):
        while True:
            with self.server_socket as server:
                server.bind((self.HOST, self.PORT))
                server.listen(4)
                print("SERVER STARTED!")

                user, address = server.accept()

                with user:
                    print(f"Connected by {address}")

                    while True:
                        option = user.recv(1024).decode('utf-8')

                        if option:
                            print("Option:", option)
                            try:
                                service = self.options.get(option)
                                service(user)
                            except ConnectionRefusedError:
                                terminal.request_to_client(user, "Connection refused :/ ")
                            except FileNotFoundError:
                                terminal.request_to_client(user, "Bad data")
                            except ValueError:
                                terminal.request_to_client(user, "Bad data")

    def stop_server(self, address):
        print(f'USER with {address=} DISCONNECTED!')
        raise Exception


if __name__ == '__main__':
    Server = Server()
    Server.run_server()







                    #
                    #
                    #
                    #
                    #
                    #
                    # if option == '1':
                    #     try:
                    #         terminal.create_user(user)
                    #     except ConnectionRefusedError:
                    #         terminal.request_to_client(user, "Cos poszlo nie tak :( ")
                    #         print("ERROR!")
                    #
                    # elif option == '2':
                    #     try:
                    #         terminal.change_balance(user)
                    #     except ConnectionRefusedError:
                    #         terminal.request_to_client(user, "Cos poszlo nie tak :( ")
                    #         print("ERROR!")
                    #
                    #     except FileNotFoundError:
                    #         terminal.request_to_client(user, "Nieprawidlowo podane dane!")
                    #         print("ERROR!")
                    #
                    #     except ValueError:
                    #         terminal.request_to_client(user, "Nieprawidlowo podane dane!")
                    #         print("ERROR!")
                    #
                    # elif option == '3':
                    #     try:
                    #         terminal.show_information(user)
                    #     except ConnectionRefusedError:
                    #         terminal.request_to_client(user, "Cos poszlo nie tak :( ")
                    #         print("ERROR!")
                    #
                    #     except FileNotFoundError:
                    #         terminal.request_to_client(user, "Nieprawidlowo podane dane!")
                    #         print("ERROR!")
                    #
                    # elif option == '4':
                    #     try:
                    #         terminal.get_money(user)
                    #     except ConnectionRefusedError:
                    #         terminal.request_to_client(user, "Cos poszlo nie tak :( ")
                    #         print("ERROR!")
                    #
                    #     except FileNotFoundError:
                    #         terminal.request_to_client(user, "Nieprawidlowo podane dane!")
                    #         print("ERROR!")
                    #
                    #     except ValueError:
                    #         terminal.request_to_client(user, "Nieprawidlowo podane dane!")
                    #         print("ERROR!")
                    #
                    # if not option:
                    #     print('USER DISCONNECTED!')
                    #     break
