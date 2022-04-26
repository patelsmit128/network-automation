import getpass
import sys
import telnetlib
import paramiko
import time

username="cisco"
password=getpass.getpass()
f=open("myswitches.txt")

for line in f:
	ip_address=line.strip()
	ssh_client=paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=ip_address,username=username,password=password)
	print("success "+ip_address)
	remote_connection = ssh_client.invoke_shell()
	print("success running config"+ip_address)
	remote_connection.send(b"enable\n")
	remote_connection.send(b"cisco\n")
	remote_connection.send(b"conf t\n")
	remote_connection.send(b"exit\n")
	remote_connection.send(b"terminal length 0\n")
	remote_connection.send(b"show run\n")
	remote_connection.send(b"exit\n")

	time.sleep(20)
   
	readoutput=remote_connection.recv(655350).decode('ascii')
	saveoutput=open("backup_switch"+ ip_address,"w")
	print("saving config in backup_switch"+ip_address+"\n")
	saveoutput.write((readoutput))
	saveoutput.write("\n")
	saveoutput.close
	

