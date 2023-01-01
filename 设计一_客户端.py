import time
from socket import *

# AF_INET表示使用IPv4，SOCK_DGRAM表示使用UDP套接字
clientSocket = socket(AF_INET, SOCK_DGRAM)

server = ('192.168.1.5', 12000)
# 设置超时时间为1秒
clientSocket.settimeout(1)
timeoutcount = 0
maxRTT = 0
minRTT = 1
sumRTT = 0
for i in range(10):
    # 发送ping命令
    clientSocket.sendto(b"ping", server)
    send_time = time.time()

    try:
        message, _ = clientSocket.recvfrom(1024)
        recv_time = time.time()
        delay = (recv_time - send_time) * 1000
        print(f"{i}\t{message.decode()}\tRTT: {(recv_time - send_time) * 1000:.2f}ms")
        maxRTT = max(maxRTT, delay)
        minRTT = min(minRTT, delay)
        sumRTT += delay
    except timeout as e:  # 超时就打印time out
        print(f"{i}\ttime out...")
        timeoutcount += 1
# 输出超时率
print(f"timeout rate:\t{(timeoutcount / 10) * 100:.2f}%")
# 输出平均RTT，最大最小RTT
print(f"RTT:\tmax:\t{maxRTT:.2f}\tmin:\t{minRTT}\taverage:{sumRTT / (10 - timeoutcount):.2f}")
clientSocket.close()
