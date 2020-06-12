#####################################################################
#  PySimpleGUI uses main thread only by default                     #
#  Use multi-threading for Netmiko if necessary                     #
#  ***FNBLI DEV-OPS CORE SWITCH LOOKING GLASS APPLICATION***        #
#  JUNE 2020 Applied Methodologies, Inc                             #
#  Author: Jeff Sicuranza                                           #
#  LOGIN TO ANY DEVICE VERSION                                      #
#  IDE(PyCharm) based and complied runtime versions available       #
#  Version 1.3 buttons all work regardless of connection status     #
#  Not connected and buttons pressed will not exit application      #
#####################################################################


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
#    'device_type': 'hp_procurve',
#    'ip': '192.168.1.5',
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

###OLD SCHOOL CALL OUT TO COBOL RUNCOB#########

######Application Information###################################################################
appinfo = '''    (C)2020 Applied Methodologies, Inc
HP ARUBA J9851A #KB.16.08.0001 Command version

Some Command Buttons have hover over pop up descriptions

NetMiko libray using hp_procurve as API device type

PySimpleGUI as GUI Library

Command line function - can run any command based on authorization level

Additional Command Buttons for switches/routers can be added or changed easily

RESTful functionality to be added in future

Compiled with PyInstaller for mobile executable version

Source Code is located @ https://github.com/jsicuran/amilabs

Built for FNBLI Dual Core FAT SPINE Data Center for single pane monitoring '''

#################################################################################################






###WINDOW THEME #####
sg.theme('Green')

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
        if event == 'SSH CONNECTIONS':
            window['-OUTPUT-'].update(net_connect.send_command('sh ip ssh '))
        if event == 'VRRP CONFIG':
            window['-OUTPUT-'].update(net_connect.send_command('sh vrrp config global '))
        if event == 'VRRP SUMMARY':
            window['-OUTPUT-'].update(net_connect.send_command('sh vrrp summary '))
        if event == 'IP ASSIGNMENTS':
            window['-OUTPUT-'].update(net_connect.send_command('sh ip '))
        if event == 'ARP TABLE':
            window['-OUTPUT-'].update(net_connect.send_command('sh arp  '))
        if event == 'SWITCH MODULES':
            window['-OUTPUT-'].update(net_connect.send_command('sh modules details  '))
        if event == 'DTS STATUS':
            window['-OUTPUT-'].update(net_connect.send_command('sh distributed-trunking status '))
        if event == 'DTS CONFIG':
            window['-OUTPUT-'].update(net_connect.send_command('sh distributed-trunking config '))
        if event == 'DTS PEER KEEPALIVE':
            window['-OUTPUT-'].update(net_connect.send_command('sh distributed-trunking peer-keepalive '))
        if event == 'DTS CONSISTENCY':
            window['-OUTPUT-'].update(
                net_connect.send_command('sh distributed-trunking consistency-parameters trunk trk1 '))
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
        if event == 'BGP NEIGHBOR':
            window['-OUTPUT-'].update(net_connect.send_command('sh ip bgp neighbor '))
        if event == 'BGP LOGGING':
            window['-OUTPUT-'].update(net_connect.send_command('sh logging bgp '))
        if event == 'BGP AS PATH':
            window['-OUTPUT-'].update(net_connect.send_command('sh ip bgp route as-path '))
        if event == 'FISERV SPECIFIC 1':
            window['-OUTPUT-'].update('TO BE ADDED')
        if event == 'FISERV SPECIFIC 2':
            window['-OUTPUT-'].update('TO BE ADDED')
        if event == 'BOLT-ON VLAN STATS':
            window['-OUTPUT-'].update(net_connect.send_command('sh vlan 2000'))
        if event == 'CC PtP VLAN STATS':
            window['-OUTPUT-'].update('TO BE ADDED')
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
            [sg.Button('Login',size=(10,1)), sg.Button('Disconnect',size=(10,1)), sg.Cancel(), sg.Button('Application Information', size=(18,1))],
            [sg.Text('_' * 160)],
            # [sg.Text('Connection Status LOG:', font=("bold"))],
            # [sg.Output(size=(35, 5), key='-OUTPUT1-'),
            [sg.Image(r"C:\Users\jsicu\PycharmProjects\GNS3-AUTOMATION\FNBLI.png", size=(398, 96), pad=(400, 0))],
            #[sg.Text('******FNBLI CORE SWITCH LOOKING GLASS UTILITY******', pad=(400,0), font=("bold"))],
