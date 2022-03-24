import time
from socket import *

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
# clientSocket.bind(('', 12001))
clientAddress = ('127.0.0.1', 12000)
counter = 0
clientSocket.settimeout(3)

for i in range(0, 11)
    try:
        message = "Testing" + str(i)
        packetSend = str.end(message)
        clientSocket.sendto(packetSend, clientAddress)
        response = clientSocket.recvfrom(1024)
        msg = "Sent :" + message + " Received :" + response[0].decode("utf-8")
        print(msg)
    except
        print("Request Timed Out")