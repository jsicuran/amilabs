#####################################################################
#  PySimpleGUI uses main thread only by default                     #
#  Use multi-threading for Netmiko if necessary                     #
#  ***FNBLI DEV-OPS CORE SWITCH LOOKING GLASS APPLICATION***        #
#  MAY 2020 Applied Methodologies, Inc                              #
#  Author: Jeff Sicuranza                                           #
#  Purpose built hard coded to switch IP version                    #
#  IDE(PyCharm) based and complied runtime versions available       #
#####################################################################


#########
#IMPORTS#
#########

#import PySimpleGUIWeb as sg ---> FOR WEB VERSION

import PySimpleGUI as sg
import os
import sys
import netmiko
import getpass
import json

##### connect to switch ####

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
#########PYSIMPLEGUI TKINTER VERSION###########
###################LOGIN TO SWITCH POP OPTIONAL IN NEXT VERSION#################

###Pseudos and TO DOs##############################################################################################
### REFERESHERS - IMPORTANT You will NOT see what you print until you call either window.read or window.Refresh.
### If you want to immediately see what was printed, call window.Refresh() immediately after your print statement.
### click login button -- popup for IP and creds of switch
### enter creds
### error check
### success = popup disappears
### blinking connected status on app main window appears or changes from disconnected to connected
#####look into sg.output formatting vs. Json.
####print (json.dumps(ios_output, indent=4))
####TOOL TIPS
#### WINDOW AUTO RE-SIZE
####Disconnect session/release cleanup 

####################################################################################################################

#########MAIN APPLICATION################################
###WINDOW LAYOUT#####

sg.theme('Green')

layout = [  [sg.Text('FNBLI CORE SWITCH #1 @ 10.200.100.230', font=("bold", 15))],
            #[sg.Button('LOGIN TO A SWITCH', button_color=('white', 'green'), size=(20,2))],
            [sg.Text('INTERFACES - CONSOLE LOG - VLAN - VRRP - IP ASSIGNMENTS:', font=("bold"))],
            [sg.Button('CONNECTED NEIGHBORS'), sg.Button('INTERFACE ASSIGNMENTS'), sg.Button('INTERFACE PORT UTILIZATION'), sg.Button('REAL TIME INTERFACE STATISTICS'), sg.Button('VLAN ASSIGNMENTS'), sg.Button('SWITCH LOG', tooltip='Switch Log from most recent to old', button_color=('white', 'red'))],
            [sg.Button('VRRP CONFIG'), sg.Button('VRRP SUMMARY'), sg.Button('IP ASSIGNMENTS'), sg.Button('ARP TABLE')],
            [sg.Text('DISTRIBUTED TRUNKING/SPANNING TREE:', font=("bold"))],
            [sg.Button('DTS STATUS'), sg.Button('DTS CONFIG'), sg.Button('DTS PEER KEEPALIVE'), sg.Button('DTS CONSISTENCY'), sg.Button('SWITCH INTERCONNECT'), sg.Button('LACP'), sg.Button('LACP PEERS'), sg.Button('STP INCONSISTENT PORTS'), sg.Button('STP SUMMARY')],
            [sg.Text('BGP AND ROUTING:', font=("bold"))],
            [sg.Button('IP ROUTING TABLE'), sg.Button('ROUTE SUMMARY'), sg.Button('BGP TABLE'), sg.Button('BGP SUMMARY'), sg.Button('BGP GENERAL DETAILS'), sg.Button('BGP NEIGHBOR'), sg.Button('BGP NEIGHBOR DETAILS'), sg.Button('BGP LOGGING'), sg.Button('BGP AS PATH')],
            [sg.Button('BOLT-ON VLAN STATS'), sg.Button('CC PtP VLAN STATS'), sg.Button('FISERV SPECIFIC 1'), sg.Button('FISERV SPECIFIC 2'), sg.Image(r'C:\Users\jsicu\Downloads\FNBLI.png', size=(398, 96), pad=(80,0))],
            [sg.Button('Clear', tooltip='Clears window below'), sg.Button('Exit', tooltip='EXIT Application')],
            [sg.Text('Enter CLI Command', font=("bold")), sg.InputText(key='-CLI-'), sg.Button('Submit')],
            [sg.Text('Enter REST API Command', font=("bold")), sg.InputText(key='-REST-'), sg.Text('JSON-RPC - Coming Soon')],
            [sg.Output(size=(155, 32), key='-OUTPUT-')]]
            #####look into sg.output formatting vs. Json.
            ####print (json.dumps(ios_output, indent=4))

