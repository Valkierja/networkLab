from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", 12222))
serverSocket.listen()
while True:
    print("Ready to serve....")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        message = message.splitlines()

        filename = str(message[0]).split(" ")[1]
        print(filename)
        f = open(filename[1:])
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        connectionSocket.send(response.encode())

        outputdata = f.read()
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        errordata = "No file"
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        response += "<h1>test error: No such file</h1>"
        connectionSocket.send(response.encode())
        connectionSocket.close()

serverSocket.close()
