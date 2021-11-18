import random
from socket import *

# Create a UDP socket
# Nitce the use of SOCK_DGRAM for UDP packets

serverSocket = socket (AF_INET, SOCK_DGRAM)

serverSocket.bind(('', 12000))

while True:
    rand = random.randint(0,10)
    message, address = serverSocket.recvfrom(1024)
    print("received: ", message)
    message = message.upper()
    if rand < 4:
        print("oops!: ")
        continue
    else:
        print("send: ", message)
        serverSocket.sendto(message,address)
