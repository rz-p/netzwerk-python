import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets

serverSocket = socket (AF_INET, SOCK_DGRAM)

serverSocket.bind(('', 12000))

message_counter = 0
while True:
    rand = random.randint(0,10)
    message, address = serverSocket.recvfrom(1024)
    message_counter += 1
    print("received #", message_counter, ": ",message)
    message = message.upper()
    if rand < 4:
        print("oops! - package lost.")
        continue
    else:
        print("send back: ", message)
        serverSocket.sendto(message,address)
