# Create a socket (connect two computers)
import socket
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_address = []


def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket binding error " + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Handling connections from multiple clients and saving to a list
# Close all previous connections where this program is re-started.
def accepting_connections():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)  # Prevents timeout
            all_connections.append(conn)
            all_address.append(address)
            print("Connection has been established : " + address[0])
        except:
            print("Error accepting connections")
