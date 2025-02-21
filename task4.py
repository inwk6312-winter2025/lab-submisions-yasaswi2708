from jinja2 import Environment, FileSystemLoader

# Load the template from the current directory
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task4.j2")

# Define the NetworkInterface class
class NetworkInterface:
    def __init__(self, description, vlan):
        self.description = description
        self.vlan = vlan

# Create an interface object
interface_obj = NetworkInterface("User Port", 30)

# Generate a list of ports (GigabitEthernet0/1 to GigabitEthernet0/10)
ports = [{"name": f"GigabitEthernet0/{n+1}"} for n in range(10)]

# Render and print the output
print(template.render(interface=interface_obj, ports=ports))
   