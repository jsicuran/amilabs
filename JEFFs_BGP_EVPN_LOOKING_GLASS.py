############################################################################
#  PySimpleGUI uses main thread only by default                            #
#  Use multi-threading for Netmiko if necessary                            #
#  ***Jeff's DEV-OPS BGP EVPN LOOKING GLASS APPLICATION***                 #
#  JUNE 2020 Applied Methodologies, Inc                                    #
#  Author: Jeff Sicuranza                                                  #
#  LOGIN TO ANY EVPN DEVICE VERSION                                        #
#  IDE(PyCharm) based and complied runtime versions available              #
#  Version 1.1                                                             #
#  Go to GNS3 LABS for Jeff's EVPN LAB to use with or use with production  #
############################################################################


#########
#IMPORTS#
#########

#import PySimpleGUIWeb as sg ---> FOR WEB VERSION
import os
import sys
import netmiko
import getpass
import json
import PySimpleGUI as sg
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException


##### connect to switch  code library####
#from netmiko import ConnectHandler
#iosv_l2_s1 = {
#    'device_type': '',
#    'ip': '',
#    'username': 'test',
#    'password': 'test',
#}
#net_connect = ConnectHandler(**iosv_l2_s1)




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

######Application Information###################################################################
appinfo = '''    (C)2020 Applied Methodologies, Inc
Cisco Nexus 9000 Command version

ISIS Underlay version

NetMiko libray using Cisco_Ios as API device type

PySimpleGUI as GUI Library

Command line function - can run any command based on authorization level

Additional Command Buttons for SPINE/LEAFS can be added or changed easily

RESTful functionality to be added in future

Compiled with PyInstaller for mobile executable version

Source Code is located @ https://github.com/jsicuran/amilabs

Orginally built for GNS3 MP-BGP EVPN LAB @ https://gns3.com/marketplace/lab/bgp-evpn-lab '''

#################################################################################################


###WINDOW THEME #####
sg.theme('Light Blue')

##########################MAIN APPLICATION LOGIC FUNCTION ################################
def apprun():
    while True:
        event, values = window.read()
        if event in (None, 'Cancel', 'Exit'):
            break
        if event == 'Clear':
            window['-OUTPUT-'].update('')
        if event == 'Submit':
            cli_command = values['-CLI-']
            window['-OUTPUT-'].update(net_connect.send_command(cli_command))
        if event == 'NVE Overlay Setup':
            window['-OUTPUT-'].update(net_connect.send_command('sh run nv overlay all '))
        if event == 'BGP Summary':
            window['-OUTPUT-'].update(net_connect.send_command('sh bgp l2vpn evpn summ '))
        if event == 'BGP MAC Table':
            window['-OUTPUT-'].update(net_connect.send_command('sh bgp l2vpn evpn '))
        if event == 'Layer2 MAC Routes':
            window['-OUTPUT-'].update(net_connect.send_command('sh l2route mac all'))
        if event == 'BGP NLRI Type 2':
            window['-OUTPUT-'].update(net_connect.send_command('sh bgp l2vpn evpn route-type 2 '))
        if event == 'BGP Neighbors':
            window['-OUTPUT-'].update(net_connect.send_command('sh bgp l2vpn evpn neighbors '))
        if event == 'EVPN NEXT HOP':
            window['-OUTPUT-'].update(net_connect.send_command('sh bgp l2vpn evpn nexthop 0.0.0.0 '))
        if event == 'EVPN Paths':
            window['-OUTPUT-'].update(net_connect.send_command('sh bgp l2vpn evpn received-paths '))
        if event == 'VLANs':
            window['-OUTPUT-'].update(net_connect.send_command('sh vlan'))
        if event == 'VRFs':
            window['-OUTPUT-'].update(net_connect.send_command('sh vrf all detail'))
        if event == 'VXLAN':
            window['-OUTPUT-'].update(net_connect.send_command('sh vxlan '))
        if event == 'VXLAN Interfaces':
            window['-OUTPUT-'].update(net_connect.send_command('sh vxlan interface '))
        if event == 'VNI':
            window['-OUTPUT-'].update(net_connect.send_command('sh nve peer control-plane-vni '))
        if event == 'NVE Peers':
            window['-OUTPUT-'].update(net_connect.send_command('sh nve peers '))
        if event == 'NVE Peer Detail':
            window['-OUTPUT-'].update(net_connect.send_command('sh nve peers detail '))
        if event == 'VTEP Peers ':
            window['-OUTPUT-'].update(net_connect.send_command('sh nve vni peer-vtep '))
        if event == 'L2FWDR Mac':
            window['-OUTPUT-'].update(net_connect.send_command('sh system internal l2fwder mac  '))
        if event == 'L2RIB Topology History':
            window['-OUTPUT-'].update(net_connect.send_command('sh system internal l2rib event-history topology '))
        if event == 'L2RIB Error Logs':
            window['-OUTPUT-'].update(net_connect.send_command('sh system internal l2rib event-history error '))
        if event == 'L2FM ERROR LOG':
            window['-OUTPUT-'].update(net_connect.send_command('sh system internal l2fm errors '))
        if event == 'ISIS Interfaces':
            window['-OUTPUT-'].update(net_connect.send_command('sh isis interface brie '))
        if event == 'ISIS Interface Detail':
            window['-OUTPUT-'].update(net_connect.send_command('sh isis interface '))
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
        if event == 'ISIS CSNP Detail':
            window['-OUTPUT-'].update(net_connect.send_command('sh isis csnp detail '))
        if event == 'ISIS SPF Log':
            window['-OUTPUT-'].update(net_connect.send_command('sh isis spf-log '))
        if event == 'PIM Detail':
            window['-OUTPUT-'].update(net_connect.send_command('sh ip mroute detail '))
        if event == 'VNI Multicast Replication':
            window['-OUTPUT-'].update(net_connect.send_command('sh nve vni control-plane '))
        if event == 'VNI Ingress Replicaton':
            window['-OUTPUT-'].update(net_connect.send_command('sh nve vni ingress-replication '))
        if event == 'Application Information':
            window['-OUTPUT-'].update(print(appinfo))
        if event == 'Disconnect':  #### DISCONNECT FROM SWITCH
            net_connect.disconnect()
            window['-OUTPUT-'].update('')
            window['-OUTPUT-'].update(print("Disconnected from:" + IP_address))
            break
