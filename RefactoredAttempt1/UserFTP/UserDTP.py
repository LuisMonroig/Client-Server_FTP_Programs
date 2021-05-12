import os
import socket


class UserDTP:
    # TODO: Set the constructor to have the
    def __init__(self):
        self.data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def set_control_connection(self, host_and_port):
        """Function argumewnt host_and_port is a tuple (host, port)."""
        self.control_socket.connect(host_and_port)

    def quit():
        pass
# here add any other function related to the dtp
