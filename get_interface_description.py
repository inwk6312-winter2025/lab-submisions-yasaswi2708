from netmiko import ConnectHandler

# Define devices
r1 = {"device_type": "cisco_ios",
"ip": "192.168.1.101",
"username": "student",
"password": "Meilab123",
"port": "22"}

r2 = {"device_type": "cisco_ios",
"ip": "192.168.1.101",  # The IP here should be different for r2
"username": "student",
"password": "Meilab123",
"port": "22"}

# Loop through devices and retrieve interface descriptions
for device in (r1, r2):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show interface description")
    net_connect.disconnect()
    print("-"*100)
    print(output)
    print("-"*100)
