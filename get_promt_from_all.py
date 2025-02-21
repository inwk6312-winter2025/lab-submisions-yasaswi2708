from netmiko import Netmiko

# Define the list of devices in your topology
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Router 1
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # Router 2
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # Router 3
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    }
]

# Loop through each device and fetch its prompt
for device in devices:
    try:
        # Establish SSH connection to the device
        net_connect = Netmiko(**device)
        
        # Print the default prompt
        print(f"Connected to {device['ip']}")
        print(f"Default prompt: {net_connect.find_prompt()}")
        
        # Send the "disable" command to exit privileged exec mode
        net_connect.send_command_timing("disable")
        print(f"After 'disable' command: {net_connect.find_prompt()}")
        
        # Enter enable mode with the secret password
        net_connect.enable()
        print(f"After 'enable' command: {net_connect.find_prompt()}")
        
        # Close the connection
        net_connect.disconnect()
        
    except Exception as e:
        print(f"Failed to connect to {device['ip']}. Error: {e}")