################## MAIN APPLICATION SCREEN LAYOUT ################################################
            [sg.Text('_'  * 160)],
            [sg.Text('INTERFACES - CONSOLE LOG - VLAN - VRRP - IP ASSIGNMENTS:', font=("bold"))],
            [sg.Button('CONNECTED NEIGHBORS'), sg.Button('INTERFACE ASSIGNMENTS'), sg.Button('INTERFACE PORT UTILIZATION'), sg.Button('REAL TIME INTERFACE STATISTICS'), sg.Button('VLAN ASSIGNMENTS'), sg.Button('SWITCH LOG', tooltip='Switch Log from most recent to old',  button_color=('white', 'blue')), sg.Button('SSH CONNECTIONS', tooltip='Show users logged into switch', button_color=('black', 'orange'))],
            [sg.Button('VRRP CONFIG'), sg.Button('VRRP SUMMARY'), sg.Button('IP ASSIGNMENTS'), sg.Button('ARP TABLE'), sg.Button('SWITCH MODULES')],
            [sg.Text('DISTRIBUTED TRUNKING/SPANNING TREE:', font=("bold"))],
            [sg.Button('DTS STATUS'), sg.Button('DTS CONFIG'), sg.Button('DTS PEER KEEPALIVE'), sg.Button('DTS CONSISTENCY'), sg.Button('SWITCH INTERCONNECT STATUS'), sg.Button('LACP'), sg.Button('LACP PEERS'), sg.Button('STP INCONSISTENT PORTS'), sg.Button('STP SUMMARY')],
            [sg.Text('BGP AND ROUTING:', font=("bold"))],
            [sg.Button('IP ROUTING TABLE'), sg.Button('ROUTE SUMMARY'), sg.Button('BGP TABLE'), sg.Button('BGP SUMMARY'), sg.Button('BGP GENERAL DETAILS'), sg.Button('BGP NEIGHBOR'), sg.Button('BGP LOGGING'), sg.Button('BGP AS PATH')],
            [sg.Button('BOLT-ON VLAN STATS', tooltip='Vendor BOLT ON VLAN STATS'), sg.Button('CC PtP VLAN STATS',tooltip='Crown Castle PtP Interface stats'), sg.Button('FISERV SPECIFIC 1',tooltip='Fiserv relevant stats'), sg.Button('FISERV SPECIFIC 2',tooltip='Fiserv relevant stats')],
            [sg.Button('Clear', tooltip='Clears window below'), sg.Button('Exit', button_color=('white', 'red'), size=(10, 1),  tooltip='EXIT Application')],
            [sg.Text('Enter CLI Command', font=("bold")), sg.InputText(key='-CLI-'), sg.Button('Submit')],
            [sg.Text('Enter REST API Command', font=("bold")), sg.InputText(key='-REST-'), sg.Text('JSON-RPC - Coming Soon')],
            [sg.Output(size=(158, 27), key='-OUTPUT-')],
            [sg.Text('2020 Applied Methodologies, Inc.')]]
                #####look into sg.output formatting vs. Json.
                ####print (json.dumps(ios_output, indent=4))

window = sg.Window('FNBLI CORE SWITCH LOOKING GLASS V1.3', layout)
    #### PUT IN LOGIN PROCESS AND ERROR HANDLING HERE#####
    #### 1st r evision is  one while loop process for all #####
    #### 2nd revision SPLIT INTO FUNCTIONS AND CALL#####
    ### test function call for SWLOGIN():  and then MAIN(): ######
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
            'device_type': 'hp_procurve',
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




