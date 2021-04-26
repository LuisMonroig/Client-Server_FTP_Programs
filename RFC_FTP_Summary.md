# Summary FTP (Luis Monroig)

| Acronym |            Meaning            |
| :------ | :---------------------------: |
| RFC     |      Request for Comment      |
| TCP     | Transmission Control Protocol |
| NVT     |    Network Virtual Terminal   |
| NVFS    |  Network Virtual File System  |
| PI      |    The protocol interpreter   |
| DTP     |     Data Transfer Process     |

###### Objectives of FTP:

-   Promote sharing of files
-   Encourage indirect or implicit (via programs) use of remote computers
-   To shield a user from variations in file storage systems among hosts
-   To transfer data reliably and efficiently

###### Purposes Transferring Files:

-   Printing => receiver knows vertical format control is represented
-   Storage => to store a file at a host and then retrieve it later in exactly the same form
-   Retrieval
-   Processing

###### FTP Components (Overview)

<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>

<img src = "FTP_project_images/FTP_components.png" alt = "FTP Components" width = 400 />


Control connection **&lt;=>** communication path between the USER-PI and SERVER-PI.

Control connection **=>** Telnet Protocol.

PI has 2 types: user-PI and server-PI which are programs that interprets user commands and server commands.

**Def:** Files are transferred only via the data connection. The control connection is used for the transfer of commands.

<br>

DTP (pp. 18 RFC)

Data connection in FTP is in full duplex connection.
DTP Requires:

-   setting up the data connection to the appropriate ports
    -   Remember that the user-process default data port is the same as the control connection port (i.e., U).
    -   The server-process default data port is the port adjacent to the control connection port (i.e., L-1).
-   choosing the parameters for transfer

User can specify an alternate data port by use of the PORT command.

FTP request command
determines the direction of the data transfer

-   retrieve from 3rd party host:
    1.  user-PI sets up control connections with both server-PI’s
    2.  One server is then told (by an FTP command) to "listen" for a connection which the other will initiate.
    3.  The user-PI sends one server-PI a PORT command indicating the data port of the other.
    4.  Finally, both are sent the appropriate transfer commands.

Server must maintain the data connection--to initiate it and to close it.maintain the data connection--to initiate it and to close it.

###### The server-PI:

-   Establishes _control communication connection_
-   Receives standard FTP commands from the user-PI
-   Sends replies
-   Governs the server-DTP

###### The User-PI

-   Initiates the control connection from its port U to the server-FTP process
-   Initiates FTP commands
-   Governs the user-DTP if that process is part of the file transfer

###### User FTP Process Requirements for File Transfer:

-   Protocol Interpreter
-   Data Transfer Process (DTP)
-   User interface
-   Cooperation with one or more server-FTP processes

<!-- TODO: Add picture of parts of FTP-->

###### The FTP commands:

-   Specify the parameters for the data connection:
    -   Data port
    -   Transfer mode (specify how the bits of the data are to be transmitted)
    -   Representation type (define the way in which the data are to be represented)
    -   Structure (define the way in which the data are to be represented)
    -   nature of file system operation (e.g. store, delete)
-   4tuple ()

###### Transferring data between two hosts (no local host):

-   Control connection must be open while file transfer takes place

    <!-- TODO: Add picture of data between two hosts-->

    <img src = "FTP_project_images/TransferingDataBetweenHosts.png" alt = "FTP Components" width = 400 />

Possible modifications of the repo found:

-   Change file's transfer mode
-   Do transferring between 2 hosts (none local host)
-   Change to non-default port
-   Use the threading library
-   Retrieve from 3rd party host:
    1.  user-PI sets up control connections with both server-PI’s
    2.  One server is then told (by an FTP command) to "listen" for a connection which the other will initiate.
    3.  The user-PI sends one server-PI a PORT command indicating the data port of the other.
    4.  Finally, both are sent the appropriate transfer commands.

###### File Structure:

-   file-structure (default) (must be accepted)
-   record-structure (default) (must be accepted)
-   page-structure
