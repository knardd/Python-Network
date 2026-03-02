import routeros_api

def get_connection():
    return routeros_api.RouterOsApiPool(
        '192.168.32.1', 
        username='admin', 
        password='1',
        plaintext_login=True
    )

connection = get_connection()
api = connection.get_api()

try:
    # 1. IP Address Add
    api.get_resource('/ip/address').add(
        address='192.168.0.168/24', 
        interface='ether1'
    )

    # 2. IP Route
    api.get_resource('/ip/route').add(
        gateway='192.168.0.200'
    )

    # 3. IP DNS (Menggunakan .set karena DNS sudah ada defaultnya)
    api.get_resource('/ip/dns').set(
        servers='8.8.8.8,1.1.1.1', 
        allow_remote_requests='yes'
    )

    # 4. IP Pool
    api.get_resource('/ip/pool').add(
        name='pool-lan', 
        ranges='192.168.32.5-192.168.32.100'
    )

    # 5. DHCP Server
    api.get_resource('/ip/dhcp-server').add(
        name='dhcp-lan', 
        interface='ether2', 
        address_pool='pool-lan', 
        disabled='no'
    )

    # 6. DHCP Network
    api.get_resource('/ip/dhcp-server/network').add(
        address='192.168.32.0/24', 
        gateway='192.168.32.1', 
        dns_server='8.8.8.8'
    )

    # 7. NAT Masquerade
    api.get_resource('/ip/firewall/nat').add(
        chain='srcnat', 
        out_interface='ether1', 
        action='masquerade'
    )

    # 8. Ping
    ping_res = api.get_binary_resource('/').call('ping', {'address': '8.8.8.8', 'count': '3'})
    print(ping_res)
    print("Semua konfigurasi berhasil diterapkan!")

except Exception as e:
    print(f"Terjadi kesalahan: {e}")

finally:
    connection.disconnect()