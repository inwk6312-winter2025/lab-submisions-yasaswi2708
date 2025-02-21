'''from netmiko import Netmiko

# Define device
device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}

# Establish connection
net_connect = Netmiko(**device)

# Send the "show ip interface brief" command and store the output
output = net_connect.send_command("show ip interface brief")

# Disconnect from the device
net_connect.disconnect()

# Print the type of output
print(type(output)) '''

from netmiko import Netmiko

# Define a list of devices in the topology
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

# Loop through each device to retrieve and parse interface information
for device in devices:
    try:
        # Establish SSH connection to the device
        net_connect = Netmiko(**device)

        # Send the "show ip interface brief" command and parse the output using TextFSM
        output = net_connect.send_command("show ip interface brief", use_textfsm=True)

        # Print the parsed output for each device
        print(f"Interfaces on {device['ip']}:\n")
        for interface in output:
            print(f"Interface: {interface['interface']}")
            print(f"IP Address: {interface['ip_address']}")
            print(f"Status: {interface['status']}")
            print(f"Protocol: {interface['proto']}")
            print("-" * 50)

        # Disconnect from the device
        net_connect.disconnect()

    except Exception as e:
        print(f"Failed to connect to {device['ip']}. Error: {e}")