#######################END MAIN APPLICATION LOGIC################################################



###########################LAUNCH GUI############################################################

#################### LOGIN SCREEN LAYOUT ########################################################
layout = [[sg.Text('Enter IPv4 Address:', font=("bold")), sg.InputText(key='-IP-', size=(18, 1)),
            sg.Text('Switch Credentials(SSH ONLY):', font=("bold")), sg.Text('Enter Username:', font=("bold")),
            sg.InputText(key='-USER-', size=(22, 1)), sg.Text('Enter Password:', font=("bold")),
            sg.InputText(key='-PWD-', password_char="*", size=(22, 1))],
            [sg.Button('Login', size=(10,1)), sg.Button('Disconnect', size=(10,1)), sg.Cancel(), sg.Button('Application Information', size=(18,1))],
            [sg.Text('_' * 160)],
            [sg.Image(r'C:\Users\jsicu\Downloads\spineleaf1.png', pad=(350, 0))],
#####@@@@@@@******NOTE sg.Image COMMAND ABOVE MAY NEED TO BE REMOVED FOR MULTI .EXE PC DISTRIBUTION################

################## MAIN APPLICATION SCREEN LAYOUT ################################################
            [sg.Text('_'  * 160)],
            [sg.Text('BGP-EVPN FABRIC OVERLAY DETAIL - Address Family: L2VPN EVPN', font=("bold"))],
            [sg.Button('NVE Overlay Setup', tooltip='NVE Overlay running configuration'), sg.Button('BGP Summary'), sg.Button('BGP MAC Table', button_color=('white', 'green'), tooltip='BGP Type 2 NLRI TABLE'), sg.Button('Layer2 MAC Routes', tooltip="L2 MAC ROUTING TABLE"), sg.Button('BGP NLRI Type 2'), sg.Button('BGP Neighbors'), sg.Button('EVPN NEXT HOP', tooltip='Next HOP for Active Traffic'), sg.Button('EVPN Paths', tooltip='BGP EVPN Recived paths')],
            [sg.Text('VXLAN NVE/VNI Detail:', font=("bold"))],
            [sg.Button('VLANs', tooltip='vlans on device'), sg.Button('VRFs',tooltip='vrfs on device'), sg.Button('VXLAN', tooltip=' LEAF VXLAN VTEPs'), sg.Button('VXLAN Interfaces'), sg.Button('VNI', tooltip='VNI Control plane peers'), sg.Button('NVE Peers'), sg.Button('NVE Peer Detail', tooltip='Active peer summary'), sg.Button('VTEP Peers', tooltip='Active peer details'), sg.Button('L2FWDR Mac', tooltip='Layer 2 MAC Table'), sg.Button('L2RIB Topology History', tooltip='Topology Change log'), sg.Button('L2RIB Error Logs'),sg.Button('L2FM ERROR LOG', tooltip='L2 Finite-state Machine log')],
            [sg.Text('FABRIC UNDERLAY DETAIL - (for ISIS based systems):',font=("bold") )],
            [sg.Button('ISIS Interfaces', tooltip='ISIS Interfaces'), sg.Button('ISIS Interface Detail', tooltip='ISIS Interface details'), sg.Button('ISIS Adjacency', tooltip='ISIS Neighbors to SPINES'), sg.Button('ISIS Routing'), sg.Button('ISIS Topology'), sg.Button('ISIS Database'), sg.Button('ISIS Database Detail', tooltip='ISIS Database Detail'), sg.Button('ISIS CSNP Detail', tooltip='CSNP Informaion'), sg.Button('ISIS SPF Log', button_color=('black', 'orange'),  tooltip='ISIS SPF Change Log',)],
            [sg.Text('FABRIC Control Plane and BUM REPLICATION:',font=("bold") )],
            [sg.Button('PIM Detail', tooltip='PIM Detail'), sg.Button('VNI Multicast Replication', tooltip='Multicast Control Plane replication'), sg.Button('VNI Ingress Replicaton', tooltip='VNI Ingress replication if used')],
            [sg.Text('_'  * 160)],
            [sg.Text('COMMAND LINE AND REST ENTRY:', font=("bold"))],
            [sg.Button('Clear', size=(10, 1), tooltip='Clears window below'), sg.Button('Exit', button_color=('white', 'red'), size=(10, 1),  tooltip='EXIT Application')],
            [sg.Text('Enter CLI Command', font=("bold")), sg.InputText(key='-CLI-'), sg.Button('Submit')],
            [sg.Text('Enter REST API Command', font=("bold")), sg.InputText(key='-REST-'), sg.Text('JSON-RPC - Coming Soon')],
            [sg.Output(size=(160, 26), key='-OUTPUT-')],
            [sg.Text('2020 Applied Methodologies, Inc.')]]
                #####look into sg.output formatting vs. Json.
                ####print (json.dumps(ios_output, indent=4))

