from socket import *
HOST = '127.0.0.1'
PORT = 2345
BUFSIZE = 1024
ADDR = (HOST, PORT)
while True:
    tcpClisock = socket(AF_INET, SOCK_STREAM)
    tcpClisock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpClisock.send(data.encode())
    data = tcpClisock.recv(BUFSIZE)
    if not data:
        break
    print(data.strip())
    tcpClisock.close()