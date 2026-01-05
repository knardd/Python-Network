import socket
import os

ip = "8.8.8.8"
port = 22

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

result = s.connect_ex((ip, port))

if (result == 0):
    print("Port", port, "open")
else:
    print("Port", port, "closed")
    
s.close()


ip = input("Masukkan IP: ")

response = os.system(f"ping -n 1 {ip}")

if (response == 0):
    print("Host", ip, "up")
else:
    print("Host", ip, "down")

port = 22
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

if (s.connect_ex((ip, port)) == 0):
    print("Port", port, "open")
else:
    print("Port", port, "closed")
    
s.close()