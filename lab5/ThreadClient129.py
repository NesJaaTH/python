import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Server hostname or ip? ")
port = int(input("Server port? "))
sock.connect((host, port))
while True:
    data1 = sock.recv(1024)
    print(data1.decode("utf-8"))
    data = input("message: ")
    sock.send((data).encode("utf-8"))
    print("response: ", sock.recv(1024).decode("utf-8"))
    exiton = data.upper()
    if exiton == "EXIT" :
        break