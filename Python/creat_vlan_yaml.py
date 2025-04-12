# Description: This script creates a YAML file with VLAN configurations for an Arista switch.
# # It uses the pyeapi library to connect to the switch and the yaml library to handle YAML files.
# # The script first imports the necessary libraries: pyeapi for network device interaction and yaml for YAML file handling.        


import pyeapi
import yaml

file = open('vlans.yml','r')

vlan_dict = yaml.safe_load(file)

pyeapi.load_config('eapi.conf')

connect = pyeapi.connect_to('leaf1')
vlan_api = connect.api('vlans')


for switch in vlan_dict['switches']:
    connect = pyeapi.connect_to(switch)
    print(f"Connected to {switch}")
    
    vlan_api = connect.api('vlans')
    for vlan in vlan_dict['vlans']:
        vlan_id = vlan['id']
        vlan_name = vlan['name']
        print(f"Creating VLAN {vlan_id} with name {vlan_name}")
        vlan_api.create(vlan_id)
        vlan_api.set_name(vlan_id, vlan_name)
    print(f"VLAN {vlan_id} created with name {vlan_name} on {switch}")

# # It then opens a YAML file named 'vlans.yml' in read mode and loads its contents into a dictionary.
# # The script iterates over the devices listed in the YAML file and connects to each switch using pyeapi.  

# for switch in vlan_dict['switches']:
#     print(switch)
# print (vlan_dict['vlans'][0]['id']) 