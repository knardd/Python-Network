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