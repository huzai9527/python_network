from socket import *
from time import ctime
HOST = ''
PORT = 23456
ADDR = (HOST, PORT)
BUFSIZE = 1024

tcpSerSocket = socket(AF_INET,SOCK_STREAM)
tcpSerSocket.bind(ADDR)
tcpSerSocket.listen(5)

while True:
    print("waiting for connection ...")
    tcpCliSocket, addr = tcpSerSocket.accept()
    print("connected from:", addr)
    while True:
        data = tcpCliSocket.recv(BUFSIZE)
        if not data:
            break
        tcpCliSocket.send(data+b' time now:'+bytes(ctime(), 'utf-8'))
    tcpCliSocket.close()
tcpSerSocket.close()
