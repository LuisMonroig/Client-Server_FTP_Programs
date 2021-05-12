import socket
# import sys
import os
import threading

"""###### Minimal Requirements for FTP:

- [ ] TYPE - ASCII Non-print (DONE: Used utf-8 argument in the encode function)
-   MODE - Stream   (????)
-   STRUCTURE - File (DONE) Record (which we will leave for the end)
-   COMMANDS - USER (Falta), QUIT, PORT(DONE), TYPE, MODE, STRU, for the default values RETR (DONE), STOR(DONE), NOOP.
-   The default values for transfer parameters are:
    -   TYPE - ASCII Non-print
    -   MODE - Stream
    -   STRU - File
-   Must support data transfer using the default port, and that only the USER-PI may initiate the use of non-default ports.
- Also implement the following commands: CWD, CDUP(DONE), STAT, MKD(DONE), PWD (#os.getcwd()), LIST, NLST? (FSM_2).
**All hosts must accept the above as the standard defaults.**"""


# TODO: class definition
class ServerFTP:
    def __init__(self):
        pass
        # TODO: Separate this function into DTP and Control connection


def list_files(conn):
    list_dir = os.listdir()
    dir_len = len(list_dir)
    conn.send(str(dir_len).encode('utf-8'))  # TODO: why utf-8?
    for i in range(dir_len):
        conn.send(list_dir[i].encode('utf-8'))  # 'unicode_escape'
        print("sent: " + str(i))
        print(list_dir[i])
    return


def download_files(conn, buffer_size):
    print("Runned function")
    selected_file = conn.recv(buffer_size).decode('utf-8')  # 'unicode_escape'

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
    f.close()  # TODO: Add a context manager


def upload_file(conn, buffer_size):
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
    f.close()     # TODO: add with


def create_directory(conn, buffer_size):
    directory_name = conn.recv(buffer_size).decode('utf-8')
    path = os.getcwd() + "\\" + directory_name
    os.mkdir(path)


def main():
    Host = "192.168.1.10"
    # socket.gethostbyname(socket.gethostname())
    Port = 5000

    # AF_INET == IPv4
    # SOCK_Stream == tcp socket type, UDP uses SOCKET_DGRAM
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket  to associate the socket with a specific network
    # interface and port number
    s.bind((Host, Port))

    print("Server is starting...")
    start(s)


def client_handler(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        print('Connected by: ', addr)
        # Decode from bytes to string
        buffer_size = 1024
        data = conn.recv(1024).decode()
        while True:
            if data == "DIR":
                list_files(conn)
            if data == "DOWNLOAD":
                download_files(conn, buffer_size)
            if data == "UPLOAD":
                upload_file(conn, buffer_size)
            if data == "mkdir":
                create_directory(conn, buffer_size)
            data = None
    conn.close()


def start(s):
    s.listen()
    print(f"[LISTENING] Server is listening on {s}")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=client_handler, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


if __name__ == "__main__":
    main()
