import socket
import sys
import time
import os
import struct
import subprocess


def list_files():
    listdir = os.listdir()
    dirlen = len(listdir)
    conn.send(str(dirlen).encode('utf-8'))
    for i in range(dirlen):
        conn.send(listdir[i].encode('utf-8'))
        print("sent: " + str(i))
        print(listdir[i])
    return


def download_files():
    print("Runned function")
    selected_file = conn.recv(buffer_size).decode('utf-8')

    # Get file extension
    filename_path, file_name = os.path.split(selected_file)
    print(filename_path)
    print(file_name)
    # Get file size
    file_size = os.path.getsize(selected_file)
    conn.send(str(file_size).encode('utf-8'))

    # Send file extention type
    conn.send(str(file_name).encode('utf-8'))

    # Rest of function
    with open(f"{selected_file}", "rb") as f:
        data = f.read()
    # send file name with extencion
    conn.sendall(data)
    f.close()


def upload_file():
    # Receive the file of the file being sent
    file_size = conn.recv(buffer_size).decode('utf-8')

    # Receive the file name+extencion type
    file_name = conn.recv(buffer_size).decode('utf-8')

    # Receive the data of the file being sent
    file_data = conn.recv(int(file_size))

    # Open new file and write the received data
    f = open("server_data/" + file_name, 'wb')
    f.write(file_data)

    # Close the the file that was previously opened
    f.close()


def create_directory():
    directory_name = conn.recv(1024).decode('utf-8')
    path = os.getcwd() + "\\" + directory_name
    os.mkdir(path)


# Host = "192.168.1.10"
Host = "192.168.1.10"
# socket.gethostbyname(socket.gethostname())
Port = 5000
buffer_size = 1024
FORMAT = 'utf-8'

# AF_INET == IPv4
# SOCK_Stream == tcp socket type, UDP uses SOCKET_DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket  to associate the socket with a specific network interface and port number
s.bind((Host, Port))
# Listen to incoming connections
s.listen(1)
conn, addr = s.accept()

# Send the client the current working directory to the client
conn.send(str(os.getcwd()).encode('utf-8'))

with conn:
    print('Connected by: ', addr)
    # Decode from bytes to string
    data = conn.recv(buffer_size).decode()
    while True:
        if data == "DIR":
            list_files()
        if data == "DOWNLOAD":
            download_files()
        if data == "UPLOAD":
            upload_file()
        if data == "mkdir":
            create_directory()
        data = None
