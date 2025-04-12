# This script connects to a network device using pyeapi and retrieves the MAC address table.
#
# The script first imports the pyeapi library, which is used for interacting with network devices.
# It then establishes a connection to a device named 'leaf1' using the `connect_to` method.
# After establishing the connection, it retrieves the MAC address table using the `enable` method.
# The MAC address table is accessed through the `unicastTable` key in the result dictionary.
# The script then iterates over the entries in the MAC address table, extracting the MAC addresses and storing them in a set to avoid duplicates.
# Finally, it prints each unique MAC address from the set.

import pyeapi

import yaml

file = open('vlans.yml','r')

vlan_dict = yaml.safe_load(file)

pyeapi.load_config('eapi.conf')

connect = pyeapi.connect_to('leaf1')


connect = pyeapi.connect_to('leaf1')
cmd_result = connect.enable(['show mac-address-table'])

print(cmd_result[0]['result'])


mac_table_set = set()
mac_table_dict = cmd_result[0]['result']['unicastTable']['tableEntries']
for mac in mac_table_dict:
    mac_table_set.add(mac['macAddress'])
for mac_entry in mac_table_set:
    print(mac_entry)
# The script retrieves the MAC address table using the `enable` method and stores the result in `cmd_result`.
# The MAC address table is accessed through the `unicastTable` key in the result dictionary.
# The script then iterates over the entries in the MAC address table, extracting the MAC addresses and storing them in a set to avoid duplicates.
# Finally, it prints each unique MAC address from the set.