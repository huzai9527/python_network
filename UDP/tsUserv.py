"""
创建服务器
ss.socket() 创建服务器套接字
ss.bind() 绑定服务器套接字
inf_loop: 服务器无限循环
    cs = ss.recvfrom()/ss.sendto() 服务器（接受/发送）
ss.close()
"""

from socket import *
from time import ctime

HOST = ''
PORT = 23456
BUFSIZE = 1024
ADDR = (HOST, PORT)
udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)
while True:
    print("waiting for message...")
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    udpSerSock.sendto(data+b' time now: '+bytes(ctime(), 'utf-8'), addr)
    print("received from and returned to:"+str(addr))
udpSerSock.close()
