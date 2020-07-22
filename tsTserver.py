"""
创建步骤

ss = socket() 创建服务器套接字
ss.bind() 套接字地址绑定
ss.listen() 监听连接
inf_loop: 服务器无限循环
    cs = ss.accept() 接受客户服连接
    comm_loop():   通信循环
        cs.recv()/cs.send() 对话接受/发送
    cs.close()  关闭客户端套接字
ss.close()  关闭服务器套接字
"""
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
