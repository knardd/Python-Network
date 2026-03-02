import routeros_api

def get_connection():
    return routeros_api.RouterOsApiPool(
        '192.168.32.1', 
        username='admin', 
        password='1',
        plaintext_login=True
    )

def tambah_bridge(nama_bridge):
    connection = get_connection()
    api = connection.get_api()
    
    # Menuju ke menu /interface/bridge
    resource = api.get_resource('/interface/bridge')
    
    # Menjalankan perintah 'add'
    resource.add(name=nama_bridge)
    
    print(f"--- Bridge '{nama_bridge}' berhasil dibuat ---")
    connection.disconnect()

def tambah_ip(interface, ip_address):
    connection = get_connection()
    api = connection.get_api()
    
    # Menuju ke menu /ip/address
    resource = api.get_resource('/ip/address')
    
    # Menjalankan perintah 'add'
    resource.add(interface=interface, address=ip_address)
    
    print(f"--- IP {ip_address} berhasil dipasang di {interface} ---")
    connection.disconnect()

# --- CARA MENJALANKANNYA ---

# 1. Tanya user mau ngapain
print("Menu MikroTik API:")
print("1. Tambah Bridge")
print("2. Tambah IP Address")
pilihan = input("Pilih menu (1/2): ")

if pilihan == "1":
    nama = input("Masukkan nama bridge baru: ")
    tambah_bridge(nama)
elif pilihan == "2":
    iface = input("Masukkan interface (contoh: ether1): ")
    ip = input("Masukkan IP (contoh: 10.10.10.1/24): ")
    tambah_ip(iface, ip)
else:
    print("Pilihan tidak ada.")