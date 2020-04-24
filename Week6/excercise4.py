'''
Use send_config_set() and send_config_from_file() to make configuration changes. 

The configuration changes should be benign. For example, on Cisco IOS I typically change the logging buffer size. 
'''
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass


def output_printer(output):
    print()
    print('-' * 80)
    print(output)
    print('-' * 80)
    print()

'''
try:
    host = raw_input("Enter host to connect to: ")
except NameError:
    host = input("Enter host to connect to: ")
'''
password = getpass()
device = {
    'host': '192.168.255.2',
    'username': 'root',
    'password': password,
    'device_type': 'cisco_ios',
}

net_connect = Netmiko(**device)

# Use send_config_set() to make config change
config = ['vlan 200', 'int vlan 200', 'ip add 192.168.200.1 255.255.255.0']
output = net_connect.send_config_set(config)
output_printer(output)

# Use send_config_from_file() to make config change
#output = net_connect.send_config_from_file('config.txt')
#output_printer(output)


message = "Verifying config change\n"
output = net_connect.send_command("show run | inc Vlan")
if '200' in output:
    message += "Vlan created!"
else:
    message += "We failed"
output_printer(message)
