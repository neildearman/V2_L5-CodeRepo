# Description: This script creates a VLAN on an Arista switch using the pyeapi library.
# It connects to the switch, creates a VLAN with ID 10, and sets its name to 'DMZ'.
#
# The script first imports the pyeapi library, which is used for interacting with network devices.
# It then loads the configuration file 'eapi.conf' to establish the connection settings.
# The script connects to a switch named 'leaf1' using the `connect_to` method.
# After establishing the connection, it accesses the VLAN API and creates a VLAN with ID 10.
# The VLAN is then named 'DMZ' using the `set_name` method of the VLAN API.
# Finally, the script prints a message indicating that the VLAN has been created successfully.
# This script is designed to be run in an environment where pyeapi is installed and configured.
# This script creates a VLAN on an Arista switch using the pyeapi library.
# It connects to the switch, creates a VLAN with ID 10, and sets its name to 'DMZ'.

import pyeapi

pyeapi.load_config('eapi.conf')
connect = pyeapi.connect_to('leaf1')
vlan_api = connect.api('vlans')
vlan_api.create('10')
vlan_api.set_name('10', 'DMZ')

