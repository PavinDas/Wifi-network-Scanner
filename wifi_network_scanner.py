import os
import subprocess
import re


def get_available_wifi_networks_simple():
    # Use 'nmcli' to get available Wi-Fi networks (for Linux systems)
    try:
        networks = subprocess.check_output(
            ["nmcli", "-f", "SSID,BSSID,SIGNAL", "dev", "wifi"],
            stderr=subprocess.STDOUT,
        ).decode("utf-8")
        print("Available Wi-Fi Networks (SSID, BSSID, Signal Strength):")
        print(networks)
        return networks
    except subprocess.CalledProcessError as e:
        print(f"Error scanning networks: {e.output.decode('utf-8')}")
        return None


def get_available_wifi_networks_advance():
    # Run a system command to list available Wi-Fi networks (works on Linux/macOS)
    wifi_command = "nmcli dev wifi"

    try:
        networks = subprocess.check_output(wifi_command, shell=True).decode("utf-8")
        print("Available Wi-Fi Networks:")
        print(networks)
    except subprocess.CalledProcessError as e:
        print(f"Error finding networks: {e}")
        return None

    return networks


def get_ip_address_of_connected_wifi():
    # Get the IP address of the currently connected Wi-Fi interface
    try:
        # Run 'ip addr show' to get network interfaces and their IP addresses
        ip_result = subprocess.check_output("ip addr show", shell=True).decode("utf-8")
        # Extract the IP address associated with the Wi-Fi interface (usually wlan0)
        ip_addresses = re.findall(r"inet (\d+\.\d+\.\d+\.\d+)", ip_result)
        if ip_addresses:
            print(f"Connected Wi-Fi IP Address: {ip_addresses[0]}")
            return ip_addresses[0]
        else:
            print("No IP address found for connected Wi-Fi.")
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving IP address: {e}")
        return None


#! Calling Simple Wifi Checker
def simple_checker():
    get_available_wifi_networks_simple()
    # Step 2: Get the IP address of the connected Wi-Fi network (if connected)
    get_ip_address_of_connected_wifi()


#! Calling Advanced Wifi Checker
def advanced_checker():
    get_available_wifi_networks_advance()
    # Step 2: Get the IP address of the connected Wi-Fi network (if connected)
    get_ip_address_of_connected_wifi()


def select_choice():
    print("1. Simple Wifi Checker \n2. Advanced Wifi Checker")
    user_choice = input("_____________\nSelect one: ")

    if user_choice == "1":
        simple_checker()
    elif user_choice == "2":
        advanced_checker()
    else:
        print("Invalid input")
        select_choice()


select_choice()
