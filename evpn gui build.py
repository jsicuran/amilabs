####
#PySimpleGUI usese main thread only by default
#Use multi-threading for Netmiko



########
#imports
########
import PySimpleGUI as sg
import netmiko
import getpass
import json

##### connect to lab evpn switch ####
from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.1',
    'username': 'admin',
    'password': 'admin',
}
net_connect = ConnectHandler(**iosv_l2_s1)


#########################################################

############ LAUNCH GUI #################################

###################LOGIN TO SWITCH POPUP#################
###Pseudo
### click login button -- popup for IP and creds of switch
### enter creds
### error check
### success = popup disappears
### blinking connected status on app main window appears or changes from disconnected to connected


#########################################################

#########MAIN APPLICATION################################
###WINDOW LAYOUT#####

sg.theme('Light Blue')

layout = [  [sg.Text('BGP-EVPN Detail:')],
            [sg.Button('LOGIN TO A SWITCH', button_color=('white', 'green'), size=(20,2))],
            [sg.Text('FABRIC OVERLAY Detail:')],
            [sg.Button('BGP Summary'), sg.Button('BGP MAC Routes'), sg.Button('Layer2 MAC Routes'), sg.Button('BGP NLRI Type 2'), sg.Button('BGP Neighbors')],
            [sg.Text('VXLAN NVE/VNI Detail:')],
            [sg.Button('VXLAN'), sg.Button('VXLAN Interfaces'), sg.Button('VNI'), sg.Button('NVE Peers'), sg.Button('NVE Peer Detail')],
            [sg.Button('L2FWDR Mac'), sg.Button('L2RIB Topology History'), sg.Button('L2RIB Error Logs')],
            [sg.Text('FABRIC UNDERLAY Detail:')],
            [sg.Button('ISIS Adjacency'), sg.Button('ISIS Routing'), sg.Button('ISIS Topology'), sg.Button('ISIS Database'), sg.Button('ISIS Database Detail')],

            [sg.Button('Clear'), sg.Button('Exit')],

            [sg.Text('Enter CLI Command'), sg.InputText(key='-CLI-'), sg.Button('Submit')],
            [sg.Text('Enter REST API Command'), sg.InputText(key='-REST-'), sg.Text('JSON-RPC - Coming Soon')],
            [sg.Output(size=(132,40), key='-OUTPUT-')]]
            #[sg.In(key='-IN-')]]


window = sg.Window('JEFFs BGP EVPN Looking Glass Utility', layout)

while True:             # MAIN Event Loop
    event, values = window.read()
    print(event, values)   # Leave active to test button dictionary value
    if event in (None, 'Exit'):
        break
    if event == 'Clear':
        window['-OUTPUT-'].update('')
    if event == 'Submit':
        cli_command = values['-CLI-']
        window['-OUTPUT-'].update(net_connect.send_command(cli_command))
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
    if event == 'L2FWDR Mac':
        window['-OUTPUT-'].update(net_connect.send_command('sh system internal l2fwder mac  '))
    if event == 'L2RIB Topology History':
        window['-OUTPUT-'].update(net_connect.send_command('sh system internal l2rib event-history topology '))
    if event == 'L2RIB Error Logs':
        window['-OUTPUT-'].update(net_connect.send_command('sh system internal l2rib event-history error '))
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