window = sg.Window('JEFFs BGP-EVPN LOOKING GLASS V1.1', layout)
    #### PUT IN LOGIN PROCESS AND ERROR HANDLING HERE#####
    #### 1st r evision is  one while loop process for all #####
    #### 2nd revision SPLIT INTO FUNCTIONS AND CALL#####
    ### test function call and then MAIN(): ######
    ### If cannot get single setup use popup window for login and transfer control###


while True:             ### MAIN SINGLE EVENT WHILE LOOP MASTER-LARGE version CALLS APPLICATION LOGIC FUNCTITON
    event, values = window.read()
    #print(event, values)   # Leave active to test button dictionary value
    if event in (None, 'Cancel', 'Exit'):
        break
    if event == 'Login':               #### CONNECT TO SWITCH
        IP_address = values['-IP-']
        username = values['-USER-']
        password = values['-PWD-']

        ios_device = {
            'device_type': 'cisco_ios',
            'ip': IP_address,
            'username': username,
            'password': password
        }
        ######ERROR EXCEPTION AND STATUS HANDLING######
        try:
            net_connect = ConnectHandler(**ios_device)
            window['-OUTPUT-'].update(print("Connected to:" + IP_address))
            apprun()    ####MAIN APPLICATION LOGIC CONTROL WHEN CONNECTED TO A SWITCH
        except (AuthenticationException):
            window['-OUTPUT-'].update(print("Check Credentials!"))
            continue
        except (NetMikoTimeoutException):
            window['-OUTPUT-'].update(print("Timeout to:" + IP_address))
            continue
        except (SSHException):
            window['-OUTPUT-'].update(print("Check SSH Setup!"))
            continue
        except Exception as unknown_error:
            window['-OUTPUT-'].update(print("Unknown Error:" + str(unknown_error)))
        continue
    if event == 'Application Information':
        window['-OUTPUT-'].update(print(appinfo))
    if event == 'Clear':
        window['-OUTPUT-'].update('')
#### SUCCESSFUL LOGIN LOOP TRANSFERS TO MAAIN APPLICATION LOGIC FUNCITION UNTIL DISCONNECT EVENT###########



window.close()



###GARBAGE COLLECTION ROUTINES###

###############
####END RUN####
###############




