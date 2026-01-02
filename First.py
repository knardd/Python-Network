router_ip = "192.168.32.1"
print("IP Router: ", router_ip)

status = "UP"
if (status == "UP"):
    print("Status Router: ", status)
else:
    print("Status Router: Router Offline")

ip = ['192.168.32.1', '192.168.32.2', '192.168.32.3']
for i in ip:
    print("Ping ke: ", i)

def ping_router(ip):
    print("Ping ke: ", ip, "berhasil")

    ping_router("192.168.32.4")

try:
    x = int(input("Masukkan Port: "))
    print("Port: ", x)
except:
    print("Error: harus angka")

