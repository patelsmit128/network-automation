from netmiko import ConnectHandler

iosv_12={
	'device_type':'cisco_ios',
	'ip':'10.10.10.8',
	'username':'cisco',
	'password':'cisco'
}

net_connect=ConnectHandler(**iosv_12)

output=net_connect.send_command('show ip int brief')
print(output)


config_command=['int loop 10','ip address 10.1.1.1 255.255.255.0']
output=net_connect.send_config_set(config_command)
print(output)

# for n in range(2,21):
# 	print("creating vlan" + str(n))
# 	config_command=['vlan' + str(n) + 'name python_vlan' + str(n)]
# 	output=net_connect.send_config_set(config_command)
# 	print(output)
# 	