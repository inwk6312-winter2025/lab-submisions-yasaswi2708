from netmiko import Netmiko

# Define the list of devices in the topology
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

# Loop through each device to retrieve uptime and configuration register
for device in devices:
    try:
        # Establish SSH connection to the device
        net_connect = Netmiko(**device)
        
        # Send the "show version" command to get uptime and configuration register details
        output = net_connect.send_command("show version")
        
        # Disconnect from the device
        net_connect.disconnect()

        # Extract uptime from the output
        uptime_start = output.find('uptime is')
        if uptime_start != -1:
            uptime_end = uptime_start + 38
            uptime = output[uptime_start:uptime_end]
            print(f"{device['ip']} => Uptime: {uptime}")
        else:
            print(f"{device['ip']} => Uptime not found.")

        # Extract configuration register from the output
        config_reg_start = output.find("Configuration register is")
        if config_reg_start != -1:
            config_reg_end = config_reg_start + 28
            config_register = output[config_reg_start:config_reg_end].split()[-1]
            print(f"{device['ip']} => Configuration Register: {config_register}")
        else:
            print(f"{device['ip']} => Configuration Register not found.")
    
    except Exception as e:
        print(f"Failed to connect to {device['ip']}. Error: {e}")
