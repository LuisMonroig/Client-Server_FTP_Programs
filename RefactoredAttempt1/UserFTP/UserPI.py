import os
import socket


class UserPI:
    # TODO: Set the constructor to have the
    def __init__(self):
        self.control_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def set_control_connection(self, host_and_port):
        """Function argumewnt host_and_port is a tuple (host, port)."""
        self.control_socket.connect(host_and_port)

    def send_FTP_cmd(self, FTP_cmd):
        self.control_socket.send(FTP_cmd.encode('utf-8'))

    def client_command(self):
        while True:
            print("FTP>", end=" ")
            FTP_cmd = input()
            # In case of GUI implementation
            path = ""
            if " " in FTP_cmd:
                split_cmd = FTP_cmd.split(" ")
                FTP_cmd = split_cmd[0]  # reuse FTP_cmd variable
                path = split_cmd[1]

            if FTP_cmd == "DIR":
                self.send_FTP_cmd(FTP_cmd)
                self.list_files()

            if FTP_cmd == "STOR":
                self.send_FTP_cmd(FTP_cmd)
                self.stor(path)

            if FTP_cmd == "RETR":
                self.send_FTP_cmd(FTP_cmd)
                self.retr(path)

            if FTP_cmd == "MKD":
                self.send_FTP_cmd(FTP_cmd)
                self.mkd(path)
                FTP_cmd = None
            if FTP_cmd == "QUIT":
                break

    def list_files(self):  # TODO: should we set path?
        dir_length = self.control_socket.recv(1024).decode()  # Encode the string to bytes
        for i in range(int(dir_length)):
            print(self.control_socket.recv(1024).decode('utf-8'))

    def mkd(self, path):  # TODO: Set default for path of mkd
        self.control_socket.send(path.encode('utf-8'))

    def stor(self, path):  # TODO: Set default for path of stor
        # TODO: asses if it is necessary to change variable name to path
        selected_file_path = path
        self.control_socket.send(str(selected_file_path).encode('utf-8'))
        print("sent requested file name")

        # Receive the file of the file being sent
        file_size = self.control_socket.recv(1024).decode('utf-8')

        # Receive the file name+extencion type
        file_name = self.control_socket.recv(1024).decode('utf-8')
        print(file_name)

        file_data = self.control_socket.recv(int(file_size))
        with open("client_data/" + file_name, 'wb') as f:
            f.write(file_data)

    def retr(self, path="client_data/text.txt"):
        with self.control_socket:
            # Get file extension
            filename_path, file_name = os.path.split(path)

            # Get file size
            file_size = os.path.getsize(path)
            self.control_socket.send(str(file_size).encode('utf-8'))

            # Send file extention type
            self.control_socket.send(str(file_name).encode('utf-8'))

            # Rest of function
            with open(path, "rb") as f:
                data = f.read()
            # send file name with extencion
            self.control_socket.sendall(data)
