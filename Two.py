import os

ip = "8.8.8.8"
response = os.system(f"ping -n 1 {ip}")

if (response == 0):
    print(ip, "up")
else:
    print(ip, "down")

ipUser = input("Masukkan IP: ")
response = os.system(f"ping -n 1 {ipUser}")

if (response == 0):
    print("HOST UP")
else:
    print("HOST DOWN")

ipList = ['8.8.8.8', '192.168.32.1', '1.1.1.1', '192.168.0.200', '192.168.0.100']

for ip in ipList:
    response1 = os.system(f"ping -n 1 {ip}")
    if (response1 == 0):
        print(ip, "UP")
    else:
        print(ip, "DOWN")
