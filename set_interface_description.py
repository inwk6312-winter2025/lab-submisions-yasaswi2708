'''
from netmiko import Netmiko

# Define the list of devices in your network
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Router 1
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    }
]

# Define the description text for the interface
description = 'Description set with Netmiko'

# List of configuration commands to set the description on the interface
description_config = [
    "interface GigabitEthernet3",  # Interface to be configured
    f"description {description}"    # Set the description
]

# Loop through devices and apply the configuration
for device in devices:
    # Establish SSH connection to the device
    net_connect = Netmiko(**device)
    
    # Send the configuration commands to the device
    output = net_connect.send_config_set(description_config)
    
    # Print the output of the commands
    print(output)
    
    # Disconnect from the device
    net_connect.disconnect()
'''
from netmiko import Netmiko

# Define the list of devices in your network
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Router 1
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    }
]

# Define the description text for the interface
description = 'Description set with Netmiko'

# List of configuration commands to set the description on GigabitEthernet3 and add a Loopback interface
description_config = [
    "interface GigabitEthernet3",            # Enter interface GigabitEthernet3
    f"description {description}",            # Set description
    "exit",                                 # Exit from GigabitEthernet3 interface config
    "interface Loopback0",                   # Create Loopback interface
    "ip address 192.168.100.1 255.255.255.0", # Assign IP address to the Loopback interface
    "exit",                                 # Exit from Loopback0 interface config
    "end"                                    # Exit global configuration mode
]

# Loop through devices and apply the configuration
for device in devices:
    # Establish SSH connection to the device
    net_connect = Netmiko(**device)
    
    # Send the configuration commands to the device
    output = net_connect.send_config_set(description_config)
    
    # Print the output of the commands
    print(output)
    
    # Disconnect from the device
    net_connect.disconnect()
