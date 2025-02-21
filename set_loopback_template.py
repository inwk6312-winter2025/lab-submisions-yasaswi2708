import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko

# Load the hosts (router) details from the YAML file
hosts = yaml.load(open('hosts.yml'), Loader=yaml.SafeLoader)

# Load the interface details (loopback configuration) from the YAML file
interfaces = yaml.load(open('interfaces.yml'), Loader=yaml.SafeLoader)

# Set up the Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, autoescape=True)
template = env.get_template('interfaces_config_template.j2')

# Render the loopback configuration using the interface data
loopback_config = template.render(data=interfaces)

# Loop through the hosts and apply the configuration
for host in hosts["hosts"]:
    # Establish SSH connection using Netmiko
    net_connect = Netmiko(
        host=host["name"],
        username=host["username"],
        password=host["password"],
        port=host["port"],
        device_type=host["type"]
    )
    
    print(f"Logged into {host['name']} successfully")
    
    # Send the configuration to the router
    output = net_connect.send_config_set(loopback_config.split("\n"))
    
    print(f"Pushed config into {host['name']} successfully")
    
    # Disconnect from the device
    net_connect.disconnect()

print("Done!")
