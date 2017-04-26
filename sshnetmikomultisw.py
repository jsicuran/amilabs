#import paramiko
#import netmiko
###Python 3.x version of David Bombal Python for network engineers video 13
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

all_devices = [NXOSV_2, NXOSV_3, NXOSV_4]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    print("Configuring NXOS VLANS")
    output = net_connect.send_command('send *** python is programming me!!! *****')
    for n in range (2,11):
        print("Creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)
