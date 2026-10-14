from netmiko import ConnectHandler

Cisco01 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.1',
    'host': 'Cisco01',
    'username': 'ieee',
    'password': 'ieee',
}

Cisco01_config = """
interface Loopback12
 ip address 12.12.12.1 255.255.255.255
 ip ospf 100 area 0
interface GigabitEthernet0/1
 no switchport
 ip address 12.0.0.1 255.255.255.0
 ip ospf network point-to-point
 ip ospf 100 area 0
"""

Juniper01 = {
    'device_type': 'juniper_junos',
    'ip': '10.0.0.2',
    'host': 'Juniper01',
    'username': 'ieee',
    'password': 'comsoc',
##    'conn_timeout': 10
}

Juniper01_config = """
set interfaces ge-0/0/1 unit 0 family inet address 12.0.0.2/24
set interfaces lo0 unit 12 family inet address 12.12.12.2/32
set protocols ospf area 0.0.0.0 interface ge-0/0/1.0 interface-type p2p
set protocols ospf area 0.0.0.0 interface lo0.12
commit
"""

device_list = [Cisco01 , Juniper01]

for device in device_list:
    net_connect = ConnectHandler(**device)
    hostname = device["host"]
    config = eval(hostname + "_config")
    config_list = config.splitlines()
    output = net_connect.send_config_set(config_list)
    print(output)
