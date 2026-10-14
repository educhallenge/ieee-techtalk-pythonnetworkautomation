from netmiko import ConnectHandler

Cisco01 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.1',
    'username': 'ieee',
    'password': 'ieee',
}

net_connect = ConnectHandler(**Cisco01)

command_list = ["show version | include ios", "show ip int brief"]


for command in command_list:
    output = net_connect.send_command(command)
    prompt = net_connect.find_prompt()
    print("########" + prompt + command)
    print(output + "\n")

