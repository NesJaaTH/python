import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    message = input("-> ")
    while message != 'q':
        s.send(bytes(message, "utf-8"))
        data = s.recv(1024)
        data1 = ''
        data1 += data.decode("utf-8")
        print("Received from server: " + data1)
        message = input("-> ")
    s.close()

if __name__ == '__main__':
    Main()