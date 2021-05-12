import socket
import UserPI
import UserDTP


class ClientFTP:
    def __init__(self, server_port=5000, server_host=socket.gethostbyname(
            socket.gethostname()), buffer_size=1024):
        self.server_host = server_host
        self.server_port = server_port
        self.buffer_size = buffer_size
        self.user_pi = UserPI()
        self.user_dtp = UserDTP()

    def connect_server(self):
        self.server_host = input("Enter IP of Host to connect: \n")
        self.server_port = input("Enter IP of Port to connect: \n")

        print("Sending server requests...")
        try:
            self.user_pi.set_control_connection((self.server_host,
                                                 self.server_port))
            print("Control Connection sucessful!")
        except:  # TODO: determine exception that should go here?
            print("Control connection unsucessful. Make sure the server is" +
                  "online or that the ports are available")
        try:
            self.user_dtp.set_control_connection((self.server_host,
                                                  self.server_port + 1))
            print("Data Connection sucessful!")
        except:  # TODO: determine exception that should go here?
            print("Data connection unsucessful. Make sure the server is" +
                  "online or that the ports are available")


def main():
    # Still need to program the main here
    pass


if __name__ == "__main__":
    main()
