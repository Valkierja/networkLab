
from socket import *
import random
import time
# 创建一个UDP套接字(SOCk_DGRAM)
serverSocket = socket(AF_INET,SOCK_DGRAM)
# 绑定server端IP和端口
serverSocket.bind(('',12000))
while True:
    rand = random.randint(0,10)
    # 接收信息
    message, address =serverSocket.recvfrom(1024)

    # 模拟30%的数据丢失。
    if rand<4:
        continue
    if message == b"ping":
        serverSocket.sendto(b"pong", address)