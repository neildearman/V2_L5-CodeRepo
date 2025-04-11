# switch = 'leaf1'
# ip = '192.168.1.1'

# print (f"Hostname is {switch} with an IP Address of {ip}")

# for i in range(1, 10,2):
#     print (f"Switch {i} is up and running")
#     if i == 5:
#         print (f"Switch {i} is down")
#         break

# set_demo = {1, 2, 3, 4, 5}
# set_demo.add(6)
# set_demo.add(6)

# print(set_demo)

# list_demo = [1, 2, 3, 4, 5]
# list_demo.append(6)

# print (list_demo[0])
# print (list_demo)

# numbers = [1, 2, 3, 4, 5]

# colours = ['red', 'green', 'blue']
# for number in numbers:
#     print (number)
#     for colour in colours:
#         print (colour)
        
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# for planet in planets:
#     print (planet)
#     if planet == 'Earth':
#         print (f"{planet} is the third planet from the Sun")
#     elif planet == 'Mars':
#         print (f"{planet} is the fourth planet from the Sun")
#     elif planet == 'Jupiter':
#         print (f"{planet} is the fifth planet from the Sun")
#     elif planet == 'Saturn':
#         print (f"{planet} is the sixth planet from the Sun")
#     elif planet == 'Uranus':
#         print (f"{planet} is the seventh planet from the Sun")
#     elif planet == 'Neptune':
#         print (f"{planet} is the eighth planet from the Sun")

# switches = {'spine1' : '192.168.1.1',
#             'spine2' : '192.168.2.2',
#             'spine3' : '192.168.3.3'}

# for switch, ip in switches.items():
#     print (f"Hostname is {switch} with an IP Address of {ip}")

# for host in switches:
#     print(host)

# for host in switches:
#     print(switches[host])

# for host in switches:
#     print(f"Hostname is {host} with an IP Address of {switches[host]}")


# number1 = 1
# number2 = 2

# sum = number1 + number2
# print (f"The sum of {number1} and {number2} is {sum}")

import pyapi

pyapi.load_config('eapi.conf')
connect = pyapi.connect_to('leaf1)' 
request_cmd = connect.enable('show mac-address-table')
print(request_cmd)

')