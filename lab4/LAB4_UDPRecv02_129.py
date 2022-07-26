import socket
import sys
HOST = ''
PORT = 8888
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket created")
except socket.error as emsg:
    print("Failed to create socket. Error Code : " + str(emsg[0]) + " Message " + emsg[1])
    sys.exit()
try:
    s.bind((HOST, PORT))
except socket.error as emsg:
    print("Bind failed. Error Code : " + str(emsg[0]) + " Message " + emsg[1])
    sys.exit()
print("Socket bind complete")
while 1:
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
    if not data:
        break
    reply = "OK..." + data.decode("utf-8")
    s.sendto(bytes(reply,"utf-8"), addr)
    print("Message[" + addr[0] + ":" + str(addr[1]) + "] - " + (data.decode("utf-8")).strip())
    exiton = (data.decode("utf-8")).upper()
    if exiton == "EXIT" :
        print("........................bye.........................")
        sys.exit()
s.close()
