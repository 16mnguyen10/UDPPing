import random
from socket import *

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
while True:
 # run-time screen captures for a sequence consists of 10 pings
 packets = random.randint(0, 10)
 # Receive the client packet along with the address it is coming from
 message, address = serverSocket.recvfrom(1024)
 if packets < 4:
  continue
 # The server responds
 serverSocket.sendto(message, address)