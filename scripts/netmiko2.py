from netmiko import ConnectHandler

iosv_12={
	'device_type':'cisco_ios',
	'ip':'10.10.10.8',
	'username':'cisco',
	'password':'cisco'
}
iosv_13={
	'device_type':'cisco_ios',
	'ip':'10.10.10.9',
	'username':'cisco',
	'password':'cisco'
}
iosv_14={
	'device_type':'cisco_ios',
	'ip':'10.10.10.11',
	'username':'cisco',
	'password':'cisco'
}
all_device=[iosv_12,iosv_13,iosv_14]
for device in all_device:
	net_connect=ConnectHandler(**device)
	# config_command=['int loop 20','ip address 20.1.1.1 255.255.255.0','router ospf 100','network 0.0.0.0 0.0.0.0 area 0']
	# output=net_connect.send_config_set(config_command)
	# print(output)
	config_command=['int loop 30','ip address 30.1.1.1 255.255.255.0']
	output=net_connect.send_config_set(config_command)
	print(output)


