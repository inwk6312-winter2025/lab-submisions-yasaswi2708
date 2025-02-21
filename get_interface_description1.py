from netmiko import ConnectHandler

# Define devices in a list (you can add more devices here as needed)
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Router 1
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # Router 2
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # Router 3
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    }
]

# Loop through each device and retrieve interface descriptions and other show commands
for device in devices:
    try:
        # Establish SSH connection to the device
        net_connect = ConnectHandler(**device)
        
        # Send the "show interface description" command to get interface descriptions
        output = net_connect.send_command("show interface description")
        
        # Optionally, you can add more "show" commands here
        output2 = net_connect.send_command("show ip interface brief")
        
        # Disconnect from the device
        net_connect.disconnect()
        
        # Print the output (interface descriptions)
        print("-" * 100)
        print(f"Device: {device['ip']} => Interface Descriptions")
        print(output)
        print("-" * 100)
        
        # You can also print other "show" commands as needed
        print(f"Device: {device['ip']} => IP Interface Brief")
        print(output2)
        print("-" * 100)
        
    except Exception as e:
        print(f"Failed to connect to {device['ip']}. Error: {e}")

