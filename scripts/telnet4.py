import getpass
import sys
import telnetlib

HOST=input("enter device ip")
user="cisco"
password=getpass.getpass()

tn=telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"int loop 2\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"vlan database\n")


for n in range(2,10):
	tn.write(b"vlan " + bytes(str(n),'utf-8') + b"\n")

tn.write(b"exit\n")
tn.write(b"exit\n")


print(tn.read_all().decode('ascii'))
