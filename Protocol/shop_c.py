import socket
import os
import calendar
import time

host = '127.0.0.1'
port = 5000

s = socket.socket()
s.connect((host, port))

print("สวัสดีครับ \nสนใจสินค้าอะไรครับ")

loop = True

while loop:
    message = input("-> ")
    s.send(bytes(message, "utf-8"))
    
    Server_data3 = s.recv(1024)
    Server_data4 = "" 
    Server_data4 = Server_data3.decode("utf-8")
    if Server_data4 == "กรุณาเลือกสินค้าใหม่นะครับ":
        os.system("cls")
        print(Server_data4)
        time.sleep(3)
        loop = True
    elif Server_data4 == "10":
        os.system("cls")
        print(Server_data4[:50])
    elif Server_data4 == 10 :
        print("")