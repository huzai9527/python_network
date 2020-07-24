from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 2345
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print('connected from:', self.client_address)
        self.wfile.write(ctime().encode())

tcpServer = TCP(ADDR, MyRequestHandler)
print('waiting for connection')
tcpServer.serve_forever()

