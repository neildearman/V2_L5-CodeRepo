# This script connects to a list of network switches using pyeapi and retrieves their running configurations.
# It saves each configuration to a separate text file in a specified directory.
# Ensure you have the necessary permissions and configurations set up for pyeapi to work correctly.
# The script handles connection errors and other exceptions gracefully, providing feedback on the status of each operation.
# Description: This script connects to a list of network switches using pyeapi and retrieves their running configurations.
# It saves each configuration to a separate text file in a specified directory.
# It handles connection errors and other exceptions gracefully, providing feedback on the status of each operation.
# This script is designed to be run in an environment where pyeapi is installed and configured.

import pyeapi
import os

pyeapi.load_config('eapi.conf')

directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)
    print(f"Directory '{directory}' created.")

switches = ['leaf1', 'leaf2', 'leaf3']
for switch in switches:
    try:
        node = pyeapi.connect(transport='https', host=switch, username='admin', password='admin')
        response = node.get_config()
        filename = os.path.join(directory, f"{switch}_running_config.txt")
        
        with open(filename, 'w') as file:
            file.write(response['result'])
        
        print(f"Configuration for {switch} saved to {filename}")
    except pyeapi.eapilib.ConnectionError as e:
        print(f"Failed to connect to {switch}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# This script connects to a list of network switches using pyeapi and retrieves their running configurations.
# It saves each configuration to a separate text file in a specified directory.
# Ensure you have the necessary permissions and configurations set up for pyeapi to work correctly.
# The script handles connection errors and other exceptions gracefully, providing feedback on the status of each operation.
# Ensure you have the necessary permissions and configurations set up for pyeapi to work correctly.
# The script handles connection errors and other exceptions gracefully, providing feedback on the status of each operation.
# The script is designed to be run in an environment where pyeapi is installed and configured.
# The script is designed to be run in an environment where pyeapi is installed and configured.