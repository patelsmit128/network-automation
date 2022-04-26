import paramiko
import time

ip_address="10.10.10.9"
username="cisco"
password="cisco"

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print("successful connection",ip_address)

remote_connection = ssh_client.invoke_shell()

remote_connection.send(b"configure terminal\n")
remote_connection.send(b"enable\n")
remote_connection.send(b"cisco\n")
remote_connection.send(b"conf t\n")
remote_connection.send(b"int loop 0\n")
remote_connection.send(b"ip address 1.1.1.1 255.255.255.255\n")
remote_connection.send(b"int loop 1\n")
remote_connection.send(b"ip address 2.2.2.2 255.255.255.255\n")
remote_connection.send(b"router ospf 1\n")
remote_connection.send(b"network 0.0.0.0 255.255.255.255 area 0\n")
remote_connection.send(b"exit\n")

remote_connection.send(b"vlan database\n")

for n in range(2,12):
	print("creating VLAN" + str(n))
	remote_connection.send(b"vlan " + bytes(str(n),'utf-8') + b"\n")
	time.sleep(0.5)

remote_connection.send(b"exit\n")
remote_connection.send(b"exit\n")
time.sleep(10)
output=remote_connection.recv(65535)
print(output)
ssh_client.close