window = sg.Window('FNBLI CORE SWITCH LOOKING GLASS V1.1', layout)

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
    if event == 'CONNECTED NEIGHBORS':
        window['-OUTPUT-'].update(net_connect.send_command('sh lldp in rem '))
    if event == 'INTERFACE ASSIGNMENTS':
        window['-OUTPUT-'].update(net_connect.send_command('sid '))
    if event == 'INTERFACE PORT UTILIZATION':
        window['-OUTPUT-'].update(net_connect.send_command('sh interfaces port-utilization '))
    if event == 'REAL TIME INTERFACE STATISTICS':
        window['-OUTPUT-'].update(net_connect.send_command('sh interface status '))
    if event == 'VLAN ASSIGNMENTS':
        window['-OUTPUT-'].update(net_connect.send_command('sh vlan '))
    if event == 'SWITCH LOG':
        window['-OUTPUT-'].update(net_connect.send_command('sh logging -r '))
    if event == 'VRRP CONFIG':
        window['-OUTPUT-'].update(net_connect.send_command('sh vrrp config global '))
    if event == 'VRRP SUMMARY':
        window['-OUTPUT-'].update(net_connect.send_command('sh vrrp summary '))
    if event == 'IP ASSIGNMENTS':
        window['-OUTPUT-'].update(net_connect.send_command('sh ip '))
    if event == 'ARP TABLE':
        window['-OUTPUT-'].update(net_connect.send_command('sh arp  '))
    if event == 'DTS STATUS':
        window['-OUTPUT-'].update(net_connect.send_command('sh distributed-trunking status '))
    if event == 'DTS CONFIG':
        window['-OUTPUT-'].update(net_connect.send_command('sh distributed-trunking config '))
    if event == 'DTS PEER KEEPALIVE':
        window['-OUTPUT-'].update(net_connect.send_command('sh distributed-trunking peer-keepalive '))
    if event == 'DTS CONSISTENCY':
        window['-OUTPUT-'].update(net_connect.send_command('sh distributed-trunking consistency-parameters trunk trk1 '))
    if event == 'SWITCH INTERCONNECT STATUS':
        window['-OUTPUT-'].update(net_connect.send_command('sh switch-interconnect '))
    if event == 'LACP':
        window['-OUTPUT-'].update(net_connect.send_command('sh lacp '))
    if event == 'LACP PEERS':
        window['-OUTPUT-'].update(net_connect.send_command('sh lacp peer '))
    if event == 'STP INCONSISTENT PORTS':
        window['-OUTPUT-'].update(net_connect.send_command('sh spanning-tree inconsistent-ports '))
    if event == 'STP SUMMARY':
        window['-OUTPUT-'].update(net_connect.send_command('sh spanning-tree  '))
    if event == 'IP ROUTING TABLE':
        window['-OUTPUT-'].update(net_connect.send_command('sh ip route '))
    if event == 'ROUTE SUMMARY':
        window['-OUTPUT-'].update(net_connect.send_command('sh ip route summary '))
    if event == 'BGP TABLE':
        window['-OUTPUT-'].update(net_connect.send_command('sh ip bgp '))
    if event == 'BGP SUMMARY':
        window['-OUTPUT-'].update(net_connect.send_command('sh ip bgp sum '))
    if event == 'BGP GENERAL DETAILS':
        window['-OUTPUT-'].update(net_connect.send_command('show ip bgp general '))
    if event == 'ISIS Database':
        window['-OUTPUT-'].update(net_connect.send_command('sh isis database '))
    if event == 'BGP NEIGHBOR':
        window['-OUTPUT-'].update(net_connect.send_command('sh ip bgp neighbor '))
    if event == 'BGP NEIGHBOR DETAILS':
        window['-OUTPUT-'].update(net_connect.send_command('sh ip bgp neighbor detail'))
    if event == 'BGP LOGGING':
        window['-OUTPUT-'].update(net_connect.send_command('sh logging bgp '))
    if event == 'BGP AS PATH':
        window['-OUTPUT-'].update(net_connect.send_command('sh ip bgp route as-path '))
    if event == 'FISERV SPECIFIC 1':
        window['-OUTPUT-'].update('TO BE ADDED')
    if event == 'FISERV SPECIFIC 2':
        window['-OUTPUT-'].update('TO BE ADDED')
    if event == 'BOLT-ON VLAN STATS':
        window['-OUTPUT-'].update('TO BE ADDED')
    if event == 'CC PtP VLAN STATS':
        window['-OUTPUT-'].update('TO BE ADDED')

window.close()

###############
####END RUN####
###############




