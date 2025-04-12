
# This script configures IP addresses on interfaces of Arista switches
# using the pyeapi library and a YAML configuration file.
# The YAML file should contain the switch names and their respective
# interfaces with IP addresses and subnet masks.

import pyeapi
import yaml

pyeapi.load_config('eapi.conf')

file = ('interface.yml', 'r')
interface.dict = yaml.safe_load(file)

for switch in interface.dict['devices']:
    connect = pyeapi.connect_to(switch)
    int_api = connect.api('ipinterfaces')
    for interface in interface.dict['devices'][switch]['interfaces']:
        ip = interface.dict['devices'][switch]['interfaces'][interface]['ip']
        mask = interface.dict['devices'][switch]['interfaces'][interface]['mask']
        mask = str(mask)
        ip_mask = ip + '/' + mask
        int_api.create(interface)
        int_api.set_ip_address(interface, ip_mask)