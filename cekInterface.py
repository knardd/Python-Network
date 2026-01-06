import paramiko
import os
import socket
import time
from scp import SCPClient

ip = "192.168.32.1"
username = "admin"
password = "1"
port = 22

command = [
    "/ip address print",
    "/ip dhcp-client add interface=ether1",
    "/ip address print",
    "/ip pool add name=pool-lan ranges=192.168.32.10-192.168.32.100",
    "/ip dhcp-server add name=dhcp-lan interface=ether2 address-pool=pool-lan disabled=no",
    "/ip dhcp-server network add address=192.168.32.0/24 gateway=192.168.32.1 dns-server=8.8.8.8",
    "/ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade",
    "/ping 8.8.8.8 count=3",
    "/system backup save name=backup-awal",
    "/export file=config-awal",
]

start_time = time.time()

#Ping Check
def ping_check(ip):
    print("[*] Pinging router...")
    response = os.system(f"ping -n 1 {ip} > nul")
    return response == 0

#SSH Port Check
def ssh_port_check(ip, port):
    print("[*] Checking SSH port...")
    try:
        sock = socket.create_connection((ip, port), timeout=3)
        sock.close()
        return True
    except:
        return False

#SSH Config
def run_ssh_config():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password, port=port, timeout=5)
    print("Connection To Mikrotik", ip)

    for cmd in command:
        print("Command: ", cmd)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        time.sleep(5)

        output = stdout.read().decode()
        error = stderr.read().decode()

        if output:
            print(output)
        if error:
            print(error)

    print("[*] Downloading backup via SCP...")

    scp = SCPClient(ssh.get_transport())
    scp.get("backup-awal.backup")
    scp.get("config-awal.rsc")
    scp.close()

    print("[+] Backup & export berhasil di-download")
        
    ssh.close()
    print ("SSH connection closed")

#Main Flow
if not ping_check (ip):
    print("Router tidak bisa diping. Cek kabel / IP.")
    exit()

if not ssh_port_check(ip, port):
    print("Port 22 SSH tertutup. Enable SSH dulu di Mikrotik.")
    exit()

print("Router reachable & SSH open")
run_ssh_config()

end_time = time.time()
total_time = end_time - start_time
print("Total Waktu: ", total_time , "detik")