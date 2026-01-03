import paramiko
import os
import socket

ip = "192.168.32.1"
username = "admin"
password = "password"
port = 22

command = [
    "ip address print",
    "ip dhcp-client add interface=ether1",
    "ip address add address=192.168.32.1/24 interface=ether2",
    "ip address print",
    "ip dhcp-server add interface=ether2",
    "ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade",
]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(ip, username=username, password=password, port=port, timeout=5)
    print("Connection To Mikrotik", ip)

    for cmd in command:
        print("Command: ", cmd)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        output = stdout.read().decode()
        error = stderr.read().decode()

        if output:
            print(output)
        if error:
            print(error)

except Exception as e:
    print("Connection Failed", e)
finally:
    ssh.close()
    print("\n[+] SSH connection ditutup")
