from netmiko import ConnectHandler

Cisco01 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.1',
    'username': 'ieee',
    'password': 'ieee',
}

net_connect = ConnectHandler(**Cisco01)

output = net_connect.send_command("show version | include ios")
print(output)

