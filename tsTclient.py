from socket import *
from time import ctime
HOST = "192.168.2.103"
PORT = 23456
ADDR = (HOST, PORT)
BUFSIZE = 1024

tcpCliSocket = socket(AF_INET, SOCK_STREAM)
tcpCliSocket.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSocket.send(data)
    data = tcpCliSocket.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSocket.close()