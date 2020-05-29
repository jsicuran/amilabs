####Main SSH LOGIN HANDLER####
####2020 AMI Inc. Jeff Sicuranza#####
#####################################

######################USE CASES#################################
### 1). FRONT END GUI POP UP FOR DEVICE LOGIN              #####
### 2). COOKBOOK CODE TO INTEGRATE INTO LARGER APPLICAITON #####
### 3). QUICK SSH TESTER FOR NETWORK DEVICES               #####
################################################################

#####IMPORTS#####
import PySimpleGUI as sg
import netmiko
import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import os
import sys
########################


####NetMiko device reference#####
#aruba_os
#hp_procurve
#hp_comware
#cisco_ios
##################################

#################GUI BUILD LAYOUT###################



layout = [[sg.Text('Enter IP Address:')],
                 [sg.InputText(key='-IP-')],
                 [sg.Text('Switch Credentials(SSH ONLY):')],
                 [sg.Text('Enter Username:')],
                 [sg.InputText(key='-USER-')],
                 [sg.Text('Enter Password:')],
                 [sg.InputText(key='-PWD-')],
                 [sg.Submit(), sg.Cancel(), sg.Button('Disconnect')],
                 [sg.Text('Connection Status:')],
                 [sg.Output(size=(43, 10), key='-OUTPUT-')]]

window = sg.Window('Connect to Switch', layout)
#######MAIN ROUTINE#####################
while True:             # MAIN Event Loop
    event, values = window.read()
    #print(event, values)   # Leave active to test button dictionary value
    if event in (None, 'Cancel'):       ####EVENT = CANCEL QUITS APPLICATION
        break
    #if event == 'Clear':               ###CAN BE USED TO CLEAR WINDOW LOG
        #window['-OUTPUT-'].update('')
    if event == 'Submit':               #### CONNECT TO SWITCH
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
            window['-OUTPUT-'].update(print("Connected to:" + IP_address ))
            continue
        except (AuthenticationException):
            window['-OUTPUT-'].update(print("Check Credentials!"))
            continue
        except (NetMikoTimeoutException):
            window['-OUTPUT-'].update(print("Timeout to:" + IP_address ))
            continue
        except (SSHException):
            window['-OUTPUT-'].update(print("Check SSH Setup!"))
            continue
        except Exception as unknown_error:
            window['-OUTPUT-'].update(print("Unknown Error:" + str(unknown_error)))
        continue
    if event == 'Disconnect':            #### DISCONNECT FROM SWITCH
        net_connect.disconnect()
        window['-OUTPUT-'].update(print("Disconnected from:" + IP_address ))

#################CLOSE WINDOW##############

window.close()
##########################################

###############
####END RUN####
###############
