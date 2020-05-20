####
#PySimpleGUI usese main thread only by default
#Use multi-threading for Netmiko



########
#imports
########
import PySimpleGUI as sg
import netmiko
import getpass

##### connect to lab evpn switch ####
from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.1',
    'username': 'admin',
    'password': 'admin',
}


#def evpn():
net_connect = ConnectHandler(**iosv_l2_s1)
output = net_connect.send_command('sh l2route evpn mac all ')

#########################################################

############ LAUNCH GUI ################

###################LOGIN TO SWITCH POPUP#################



#########################################################

#########MAIN APPLICATION################################


sg.theme('Light Blue')

layout = [  [sg.Text('BGP-EVPN Detail:')],
            [sg.Button('BGP Summary'), sg.Button('BGP MAC Routes'), sg.Button('Layer2 MAC Routes'), sg.Button('BGP NLRI Type 2'), sg.Button('BGP Neighbors')],
            [sg.Text('VXLAN NVE/VNI Detail:')],
            [sg.Button('VXLAN'), sg.Button('VXLAN Interfaces'), sg.Button('VNI'), sg.Button('NVE Peers'), sg.Button('NVE Peer Detail')],
            [sg.Text('ISIS Underlay Detail:')],
            [sg.Button('ISIS Adjacency'), sg.Button('ISIS Routing'), sg.Button('ISIS Topology'), sg.Button('ISIS Database'), sg.Button('ISIS Database Detail')],

            [sg.Button('Clear'), sg.Button('Exit')],

            [sg.Text('Enter CLI Command'), sg.In(key='-IN-')],
            [sg.Output(size=(70,40), key='-OUTPUT-')]]
            #[sg.In(key='-IN-')]]


window = sg.Window('BGP EVPN Monitor Utility', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Clear':
        window['-OUTPUT-'].update('')
    if event == 'BGP Summary':
        window['-OUTPUT-'].update(net_connect.send_command('sh bgp l2vpn evpn summ '))
    if event == 'BGP MAC Routes':
        window['-OUTPUT-'].update(net_connect.send_command('sh bgp l2vpn evpn '))
    if event == 'Layer2 MAC Routes':
        window['-OUTPUT-'].update(net_connect.send_command('sh l2route mac all'))
    if event == 'BGP NLRI Type 2':
        window['-OUTPUT-'].update(net_connect.send_command('sh bgp l2vpn evpn route-type 2 '))
    if event == 'BGP Neighbors':
        window['-OUTPUT-'].update(net_connect.send_command('sh bgp l2vpn evpn neighbors '))
    if event == 'VXLAN':
        window['-OUTPUT-'].update(net_connect.send_command('sh vxlan '))
    if event == 'VXLAN Interfaces':
        window['-OUTPUT-'].update(net_connect.send_command('sh vxlan interface '))
    if event == 'VNI':
        window['-OUTPUT-'].update(net_connect.send_command('sh nve vni '))
    if event == 'NVE Peers':
        window['-OUTPUT-'].update(net_connect.send_command('sh nve peers '))
    if event == 'NVE Peer Detail':
        window['-OUTPUT-'].update(net_connect.send_command('sh nve peers detail '))
    if event == 'ISIS Adjacency':
        window['-OUTPUT-'].update(net_connect.send_command('sh isis adjacency '))
    if event == 'ISIS Routing':
        window['-OUTPUT-'].update(net_connect.send_command('sh isis route detail '))
    if event == 'ISIS Topology':
        window['-OUTPUT-'].update(net_connect.send_command('sh isis topology '))
    if event == 'ISIS Database':
        window['-OUTPUT-'].update(net_connect.send_command('sh isis database '))
    if event == 'ISIS Database Detail':
        window['-OUTPUT-'].update(net_connect.send_command('sh isis database detail '))


window.close()

###############
####END RUN####
###############




