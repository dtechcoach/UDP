#UDPClient.py

from socket import socket, SOCK_DGRAM, AF_INET

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input lowercase sentence: ')
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, addr = clientSocket.recvfrom(2048)
print modifiedMessage, addr
clientSocket.close()

#Allow the client to give up if no response has been reveived within 1 second.