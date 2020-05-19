####
#PySimpleGUI usese main thread only by default
#Use multi-threading for Netmiko



#####
#imports
########
import PySimpleGUI as sg
import netmiko

##### connect to lab evpn switch ####
from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.1',
    'username': 'admin',
    'password': 'admin',
}

net_connect = ConnectHandler(**iosv_l2_s1)
output = net_connect.send_command('sh bgp l2vpn evpn ')
########################################################

############ LAUNCH GUI ################

sg.theme('Light Blue')

layout = [  [sg.Text('Press MAC ROUTE:')],
            [sg.Button('MAC ROUTES'), sg.Button('Clear'), sg.Button('Exit')],
            [sg.Output(size=(60,50), key='-OUTPUT-')],
            [sg.In(key='-IN-')]]


window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Clear':
        window['-OUTPUT-'].update('')
    if event == 'MAC ROUTES':
        window['-OUTPUT-'].update(output)
window.close()

###############
####END RUN####
###############




