import socket
import os

# Define the network subnet to scan
subnet = '192.168.1.'

# Define IP address ranges for each category
paziresh_range = range(50, 86)
hemato_range = range(86, 101)
tests_range = range(101, 151)
genetic_range = range(151, 181)
edari_range = range(181, 201)

# Initialize empty dictionaries for each category
paziresh_devices = {}
hemato_devices = {}
tests_devices = {}
genetic_devices = {}
edari_devices = {}

# Loop through all possible IP addresses in the subnet and attempt to ping each one
for i in range(1, 256):
    ip = subnet + str(i)
    response = os.system('ping -n 1 ' + ip)
    if response == 0:
        # If the ping is successful, try to resolve the IP address to a hostname
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = 'Unknown'
        # Determine the category of the device based on its IP address
        if i in paziresh_range:
            paziresh_devices[hostname] = ip
        elif i in hemato_range:
            hemato_devices[hostname] = ip
        elif i in tests_range:
            tests_devices[hostname] = ip
        elif i in genetic_range:
            genetic_devices[hostname] = ip
        elif i in edari_range:
            edari_devices[hostname] = ip

# Ask the user to select a category
print('Select a category:')
print('1. Paziresh')
print('2. Hemato')
print('3. Tests Room')
print('4. Genetic')
print('5. Edari')
category = int(input())

# Display an empty IP address for the selected category
if category == 1:
    for i in paziresh_range:
        ip = subnet + str(i)
        if ip not in paziresh_devices.values():
            print(f'Empty IP address in Paziresh category: {ip}')
            break
elif category == 2:
    for i in hemato_range:
        ip = subnet + str(i)
        if ip not in hemato_devices.values():
            print(f'Empty IP address in Hemato category: {ip}')
            break
elif category == 3:
    for i in tests_range:
        ip = subnet + str(i)
        if ip not in tests_devices.values():
            print(f'Empty IP address in Tests Room category: {ip}')
            break
elif category == 4:
    for i in genetic_range:
        ip = subnet + str(i)
        if ip not in genetic_devices.values():
            print(f'Empty IP address in Genetic category: {ip}')
            break
elif category == 5:
    for i in edari_range:
        ip = subnet + str(i)
        if ip not in edari_devices.values():
            print(f'Empty IP address in Edari category: {ip}')
            break
else:
    print('Invalid category selected')