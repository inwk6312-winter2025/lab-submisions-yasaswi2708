from netmiko import Netmiko

device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",  # Router 1
    "username": "student",
    "password": "Meilab123",
    "secret": "cisco",  # The enable password for the device
    "port": "22",
}

# Establish SSH connection
net_connect = Netmiko(**device)

# Print the default prompt
print(f"Default prompt: {net_connect.find_prompt()}")

# Send the "disable" command to exit privileged exec mode
net_connect.send_command_timing("disable")
print(f"Disable command: {net_connect.find_prompt()}")

# Enter enable mode with the secret password
net_connect.enable()
print(f"Enable command: {net_connect.find_prompt()}")
