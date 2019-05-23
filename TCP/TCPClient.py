#TCPClient.py

from socket import socket, AF_INET, SOCK_STREAM
serverName = 'localhost'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = raw_input('Input lowercase sentence: ')
clientSocket.send(message)
modifiedMessage = clientSocket.recv(2048)
print 'From Server: ', modifiedMessage
clientSocket.close()
