####
#PySimpleGUI usese main thread only by default
#Use multi-threading for Netmiko



#########
#IMPORTS#
#########

#import PySimpleGUIWeb as sg

import PySimpleGUI as sg
import netmiko
import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import os
import sys


#####HPProcurveSSH
##### connect to lab switch ####
from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'hp_procurve',
    'ip': '192.168.1.5',
    'username': 'test',
    'password': 'test',
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
### sg.Image(r'C:\Users\jsicu\Downloads\FNBLI.png', size=(398, 96))
sg.theme('Green')

#frame_layout = [ [sg.T('VXLAN')]]

layout = [  [sg.Text('Enter IP Address:')],
                 [sg.InputText(key='-IP-')],
                 [sg.Text('Switch Credentials(SSH ONLY):')],
                 [sg.Text('Enter Username:')],
                 [sg.InputText(key='-USER-')],
                 [sg.Text('Enter Password:')],
                 [sg.InputText(key='-PWD-')],
                 [sg.Submit(), sg.Cancel(), sg.Button('Disconnect')],
                 [sg.Text('Connection Status:')],
                 [sg.Output(size=(10, 10), key='-OUTPUT1-')],

            #[sg.Button('LOGIN TO A SWITCH', button_color=('white', 'green'), size=(20,2))],
            [sg.Text('FABRIC OVERLAY Detail:')],
            [sg.Button('BGP Summary'), sg.Button('BGP MAC Routes'), sg.Button('Layer2 MAC Routes'), sg.Button('BGP NLRI Type 2'), sg.Button('BGP Neighbors')],
            [sg.Text('VXLAN NVE/VNI Detail:')],
            #[sg.Frame('', frame_layout)],
            [sg.Button('VXLAN'), sg.Button('VXLAN Interfaces'), sg.Button('VNI'), sg.Button('NVE Peers'), sg.Button('NVE Peer Detail')],
            [sg.Button('L2FWDR Mac'), sg.Button('L2RIB Topology History'), sg.Button('L2RIB Error Logs')],
            [sg.Text('FABRIC UNDERLAY Detail:')],
            [sg.Button('ISIS Adjacency'), sg.Button('ISIS Routing'), sg.Button('ISIS Topology'), sg.Button('ISIS Database'), sg.Button('ISIS Database Detail')],

            [sg.Button('Clear'), sg.Button('Exit')],

            [sg.Text('Enter CLI Command'), sg.InputText(key='-CLI-'), sg.Button('Submit')],
            [sg.Text('Enter REST API Command'), sg.InputText(key='-REST-'), sg.Text('JSON-RPC - Coming Soon')],
            [sg.Output(size=(140, 38), key='-OUTPUT-')]]
            #[sg.In(key='-IN-')]]
            #print (json.dumps(ios_output, indent=4))


window = sg.Window('FNBLI CORE SWITCH Looking Glass', layout)

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
        window['-OUTPUT-'].update(net_connect.send_command('sh ip route '))
    if event == 'BGP MAC Routes':
        window['-OUTPUT-'].update(net_connect.send_command('sh ip '))
    if event == 'Layer2 MAC Routes':
        window['-OUTPUT-'].update(net_connect.send_command('sid'))
    if event == 'BGP NLRI Type 2':
        window['-OUTPUT-'].update(net_connect.send_command('sh int port-util '))
    if event == 'BGP Neighbors':
        window['-OUTPUT-'].update(net_connect.send_command('sh vrrp sum '))
    if event == 'VXLAN':
        window['-OUTPUT-'].update(net_connect.send_command('sh ip bgp nei '))
    if event == 'VXLAN Interfaces':
        window['-OUTPUT-'].update(net_connect.send_command('sh ip bgp summary'))
    if event == 'VNI':
        window['-OUTPUT-'].update(net_connect.send_command('sh distributed-trunking status '))
    if event == 'NVE Peers':
        window['-OUTPUT-'].update(net_connect.send_command('sh vlan '))
    if event == 'NVE Peer Detail':
        window['-OUTPUT-'].update(net_connect.send_command('sh logging -r '))
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