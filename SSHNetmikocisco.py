#import paramiko
#import netmiko
from netmiko import ConnectHandler

NXOSV = {
    'device_type': 'cisco_nxos',
    'ip': '10.1.1.2',
    'username': 'admin',
    'password': 'admin',
}


net_connect = ConnectHandler(**NXOSV)
#net_connect.find_prompt()
output = net_connect.send_command('show vlan')
print(output)

print("Configuring NXOS VLANS")
output = net_connect.send_command('send *** python is programming me!!! *****')

for n in range (2,11):
    print("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)
