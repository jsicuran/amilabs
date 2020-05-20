###Python 3.x version of David Bombal Python for network engineers video 11
###Jeff S. 4/17
import paramiko
import time

ip_address = "10.1.1.2"
username = "admin"
password = "admin"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print("Successful connection", ip_address)

remote_connection = ssh_client.invoke_shell()
remote_connection.send("send *** python is programming me!!! *****\n")
remote_connection.send("configure terminal\n")


for n in range (2,21):
    print("Creating VLAN " + str(n))
    remote_connection.send("vlan " + str(n) +  "\n")
    remote_connection.send("name Python_VLAN " + str(n) +  "\n")
    time.sleep(0.5)

remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print (output)

ssh_client.close