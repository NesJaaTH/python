import time
from socket import *
import socket

for pings in range(10):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)
    message = "test"
    addr = ('127.0.0.1', 12000)

    start = time.time()
    sock.sendto(message, addr)
    try:
        data, server = sock.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print("%s %d %d" % (data, pings, elapsed))

    except timeout:
        print("REQUEST TIMED OUT")
