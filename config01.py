from netmiko import ConnectHandler

Juniper01 = {
    'device_type': 'juniper_junos',
    'ip': '10.0.0.2',
    'username': 'ieee',
    'password': 'comsoc',
##    'conn_timeout': 10
}

config = """
set interfaces ge-0/0/1 unit 0 family inet address 12.0.0.2/24
set interfaces lo0 unit 12 family inet address 12.12.12.2/32
set protocols ospf area 0.0.0.0 interface ge-0/0/1.0 interface-type p2p
set protocols ospf area 0.0.0.0 interface lo0.12
commit
"""

config_list = config.splitlines()

net_connect = ConnectHandler(**Juniper01)

output = net_connect.send_config_set(config_list)
print(output)