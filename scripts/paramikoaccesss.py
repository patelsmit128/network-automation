import getpass
import sys
import telnetlib
import paramiko
import time

username="cisco"
password=getpass.getpass()
f=open("myswitches.txt")

for line in f:
	try:

		ip_address=line.strip()
		ssh_client=paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(hostname=ip_address,username=username,password=password)
		
		remote_connection = ssh_client.invoke_shell()
		remote_connection.send(b"exit\n")
	except:
		remote_connection=("socket.error")

	result=remote_connection

	if result=="socket.error":
		print(ip_address+" Not Accessible")
	else:
		print(ip_address+" Accessible")		
input("enter to exit")				

	
	

