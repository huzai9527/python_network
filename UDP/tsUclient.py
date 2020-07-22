"""
创建客户端
cs = socket()  创建客户端套接字
comm_loop:
    cs.sendto()/cs.recvfrom() 对话（接受/发送）
cs.close()
"""

from socket import *
HOST = '192.168.0.117'
PORT = 23456
BUFSIZE = 1024
ADDR = (HOST, PORT)
udpClientSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input('> ')
    if not data:
        break
    udpClientSock.sendto(data.encode(), ADDR)
    data, ADDR = udpClientSock.recvfrom(BUFSIZE)
    if not data:
        break
    print(data)
udpClientSock.close()