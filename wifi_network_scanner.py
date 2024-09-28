import subprocess
import re

#! Checking available wifi networks
def network_scanning():
    #? Linux comand for find available wifi networks
    wifi_command = "nmcli dev wifi"

    try:
        networks = subprocess.check_output(wifi_command, shell=True).decode("utf-8")
        print("Available Wi-Fi Networks:")
        print(networks)
    except subprocess.CalledProcessError as e:
        print(f"Error finding networks: {e}")



#! Get the IP address of the currently connected Wi-Fi interface
def connected_ip():
    try:
        ip_result = subprocess.check_output("ip addr show", shell=True).decode("utf-8")
        #? Extract the IP address
        ip_addresses = re.findall(r"inet (\d+\.\d+\.\d+\.\d+)", ip_result)
        if ip_addresses:
            print(f"Connected Wi-Fi IP Address: {ip_addresses[0]}")
        else:
            print("No IP address found.")
    except subprocess.CalledProcessError as e:s
        print(f"Error finding IP address: {e}")




#! Calling Wifi Checker
network_scanning()
connected_ip()