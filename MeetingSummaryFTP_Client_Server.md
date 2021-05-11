# FTP Client / Server Project

## Summary of Meeting 1

#### Instructions for the FTP Client implementation

-   [ ] The client should initiate a TCP connection with the server.
-   [ ] Client must be able to view any of the directories and download any of the available files via **_TCP_**.
-   [ ] The client must also be able to upload files and create new directories.
-   [ ] Design a simple GUI that helps us present the implementation of the protocol to the professor.
-   [ ] Make a presentation using the Engineering Design Process

#### Instructions for the FTP Server implementation

-   [ ] FTP server must include at least 3 directories with 5 files each
-   [ ] Transfer files to client

#### Todo

-   [x] Create GitHub repo
-   [x] Research the Engineering Design Process
-   [ ] Find and try to read RFC 959, and any relevant updates, to ensure that the protocol is properly implemented
-   [x] Research pros con python
-   [x] Research pros con C# .net
-   [ ] Email professor about which technology he recommends: c# .net or python.
    <br>

* * *

## Summary of Meeting 2

#### Decisions made:

-   Python will be used due to  the existence of incredibly useful and simple libraries and other  FTP projects online that are similar to ours.  
-   Added Ema and Mario to the GitHub project
-   The project will be implemented using socket libraries instead of the built in library [ftplib](https://docs.python.org/3/library/ftplib.html).
-   Next meeting: Monday from 4pm to 5pm

#### Todo

-   [x] Email professor to ask about which Engineering Design Process (EDP) should we use. (Luis)
-   [X] Try to finish reading RFC 959. (All)
-   [x] Download or screen-record the classes about UDP and TCP that are about to be erased, in case they are necessary in the future. (Volunteer)
-   [X] Research the following libraries: (All)
    -   [X] import socket
    -   [X] import sys
    -   [X] import os
    -   [X] import struct
-   [ ] Check if the code in other GitHub profiles does work (clone/test), read it, and understand it. (Volunteer)

* * *

## Summary of Meeting 3

#### Decisions made:

-   Read and build prototype
-   Learn some GUI framework to use it for the project
-   Research how to display the file explorer from a server to the client.

#### Todo

-   [X] Try to finish reading RFC 959. (All)
-   [X] Research the following libraries: (All)
    -   [X] import socket
    -   [X] import sys
    -   [X] import os
    -   [X] import struct
-   [ ] Read and fully understand the code in other GitHub profiles and how it works (read it, and understand it) (All)

### Next Meeting date
- TBA

---

## Summary of Meeting 4

#### Decisions made:
- Add the following commands to meet the professors requirement: CWD, CDUP, STAT, MKD, PWD (FSM_1), LIST, NLST? (FSM_2).
- Hands-on coding meeting Tomorrow May 11 at 7pm. Using Atoms text editor and the teletype package.
- PyQt5 will be used for the GUI and ideas for the design where discussed.

#### Todo

- [ ] Review the concepts on the minimal requirements section.
- [ ] Understand FSM's.
- [ ] Read and understand the Ema's cod and the prototype code obtained from GitHub.
- [ ] Continue to deepen our knowledge in the most relevant python classes.

---
