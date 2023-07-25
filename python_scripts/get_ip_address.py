import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

website = input("Enter the website domain ")
ip_address = get_ip_address(website)
if ip_address:
    print(f"The IP address of {website} is {ip_address}.")
else:
    print(f"Failed to get the IP address of {website}.")
