from distutils.log import error
from http import client
from logging.config import listen
import socket
import threading
import os
import time
class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        clientnumber = 0
        print("---------------Wait Client-------------------")
        self.sock.listen(1)
        while True:
            clientnumber += 1
            client, address = self.sock.accept()
            print("Client Connected","address = ", address[0],"Port = ",address[1],"อันดับการติดต่อ", str(clientnumber))
            clientconnect = "Welcome to Server ON"
            clientconnect1 = "อันดับการติดต่อ"
            client.send(bytes(f"{clientconnect},{clientconnect1},{str(clientnumber)},{address[0]},{address[1]}","utf-8"))
            client.settimeout(60)
            threading.Thread(target=self.listenToClient,
                             args=(client, address)).start()

    def listenToClient(self, client, address):
        size = 4096
        while True:
            try:
                data = client.recv(size).decode("utf-8").split(",")
                if data:
                    # Set the response to echo back the recieved data
                    print(f"อันดับเครื่องที่ส่ง {data[1]} IP = {data[2]} Port = {data[3]}\nข้อความที่ส่งมา = {data[0]}")
                    print("----------------------------------------------------------------------------")
                    response1 = "เครืองที่ส่ง " + str(data[1])
                    response2 = "ข้อความ " + str(data[0])
                    client.send(bytes(f"{response1},{response2}","utf-8"))
                else:
                    raise error('Client disconnected')

            except:
                client.close()
                return False

if __name__ == "__main__":
    os.system("cls")
    while True:
        port_num = input("Port? ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('', port_num).listen()
