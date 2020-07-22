"""
创建客户段为代码
cs  = socket() 创建客户端套接字
cs.connect() 尝试连接服务器
comm_loop: 通信循环
    cs.send()/cs.recv() 对话（发送/接收）
cs.close()
"""
from socket import *
from time import ctime
HOST = "192.168.0.118"
PORT = 23456
ADDR = (HOST, PORT)
BUFSIZE = 1024

tcpCliSocket = socket(AF_INET, SOCK_STREAM)
tcpCliSocket.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break

    tcpCliSocket.send(data.encode())
    data = tcpCliSocket.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSocket.close()