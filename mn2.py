import time
import random
from socket import *

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
# clientSocket.bind(('', 12001))
clientAddress = ('localhost', 12000)
counter = 0
clientSocket.settimeout(1)
Avg_RTT = 0
packet_Loss_Rate = 0
min_RTT = 100
maximum_RTT = 0
sum_RTT = 0
totalTime = 0
Avg_RTT = 0
packet_loss = 0

try:
    # Receive the client packet along with the address it is coming from
    # message, address = serverSocket.recvfrom(1024)
    for i in range(1, 11):
        counter += 1
        start = time.time()
        # Ping #: Host 127.0.0.1 replied: seq 1 Tue Sep 28 23:19:27 2021, RTT = 0.00 ms
        message = "Ping " + str(i) + ": host 127.0.0.1 replied: seq " + str(i) + " " + time.ctime(
            start)
        rand_int = random.randint(10, 40)

        try:
            packetSent = clientSocket.sendto(message.encode(), ('localhost', 12000))
            time.sleep(rand_int)
            end = time.time()
            totalTime = end - start
            sum_RTT = sum_RTT + totalTime

            if totalTime > maximum_RTT:
                maximum_RTT = totalTime
            if totalTime < min_RTT:
                min_RTT = totalTime

            print(message + ", RTT = " + str(round(totalTime, 2)) + " ms")
        except clientSocket.timeout:
            print("Request Timed Out")
            packet_loss += 1

finally:
    Avg_RTT = sum_RTT / counter
    packet_Loss_Rate = (packet_loss / counter) * 100
    print("Min RTT = " + str(round(min_RTT, 2)) + " ms")
    print("Max RTT = " + str(round(maximum_RTT, 2)) + " ms")
    print("Avg RTT = " + str(round(Avg_RTT, 2)) + " ms")
    print("Packet Lost = " + str(round(packet_Loss_Rate, 2)) + " %")
    clientSocket.close()
