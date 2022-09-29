import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Server hostname or ip? ")
port = int(input("Server port? "))
sock.connect((host, port))
data = sock.recv(4096).decode("utf-8").split(",")
print(data)
print(f"{data[0]}\n{data[1]} {data[2]}")
while True:
    data1 = input("message: ")
    sock.send(bytes(f"{data1},{data[2]},{data[3]},{data[4]}","utf-8"))
    response = sock.recv(4096).decode("utf-8").split(",")
    print(f"{response[0]}\n{response[1]}")
    exiton = data1.upper()
    if exiton == "EXIT" :
        break