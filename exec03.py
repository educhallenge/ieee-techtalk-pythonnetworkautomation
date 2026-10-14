from netmiko import ConnectHandler

def exec(command_list):
    for command in command_list:
        output = net_connect.send_command(command)
        prompt = net_connect.find_prompt()
        print("########" + prompt + command)
        print(output + "\n")

Cisco01 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.1',
    'username': 'ieee',
    'password': 'ieee',
}

Juniper01 = {
    'device_type': 'juniper_junos',
    'ip': '10.0.0.2',
    'username': 'ieee',
    'password': 'comsoc',
##    'conn_timeout': 10
}

device_list = [Cisco01 , Juniper01]
ios_cmdlist = ["show version | include ios" , "show ip int brief"]
junos_cmdlist = ["show system information", 'show interface terse | match "ge|fxp"']

for device in device_list:
    net_connect = ConnectHandler(**device)
    if device["device_type"] == "cisco_ios":
        exec(ios_cmdlist)
    elif device["device_type"] == "juniper_junos":
        exec(junos_cmdlist)
