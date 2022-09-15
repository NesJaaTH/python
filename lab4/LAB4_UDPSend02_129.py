import socket
import sys
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()
host = '127.0.0.1'
port = 8888
while (1):
    msg = input('Enter message to send : ')
    try:
        s.sendto(bytes(msg,"utf-8"), (host, port))
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
        print('Server reply : ' + reply.decode("utf-8"))
        exiton = msg.upper()
        if exiton == "EXIT":
            print("...............bye.....................")
            sys.exit()
    except socket.error as emsg:
        print('Error Code : ' + str(emsg[0]) + ' Message ' + emsg[1])
        sys.exit()
