import socket

import sys
import os
import struct


# Connect to IP
def connect(host, port, buffer_size, s):
    # Connect to the server
    print("Sending server request...")
    try:
        s.connect((host, port))
        print("Connection sucessful")
    except:
        print("Connection unsucessful. Make sure the server is online.")


# List contents of directory
def list_files(option, s):
    # Encode the string to bytes
    s.send(option.encode('utf-8'))
    dir_length = s.recv(1024).decode()
    # i = 0
    for i in range(int(dir_length)):
        print(s.recv(1024).decode('utf-8'))


# Download file from server
def download_file(option, s):
    s.send(option.encode('utf-8'))
    selected_file_path = "server_data/text.txt"
    s.send(str(selected_file_path).encode('utf-8'))
    print("sent requested file name")
    # Receive the file of the file being sent
    file_size = s.recv(1024).decode('utf-8')

    # Receive the file name+extencion type
    file_name = s.recv(1024).decode('utf-8')
    print(file_name)
    # Receive the data of the file being sent
    file_data = s.recv(int(file_size))

    # Open new file and write the received data
    f = open("client_data/" + file_name, 'wb')
    f.write(file_data)

    # Close the the file that was previously opened
    f.close()


def upload_file(option, s):
    s.send(option.encode('utf-8'))
    path = "client_data/test.pdf"

    # Get file extension
    filename_path, file_name = os.path.split(path)

    # Get file size
    file_size = os.path.getsize(path)
    s.send(str(file_size).encode('utf-8'))

    # Send file name+extention type
    s.send(str(file_name).encode('utf-8'))

    # Rest of function
    with open(f"{path}", "rb") as f:
        data = f.read()
    # send file name with extencion
    s.sendall(data)
    f.close()


def create_directory(split_option_command, split_option_arg, s):
    s.send(split_option_command.encode('utf-8'))
    s.send(split_option_arg.encode('utf-8'))


def main():
    host = "192.168.1.10"
    port = 5000
    buffer_size = 1024

    print("Enter IP of Host to connect: \n")
    input(host)
    print("Enter IP of Port to connect: \n")
    input(port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect(host, port, buffer_size, s)

    while True:
        print("FTP>")
        option = input()
        split_option_command = ""
        split_option_arg = ""

        if " " in option:
            split_option = option.split()
            split_option_command = split_option[0]
            split_option_arg = split_option[1]

        if option == "DIR":
            list_files(option, s)
        if option == "DOWNLOAD":
            download_file(option, s)
        if option == "UPLOAD":
            upload_file(option, s)
        if split_option_command == "mkdir":
            create_directory(split_option_command, split_option_arg, s)
            option = None
        if option == "QUIT":
            break


if __name__ == "__main__":
    main()
