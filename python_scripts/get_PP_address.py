import socket

def get_ip_addresses(domain):
    try:
        # Get the primary IP address (public IP)
        public_ip = socket.gethostbyname(domain)

        # Get all IP addresses associated with the domain (private IPs)
        private_ips = socket.gethostbyname_ex(domain)[2]

        return public_ip, private_ips
    except socket.gaierror:
        return None, None

def main():
    domain = input("Enter the domain name: ")
    public_ip, private_ips = get_ip_addresses(domain)

    if public_ip:
        print(f"The public IP address of {domain} is {public_ip}.")
    else:
        print(f"Failed to get the public IP address of {domain}.")

    if private_ips:
        print(f"The private IP addresses of {domain} are:")
        for ip in private_ips:
            print(ip)
    else:
        print(f"Failed to get the private IP addresses of {domain}.")

if __name__ == "__main__":
    main()
