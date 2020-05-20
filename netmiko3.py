#import paramiko
#import netmiko
###Python 3.x version of David Bombal Python for network engineers video 14
###Jeff S. 4/17
from netmiko import ConnectHandler

NXOSV_2 = {
    'device_type': 'cisco_nxos',
    'ip': '10.1.1.2',
    'username': 'admin',
    'password': 'admin',
}

NXOSV_3 = {
    'device_type': 'cisco_nxos',
    'ip': '10.1.1.3',
    'username': 'admin',
    'password': 'admin',
}

NXOSV_4 = {
    'device_type': 'cisco_nxos',
    'ip': '10.1.1.4',
    'username': 'admin',
    'password': 'admin',
}

all_devices = [NXOSV_4, NXOSV_3, NXOSV_2]

with open('nxosportcfg.txt') as f:
    lines = f.read().splitlines()
print(lines)


for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    print("Configuring NXOS Switch Ports")
    output = net_connect.send_command('send *** python is programming me!!! *****')
    output = net_connect.send_config_set(lines)
    print(output) 

   
