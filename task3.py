from jinja2 import Environment, FileSystemLoader

# Load templates from the current directory
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task3.j2")

# Define the NetworkInterface class
class NetworkInterface:
    def __init__(self, description, vlan):
        self.description = description
        self.vlan = vlan

# Create an interface object
interface_obj = NetworkInterface("User Port", 20)

# Render and print the output
print(template.render(interface=interface_obj))
