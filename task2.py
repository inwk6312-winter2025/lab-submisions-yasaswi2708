from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task2.j2")
class NetworkInterface(object):
    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink

interface_obj = NetworkInterface("GigabitEthernet0/1", "Server Port", 10)
print(template.render(interface=interface_obj))
interface1 = NetworkInterface("GigabitEthernet0/2", "second port", 100, uplink=True)
print(template.render(interface=interface1))