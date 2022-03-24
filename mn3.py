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
    for i in range(1, 7):
        counter += 1
        start = time.time()
        # Ping #: Host 127.0.0.1 replied: seq 1 Tue Sep 28 23:19:27 2021, RTT = 0.00 ms
        message = "Ping " + str(i) + ": host 127.0.0.1 replied: seq " + str(i) + " " + time.ctime(
            start)
        delay_int = random.randint(1,10)
        packet_Loss_Int = random.randint(1, 10)

        try:
            packetSent = clientSocket.sendto(message.encode(), ('localhost', 12000))
            time.sleep(delay_int)
            end = time.time()
            totalTime = end - start
            sum_RTT = sum_RTT + totalTime

            print(str(packet_Loss_Int))

            # Packet Loss Counter
            if packet_Loss_Int == (1 and 2):
                print("Ping " + str(i) + ": timed out, message was lost")
                packet_loss += 1
                continue

            # Min and Max RTT
            if totalTime > maximum_RTT:
                maximum_RTT = totalTime
            if totalTime < min_RTT:
                min_RTT = totalTime

            print(message + ", RTT = " + str(round(totalTime, 2)) + " ms")

        except clientSocket.timeout:
            print("Request Timed Out")

finally:
    # Average and Loss Rate Calculation
    Avg_RTT = sum_RTT / counter
    packet_Loss_Rate = (packet_loss / counter) * 100

    print("Min RTT = " + str(round(min_RTT, 2)) + " ms")
    print("Max RTT = " + str(round(maximum_RTT, 2)) + " ms")
    print("Avg RTT = " + str(round(Avg_RTT, 2)) + " ms")
    print("Packet Lost = " + str(packet_Loss_Rate) + " %")
    clientSocket.close()
