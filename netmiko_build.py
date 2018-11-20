from netmiko import ConnectHandler
from getpass import getpass

fg_default = {
    'device_type':'fortinet_ssh',
    'ip':'192.168.1.99',
    'username':'admin',
    'password':''
}

miko_devices = [fg_default]

with open('netmiko_config.txt') as f:
    lines = f.read().splitlines()

for device in miko_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(lines)
    print(output)
