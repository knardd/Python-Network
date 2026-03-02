import routeros_api

connection = routeros_api.RouterOsApiPool('192.168.32.1', username='admin', password='1', plaintext_login=True)

api = connection.get_api()

# Mengambil daftar IP Address
list_ip = api.get_resource('/ip/address')
data = list_ip.get()

for item in data:
    print(f"Interface: {item['interface']} - IP: {item['address']}")

connection.disconnect()