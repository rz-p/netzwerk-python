import socket
import time
import datetime

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create new socket
serverSocket.settimeout(0.1) # set timeout to 1 second

address = ("127.0.0.1", 12000)
start = time.time()
i = 0

for i in range(10):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    message = str.encode("ping " + st)
    serverSocket.sendto(message, address)
    print(">", i, "\n", "current time: ", start)

    try:
        data, server = serverSocket.recvfrom(1024)
        elapsed = ts - start
        print(f'{data} {elapsed}')

    except socket.timeout:
        print('REQUEST TIMED OUT')









