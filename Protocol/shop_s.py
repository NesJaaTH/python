import socket 
import calendar
import os
import time

host = '127.0.0.1'
port = 5000

s = socket.socket()
s.bind((host, port))
    
s.listen(5)
c, addr = s.accept()
print("Connection from: " + str(addr))
print("wellcom to shop")

loop = True

while loop:
    data1 = c.recv(1024)
    data = ''
  
    data = data1.decode("utf-8")

    message = input("-> ")
    c.send(bytes(message, "utf-8"))
    if data == "กางเกง":
        print("from connected user: " + data)
        c.send(bytes("จำนวนครับ", "utf-8"))
        loop = True
    else:
        c.send(bytes("กรุณาเลือกสินค้าใหม่นะครับ", "utf-8"))
        loop = True