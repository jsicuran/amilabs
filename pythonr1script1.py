

#### Windows 10 and Python V3.x example GNS3 Talks: Python for Network Engineers with GNS3 (Part 1)
##### David Bombel's training Session
##### tested Jeff Sicuranza 4/17 using Windows 10, Python 3 and VIRAL LAB via FLAT network

import os
import getpass
import sys
import telnetlib

def cls():
  os.system('cls')


cls()
HOST = "10.1.1.10"
#user = raw_input("Enter your telnet username: ")
user = input("Username:")
password = getpass.getpass()
tn = telnetlib.Telnet(HOST)


tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password: 
	tn.read_until(b"Password: ") 
	tn.write(password.encode('ascii') + b"\n")
tn.write(b"enable\n")
tn.write(b"amilabs\n")
tn.write(b"conf t\n")
os.system('color E')
print("*****APPLYING CONFIGURATION - STANDBY******")
tn.write(b"int loop 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"int loop 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
print("*****FINISHED APPLYING CONFIGURATION******")
os.system('color F')
cont = input("Write Configuration? y/n > ")
if cont == "y":
	tn.write(b"wri mem\n")
	print("***Saving Configuration****")
else:      
    tn.write(b"exit\n")
os.system('color F')
print("****Terminating Telnet Session****")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))
#exit() will or will not work depending on windows and python 3.x version 





#tn.write("enable\n")
#tn.write("amilabs\n")
#tn.write("conf t\n")
#tn.write("int loop 0\n")
#tn.write("ip address 1.1.1.1 255.255.255.255\n")

#tn.write("end\n")
#tn.write("exit\n")


