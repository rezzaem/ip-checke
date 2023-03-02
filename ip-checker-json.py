import json
import subprocess

# define the network subnet
subnet = "192.168.1."

# define device categories and their IP ranges
device_categories = {
    "Paziresh": range(50, 86),
    "Hemato": range(86, 101),
    "Tests Room": range(101, 151),
    "Genetic": range(151, 171),
    "Edari": range(171, 201),
    "machines":[128]
}

# check for active IPs
nmap_output = subprocess.check_output(["nmap", "-sP", subnet + "0/24"]).decode('utf-8')

# create a dictionary to store the active IPs
active_ips = {}

# extract the IPs and device names from the nmap output
for line in nmap_output.split("\n"):
    if "Nmap scan report for" in line:
        ip = line.split()[-1]
    elif "MAC Address" in line:
        device_name = line.split("(")[-1].strip(")")
        active_ips[ip] = device_name

# categorize the active IPs
categorized_ips = {}
for category, ip_range in device_categories.items():
    categorized_ips[category] = []
    for ip, device_name in active_ips.items():
        last_octet = int(ip.split(".")[-1])
        if last_octet in ip_range:
            categorized_ips[category].append(ip)

# save the categorized IPs to a JSON file
with open("categorized_ips.json", "w") as f:
    json.dump(categorized_ips, f, indent=4)

# print the categorized IPs
for category, ips in categorized_ips.items():
    print(category + ": " + ", ".join(ips))
